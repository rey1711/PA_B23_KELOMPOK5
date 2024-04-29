from collections import deque
from colorama import init, Fore
import mysql.connector
from mysql.connector import Error

class SingletonLogger:
   _instance = None
   _connection = None

   def __new__(cls):
      if cls._instance is None:
         cls._instance = super().__new__(cls)
         cls._instance.connect_to_database()
      return cls._instance

   def connect_to_database(self):
      try:
         hostname = "462.h.filess.io"
         database = "reytop3_perfectly"
         port = "3306"
         username = "reytop3_perfectly"
         password = "73bac833e2e1437cc2e127b57d2a70b7b4f11308"

         self._connection = mysql.connector.connect(
               host=hostname,
               database=database,
               user=username,
               password=password,
               port=port
         )
         if self._connection.is_connected():
               db_Info = self._connection.get_server_info()
               print("Connected to MySQL Server version ", db_Info)
      except Error as e:
         print("Error while connecting to MySQL", e)

   def log(self, message):
      print(message)

   def close_connection(self):
      if self._connection:
         self._connection.close()
         print("Connection to database closed.")

logger1 = SingletonLogger()
logger2 = SingletonLogger()

if logger1 is logger2:
   print("Instance sama, singleton berhasil")

logger1.log("This is a log message")

logger1.close_connection()

class User:
   def __init__(self, username, password):
      self.username = username
      self.password = password

class Admin(User):
   def __init__(self, username, password, shop):
      if shop.authenticate_admin(username, password):
         super().__init__(username, password)
         self.shop = shop  
      else:
         raise ValueError("Invalid username or password.")

   def delete_order(self, customer_name):
      try:
         for order in self.shop.order_queue:  
               if order[0] == customer_name:
                  self.shop.order_queue.remove(order)
                  print(Fore.GREEN + f"Order for {customer_name} deleted successfully.")
                  return
         print(Fore.RED + f"No order found for customer '{customer_name}'.")
      except Exception as e:
         print(Fore.RED + f"An error occurred: {str(e)}")

class Customer(User):
   def __init__(self, username, password, shop):
      if shop.authenticate_user(username, password):
         super().__init__(username, password)
         self.shop = shop
      else:
         raise ValueError("Invalid username or password.")

   def place_order(self, order_type, id_barang, quantity, days=1):
      try:
         found = False
         id_barang = int(id_barang)
         for laptop in self.shop.barang:
               if laptop.get('id_barang') == id_barang:
                  stock = int(laptop['stock'])
                  harga = int(laptop['harga']) 
                  nama_barang = laptop['nama_barang']
                  total_harga = harga * quantity 
                  if stock >= quantity:
                     order = (id_barang, quantity, order_type, days, total_harga) 
                     self.shop.order_queue.append(order)
                     try:
                           connection = self.shop.connect_to_database()
                           if connection:
                              cursor = connection.cursor(dictionary=True)
                              if order_type == "pembelian":
                                 cursor.execute("""
                                       INSERT INTO transaksi (id_transaksi, id_barang, total_barang)
                                       VALUES (DEFAULT, %s, %s)
                                 """, (id_barang, quantity)) 
                                 cursor.execute("""
                                       INSERT INTO pembelian (id_pembelian, id_transaksi, tanggal_pembelian, total_harga)
                                       VALUES (DEFAULT, LAST_INSERT_ID(), CURRENT_DATE(), %s)
                                 """, (total_harga,))
                              elif order_type == "penyewaan":
                                 jaminan = input("Masukkan jaminan: ")
                                 cursor.execute("""
                                       INSERT INTO transaksi (id_transaksi, id_barang, total_barang)
                                       VALUES (DEFAULT, %s, %s)
                                 """, (id_barang, quantity)) 
                                 from datetime import datetime, timedelta
                                 today = datetime.now()
                                 return_date = today + timedelta(days=days)
                                 cursor.execute("""
                                       INSERT INTO penyewaan (id_penyewaan, id_transaksi, tanggal_minjam, jaminan, tanggal_kembali, total_harga)
                                       VALUES (DEFAULT, LAST_INSERT_ID(), CURRENT_DATE(), %s, %s, %s)
                                 """, (jaminan, return_date.strftime('%Y-%m-%d'), total_harga))
                              connection.commit()
                              connection.close()
                     except Exception as e:
                           print(Fore.RED + f"Failed to insert transaction data: {str(e)}")
                     if order_type == "pembelian":  
                           laptop['stock'] = str(stock - quantity)
                           print(Fore.GREEN + f"Order placed by {self.username}: {quantity} {nama_barang.capitalize()}(s)")
                     elif order_type == "penyewaan":  
                           price_per_day = harga / 50  
                           total_harga = price_per_day * days * quantity
                           print(Fore.GREEN + f"Order placed by {self.username}: {quantity} {nama_barang.capitalize()}(s) for {days} days. Total price: ${total_harga}")
                     found = True
                     break
                  else:
                     raise ValueError(f"Insufficient stock for {nama_barang.capitalize()}")
         if not found:
               raise ValueError(f"Laptop with ID {id_barang} not found")
      except ValueError as e:
         print(Fore.RED + str(e))
      except Exception as e:
         print(Fore.RED + f"An error occurred: {str(e)}")



class LaptopShop:
   def __init__(self):
      self.total_income = 0
      self.order_stack = deque()
      self.order_queue = deque()
      self.menu = []
      self.orders = []
      self.barang = self.fetch_laptops_from_database()
      self.users = self.fetch_users_from_database()
      self.admins = self.fetch_admins_from_database()
      
   def fetch_purchase_history_from_database(self):
      try:
         connection = self.connect_to_database()
         if connection:
               cursor = connection.cursor(dictionary=True)
               cursor.execute("""
                  SELECT pembelian.id_pembelian, pembelian.tanggal_pembelian, pembelian.total_harga, 
                  transaksi.total_barang
                  FROM pembelian
                  INNER JOIN transaksi ON pembelian.id_pembelian = transaksi.total_barang;
               """)
               purchase_history = cursor.fetchall()
               connection.close()
               return purchase_history
         else:
               print("Failed to connect to database")
               return []
      except Exception as e:
         print(Fore.RED + f"An error occurred: {str(e)}")
         return []

   def fetch_laptops_from_database(self):
      try:
         connection = self.connect_to_database()
         if connection:
               cursor = connection.cursor(dictionary=True)
               cursor.execute("SELECT id_barang, nama_barang, harga, stock, spek FROM barang;")
               barang = cursor.fetchall()
               connection.close()
               for laptop in barang:
                  if 'nama_barang' not in laptop:
                     raise ValueError("Missing key 'nama_barang' in laptop data")
               return barang
         else:
               print("Failed to connect to database")
               return []
      except Exception as e:
         print(Fore.RED + f"An error occurred: {str(e)}")
         return []

      
   def fetch_admins_from_database(self):
      try:
         connection = self.connect_to_database()
         if connection:
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM admin;")
            admins_data = cursor.fetchall()
            connection.close()
            return admins_data
         else:
            print("Failed to connect to database")
            return []
      except Exception as e:
         print(Fore.RED + f"An error occurred: {str(e)}")
         return []
      
   def fetch_users_from_database(self):
      try:
         connection = self.connect_to_database()
         if connection:
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM pelanggan;")
            users_data = cursor.fetchall()
            connection.close()
            return users_data
         else:
            print("Failed to connect to database")
            return []
      except Exception as e:
         print(Fore.RED + f"An error occurred: {str(e)}")
         return []

   def authenticate_admin(self, username, password):
      try:
         for admin in self.admins:
            if admin.get('nama_admin') == username and admin.get('password') == password:
               return True
         return False
      except Exception as e:
         print(Fore.RED + f"An error occurred: {str(e)}")
         return False
      
   def authenticate_user(self, username, password):
      try:
         for user in self.users:
            if user.get('nama_pelanggan') == username and user.get('password') == password:
               return True
         return False
      except Exception as e:
         print(Fore.RED + f"An error occurred: {str(e)}")
         return False

   def connect_to_database(self):
      hostname = "462.h.filess.io"
      database = "reytop3_perfectly"
      port = "3306"
      username = "reytop3_perfectly"
      password = "73bac833e2e1437cc2e127b57d2a70b7b4f11308"

      try:
         connection = mysql.connector.connect(host=hostname, database=database, user=username, password=password, port=port)
         if connection.is_connected():
               db_Info = connection.get_server_info()
               print("Connected to MySQL Server version ", db_Info)
               return connection
      except Error as e:
         print("Error while connecting to MySQL", e)
         return None


   def calculate_total_income(self):
      return self.total_income
   
   def add_new_laptop(self, laptop_name, price, stock, spek):
      try:
         connection = self.connect_to_database()
         if connection:
               cursor = connection.cursor()
               cursor.execute("""
                  INSERT INTO barang (nama_barang, harga, stock, spek)
                  VALUES (%s, %s, %s, %s)
               """, (laptop_name, price, stock, spek))

               connection.commit()
               connection.close()
               print(Fore.GREEN + f"Laptop '{laptop_name}' added successfully.")
      except Exception as e:
         print(Fore.RED + f"An error occurred: {str(e)}")

   def update_laptop(self, laptop_id, new_price, new_stock, new_spek):
      try:
         connection = self.connect_to_database()
         if connection:
               cursor = connection.cursor()
               cursor.execute("""
                  UPDATE barang
                  SET harga = %s, stock = %s, spek = %s
                  WHERE id_barang = %s;
               """, (new_price, new_stock, new_spek, laptop_id))
               connection.commit()
               connection.close()
               print(Fore.GREEN + f"Laptop with ID '{laptop_id}' updated successfully.")
      except Exception as e:
         print(Fore.RED + f"An error occurred: {str(e)}")

   def del_laptop(self, laptop_id):
      try:
         connection = self.connect_to_database()
         if connection:
               cursor = connection.cursor()
               cursor.execute("""
                  DELETE FROM barang
                  WHERE id_barang = %s;
               """, (laptop_id,))
               connection.commit()
               connection.close()
               print(Fore.GREEN + f"Laptop with ID '{laptop_id}' deleted successfully.")
      except Exception as e:
         print(Fore.RED + f"An error occurred: {str(e)}")


   def display_pembelian_history(shop):
      try:
         return shop.order_queue
      except Exception as e:
         print(Fore.RED + f"An error occurred: {str(e)}")
         return []

   def display_penyewaan_history(shop):
      try:
         return shop.order_queue
      except Exception as e:
         print(Fore.RED + f"An error occurred: {str(e)}")
         return []

   def display_menu_and_stock(self, order_type="pembelian"):
      try:
         if order_type == "pembelian" or order_type == "penyewaan":
               connection = self.connect_to_database()
               if connection:
                  cursor = connection.cursor(dictionary=True)
                  if order_type == "pembelian":
                     cursor.execute("SELECT id_barang, nama_barang, harga, stock, spek FROM barang;")
                  elif order_type == "penyewaan":
                     cursor.execute("SELECT id_barang, nama_barang, harga, stock, spek FROM barang;")
                  menu = cursor.fetchall()
                  connection.close()
                  return menu
         else:
               raise ValueError("Invalid order type. Please choose 'pembelian' or 'penyewaan'.")
      except Exception as e:
         print(Fore.RED + f"An error occurred: {str(e)}")
         return []

   def update_menu_and_stock(self):
      try:
         return self.barang
      except Exception as e:
         print(Fore.RED + f"An error occurred: {str(e)}")
         return []

   def display_orders(self):
      try:
         return self.order_queue
      except Exception as e:
         print(Fore.RED + f"An error occurred: {str(e)}")
         return []
      

      
   def search_menu(self, keyword):
      try:
         results = []
         for laptop in self.barang:
            for key, value in laptop.items():
                  if keyword.lower() in str(value).lower():
                     results.append(laptop)
                     break  
         return results
      except Exception as e:
         print(Fore.RED + f"An error occurred: {str(e)}")
         return []

   def add_new_admin(self, username, password):
      try:
         if not username.isalpha():
               raise ValueError("Username should only contain letters.")
         
         # Lakukan pengecekan apakah admin dengan username tersebut sudah ada
         for admin in self.admins:
               if admin.get('nama_admin') == username:
                  raise ValueError("Admin with this username already exists.")
         
         # Jika tidak ada admin dengan username yang sama, tambahkan admin baru
         self.admins.append({'nama_admin': username, 'password': password})
         print(Fore.GREEN + "Admin registered successfully!")
      except Exception as e:
         print(Fore.RED + f"An error occurred: {str(e)}")

   def add_new_customer(self, username, password):
      try:
         if not username.isalpha():
               raise ValueError("Username should only contain letters.")
         for user in self.users:
               if user.get('nama_pelanggan') == username:
                  raise ValueError("Customer with this username already exists.")
         self.users.append({'nama_pelanggan': username, 'password': password})
         print(Fore.GREEN + "Customer registered successfully!")
      except Exception as e:
         print(Fore.RED + f"An error occurred: {str(e)}")

   def sort_menu(self, order_type='ascending'):
      try:
         if order_type == '1':
               self.barang = sorted(self.barang, key=lambda x: x['harga'])
         elif order_type == '2':
               self.barang = sorted(self.barang, key=lambda x: x['harga'], reverse=True)
         else:
               raise ValueError("Invalid order type. Please choose 'ascending' or 'descending'.")
      except Exception as e:
         print(Fore.RED + f"An error occurred: {str(e)}")