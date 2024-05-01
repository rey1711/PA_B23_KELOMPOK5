# reytop
Deskripsi Program

Perusahan kami menyediakan berbagai macam merk laptop dengan harga yang terjangkau,perusahaan kami juga menyediakan metode pembelian dan penyewaan dimana customer dapat menyewa atau membeli barang dari kami.
program ini memiliki dua peran utama yaitu admin dan pelanggan.untuk penjelasan sebagai berikut:


Pelanggan (Customer):
  Pelanggan dapat masuk ke dalam sistem dengan username dan password mereka.
  Setelah masuk, mereka dapat melihat menu lengkap dari laptop yang tersedia untuk pembelian dan penyewaan.
  Pelanggan juga dapat melakukan pencarian laptop berdasarkan kata kunci tertentu.
  Mereka dapat memesan laptop untuk dibeli atau disewa, dengan memilih jumlah yang diinginkan.
  Pelanggan dapat melihat riwayat pesanan mereka.


Admin:
    Admin memiliki hak akses penuh terhadap sistem.Mereka dapat melihat dan mengelola stok laptop yang tersedia.Admin dapat menambahkan laptop baru ke dalam stok perusahaan, serta mengupdate harga dan jumlah       stok dari laptop yang sudah ada.Mereka juga memiliki kemampuan untuk menghapus laptop dari stok jika diperlukan.Admin dapat melihat riwayat pesanan lengkap dari pelanggan.

Program ini memberikan pengalaman pengguna yang ramah dan efisien baik untuk pelanggan maupun admin, dengan antarmuka yang mudah digunakan dan fungsi yang lengkap untuk memenuhi kebutuhan perusahaan            Reytop dalam mengelola bisnis pembelian dan penyewaan laptop mereka.

*Struktur Project*


  
![Screenshot 2024-05-01 143205](https://github.com/PAB23KELOMPOK5/PA_B23_KELOMPOK5/assets/145863352/5947d6cd-2284-4c3c-a07d-2eb8796ace98)


  
![image](https://github.com/PAB23KELOMPOK5/PA_B23_KELOMPOK5/assets/145863352/db40e96f-47ff-4976-afec-51a2195c21fa)

 
![image](https://github.com/PAB23KELOMPOK5/PA_B23_KELOMPOK5/assets/145863352/8b8bdd07-15c1-4a9d-b7e2-417a81bd9699)


![image](https://github.com/PAB23KELOMPOK5/PA_B23_KELOMPOK5/assets/145863352/1f903cfd-0e90-4895-91dd-716fb2fedd25)


![image](https://github.com/PAB23KELOMPOK5/PA_B23_KELOMPOK5/assets/145863352/2413f2c0-13d0-423a-bf81-5564bacb2356)




Struktur MVC
![image](https://github.com/PAB23KELOMPOK5/PA_B23_KELOMPOK5/assets/143304299/e930ae47-1de6-4b87-b337-af123449a9bd)


  MVC (Model-View-Controller) adalah  pola desain arsitektur perangkat lunak yang membagi aplikasi menjadi tiga komponen utama: model , view, dan controller. Setiap komponen memiliki tanggung jawabnya sendiri untuk memproses informasi dan mengelola interaksi antara pengguna dan aplikasi. Mari kita jelaskan secara singkat setiap bagian dari MVC.
MVC 


  Model: Model mewakili struktur data dan logika bisnis suatu aplikasi.
   Ini adalah bagian yang bertanggung jawab untuk mengelola data aplikasi dan berinteraksi dengan database atau sumber data lainnya.
  Model tidak berhubungan langsung dengan tampilan atau pengguna;Itu hanya  pemrosesan data.

  
  ![image](https://github.com/rey1711/reytop/assets/145863352/93de6aeb-eb90-4623-a7ce-81c3b43195fd)



  View
      View adalah bagian yang menangani tampilan atau penyajian data kepada pengguna.
 Ini menjelaskan bagaimana informasi disajikan kepada pengguna, seperti halaman web, antarmuka pengguna grafis (GUI), atau tampilan teks sederhana.
 View tidak memiliki logika bisnis.Tugasnya hanya  menampilkan informasi yang diberikan oleh model.

 
![image](https://github.com/rey1711/reytop/assets/145863352/6382f509-4b03-4262-8812-9de3710ec363)


  Controller
      Controller bertindak sebagai perantara antara model dan View.
 Menerima masukan dari pengguna tentang View mengambil atau memperbarui data dan memilih tampilan yang sesuai untuk ditampilkan kepada pengguna.
 Ini adalah bagian yang mengatur alur logika aplikasi dan menghubungkan model ke view.

 
 ![image](https://github.com/rey1711/reytop/assets/145863352/5369c30a-4a82-45a0-a1bd-4690d693d59c)



*Fitur dan Fungsionalitas*

CONTROLLER

``` 
from colorama import Fore
from Model.model import Admin, Customer
from VIew.view import display_menu_and_stock, display_pembelian_history, display_penyewaan_history
import pwinput
```


diatas adalah dictionary
colorama     : untuk memberikan warna pada codingan 
Model        : untuk mewakili penggunaan sistem admin dan pelanggan 
VIev.view    : untuk menampilkan menu yang ada di prpgram
pwinput      : untuk menyamarkan password yang  dimasukkan agar menjadi * 


```
def customer_actions(shop): 
    while True:
        try:
            customer_username = input("Enter your username: ")
            customer_password = pwinput.pwinput(prompt="Enter your password: ")
            customer = Customer(customer_username, customer_password, shop)
            while True:
                print_menu_customer()
                customer_choice = input("Enter your choice: ")
                try:
                    if customer_choice == '1':
                        display_menu_and_stock(shop.display_menu_and_stock())
                    elif customer_choice == '2':
                        try:
                            menu = shop.display_menu_and_stock()
                            display_menu_and_stock(menu)
                            sorting_order = input("Enter sorting order: 'asc' for ascending or 'desc' for descending: ")
                            if sorting_order.lower() == 'asc' or sorting_order.lower() == 'desc':
                                shop.sort_menu(sorting_order)
                                menu = shop.display_menu_and_stock()  
                                display_menu_and_stock(menu)
                            else:
                                raise ValueError("Invalid sorting order. Please enter 'asc' for ascending or 'desc' for descending.")
                        except ValueError as e:
                            print(Fore.RED + f"Invalid Input data.")
                    elif customer_choice == '3':
                        keyword = input("Enter the keyword to search: ")
                        display_menu_and_stock(shop.search_menu(keyword))
                    elif customer_choice == '4':
                        display_menu_and_stock(shop.display_menu_and_stock())
                        order_type = input("Enter order type (pembelian or penyewaan): ")
                        id_barang = input("Enter the ID of the laptop that you want to order: ")
                        quantity = int(input("Enter the quantity: "))
                        if order_type not in ["pembelian", "penyewaan"]:
                            raise ValueError("Invalid order type. Please choose 'pembelian' or 'penyewaan'.")
                        if order_type == "penyewaan":
                            display_menu_and_stock(shop.display_menu_and_stock("penyewaan"), order_type="penyewaan")
                            days = int(input("Enter the number of days for rental: "))
                            customer.place_order(order_type, id_barang, quantity, days)
                        else:
                            customer.place_order(order_type, id_barang, quantity)
                    elif customer_choice == '0':
                        return
                    else:
                        print(Fore.RED + "Invalid choice. Please try again.")
                except KeyboardInterrupt:
                    print(Fore.RED + "Program interrupted by the user.")
                except Exception as e:
                    print(Fore.RED + f"Invalid Input data.")
        except KeyboardInterrupt:
            print(Fore.RED + "Program interrupted by the user.")
        except Exception as e:
            print(Fore.RED + f"Invalid Input data.")
```
Program di atas untuk memasukkan nama dan password dari  customer,menampilkan menu dan menampilkan stock barang yang ada secara urut ascending atau descending


```
def admin_actions(shop):
    while True:
        try:
            admin_username = input(Fore.GREEN + "Enter your username: ")
            admin_password = pwinput.pwinput(prompt="Enter your password: ")
            admin = Admin(admin_username, admin_password, shop)
            while True:
                print_menu_admin()
                admin_choice = input("Enter your choice: ")
                try:
                    if admin_choice == '1':
                        display_menu_and_stock(shop.display_menu_and_stock())
                    elif admin_choice == '2':
                        laptop_name = input("Enter new laptop name: ")
                        price = int(input("Enter price: "))
                        stock = int(input("Enter stock: "))
                        spek = input("Enter laptop spec : ")
                        try:
                            shop.add_new_laptop(laptop_name, price, stock, spek)
                        except ValueError as e:
                            print(Fore.RED + f"Invalid Input data.")
                    elif admin_choice == '3':
                        try:
                            display_menu_and_stock(shop.display_menu_and_stock())
                            laptop_name = input("Enter the ID of the laptop to update: ")
                            new_price = int(input("Enter the new price: "))
                            new_stock = int(input("Enter the new stock: "))
                            new_spek = (input("Enter the new spec: "))
                            try:
                                shop.update_laptop(laptop_name, new_price, new_stock, new_spek)
                            except ValueError as e:
                                print(Fore.RED + f"Invalid Input data.")
                        except ValueError as e:
                            print(Fore.RED + f"Invalid Input data.")
                    elif admin_choice == '4':
                        display_menu_and_stock(shop.display_menu_and_stock())
                        deleteLaptop = input("Enter the laptop ID to delete: ")
                        try:
                            shop.del_laptop(deleteLaptop)
                        except ValueError as e:
                            print(Fore.RED + f"Invalid Input data.")
                    elif admin_choice == '5':
                        print("1. Display Pembelian History")
                        print("2. Display Penyewaan History")
                        history_choice = input("Enter your choice: ")
                        if history_choice == '1':
                            display_pembelian_history(shop)
                        elif history_choice == '2':
                            display_penyewaan_history(shop)
                        else:
                            print(Fore.RED + "Invalid choice. Please try again.")

                    elif admin_choice == '0':
                        return
                    else:
                        print(Fore.RED + "Invalid choice. Please try again.")
                except KeyboardInterrupt:
                        print(Fore.RED + "Program interrupted by the user.")
                except Exception as e:
                    print(Fore.RED + f"Invalid Input data.")
        except KeyboardInterrupt:
            print(Fore.RED + "Program interrupted by the user.")
        except Exception as e:
            print(Fore.RED + f"Invalid Input data.")
```

di atas adalaf def untuk Fungsi admin_actions memberikan pilihan bagi admin untuk mengelola sistem toko dengan menambahkan, memperbarui, dan menghapus informasi laptop serta melihat riwayat pembelian atau penyewaan. Admin diminta untuk memasukkan nama pengguna dan kata sandi dengan bantuan pwinput, sementara pesan username ditampilkan dalam warna hijau menggunakan colorama. Program ini dirancang untuk menangani berbagai kesalahan yang mungkin terjadi dan terus berjalan dalam loop utama agar admin dapat terus melakukan aksi tanpa perlu memulai ulang program.



```
def print_menu_customer():
    print(Fore.BLUE + "Customer Options")
    print(Fore.BLUE + "1. Display Menu and Stock")
    print(Fore.BLUE + "2. Sort Menu by Price")
    print(Fore.BLUE + "3. Search Menu ")
    print(Fore.BLUE + "4. Place Order")
    print(Fore.BLUE + "0. Exit")


def print_menu_admin():
    print(Fore.BLUE + "Admin Options")
    print(Fore.BLUE + "1. Display Menu and Stock")
    print(Fore.BLUE + "2. Add New Laptop")
    print(Fore.BLUE + "3. Update Laptop")
    print(Fore.BLUE + "4. Delete Laptop")
    print(Fore.BLUE + "5. Display Orders History")
    print(Fore.BLUE + "0. Exit")
```
fungsi di atas untuk  menampilkan opsi yang tersedia untuk customer dan pelanggan

 
MODEL

```
from collections import deque
from colorama import Fore
import mysql.connector
from mysql.connector import Error
```

Import deque : Untuk mendapatkan akses data untuk deque seperti sebuah daftar atau lebih fleksibel agar bisa menambahkan atau menghapus elemen dengan lebih mudah.
Import fore  : memberikan warna pada terminal
Import mysql connector :   buat menghubungkan program ke database
Mysql connector import error : Untuk menampilkan masalah yang ada ketika ada masalah muncul saat menghubungkat program dengan database


```
class SingletonLogger:
   _instance = None  
   _connection = None
```
Untuk memastikan hanya satu logger yang masuk ke program


```
   def __new__(cls):
      if cls._instance is None:
         cls._instance = super().__new__(cls)
         cls._instance.connect_to_database()
      return cls._instance
```
Untuk Menghubungkan program jika ada database baru yang ingin di hubungkan dengan program



```
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
               print("Welcome to ReyTop ✨")
      except Error as e:
         print("Error while connecting to MySQL", e)
```

Untuk menampilkan detail koneksinya dan membuat koneksinya



```
def log(self, message):
      print(message)

   def close_connection(self):
      if self._connection:
         self._connection.close()
         print("Please wait, Going to Connecting Database")

logger1 = SingletonLogger()
logger2 = SingletonLogger()

if logger1 is logger2:
   print("Instance Checking, Success")

logger1.close_connection()

class User:
   def __init__(self, username, password):
      self.username = username
      self.password = password

class Admin(User):
   def __init__(self, username, password, shop):
      if shop.authenticate_admin(username, password)
         super().__init__(username, password)
         self.shop = shop  
      else:
         raise ValueError("Invalid username or password."):

class Customer(User):
   def __init__(self, username, password, shop):
      if shop.authenticate_user(username, password):
         super().__init__(username, password)
         self.shop = shop
      else:
         raise ValueError("Invalid username or password.")
```
Log : Untuk untuk mencetak pesan log ke konsol
close_connection : untuk menutup koneksi ke database
class user,admin dan customer : untuk mendefenisikan tiga kelas yaitu user,admin,dan customer.


```
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
                           print(Fore.RED + f"Failed to insert transaction data.")
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
            print(Fore.RED + f"Invalid Input data.")
      except Exception as e:
            print(Fore.RED + f"Invalid Input data.")
```

untuk menempatkan  pesanan untuk pembelian maupun penyewaan
pada fungsi def di atas untuk mengecek apakah stok barang ada atau tidak
untuk mencetak transaksi database,informasi pesanan dan penanganan kesalahan.


```
class LaptopShop:
   def __init__(self):
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
         print(Fore.RED + f"Invalid Input data.")
         return []
```

Class Laptop untuk manajemen operasi toko
order stack untuk menyimpan pesanan
order queue untuk menyimpan pesanan berikutnya
def fetch_purchase_history_from_database untuk mengambil riwayat pembelian dari database


```
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
         print(Fore.RED + f"Invalid Input data.")
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
         print(Fore.RED + f"Invalid Input data.")
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
         print(Fore.RED + f"Invalid Input data.")
         return []
```
def fetch_laptops_from_database : Melakukan koneksi ke database lalu mengeksekusi query sql
def fetch_admins_from_database  : Melakukan koneksi ke database lalu mengeksekusi query sql untuk tabel admin
def fetch_users_from_database  : Melakukan koneksi ke database lalu mengeksekusi query sql untuk tabel  user


```
   def authenticate_admin(self, username, password):
      try:
         connection = self.connect_to_database()
         if connection:
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM admin WHERE nama_admin = %s AND password = %s", (username, password))
            admin = cursor.fetchone()
            connection.close()
            if admin:
               return True
            else:
               return False
         else:
            print("Failed to connect to database")
            return False
      except Exception as e:
         print(Fore.RED + f"Invalid Input data.")
         return False

   def authenticate_user(self, username, password):
      try:
         connection = self.connect_to_database()
         if connection:
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM pelanggan WHERE nama_pelanggan = %s AND password = %s", (username, password))
            user = cursor.fetchone()
            connection.close()
            if user:
               return True
            else:
               return False
         else:
            print("Failed to connect to database")
            return False
      except Exception as e:
         print(Fore.RED + f"Invalid Input data.")
         return False
```
def authenticate_admin :  untuk memverifikasi admin yang masuk mencocokkan dengan data admin yang ada seperti password dan username
def authenticate_user : untuk memverifikasi user yang masuk dnegan mencocokkan username dan paswwrodnya


```
def connect_to_database(self):
      hostname = "462.h.filess.io"
      database = "reytop3_perfectly"
      port = "3306"
      username = "reytop3_perfectly"
      password = "73bac833e2e1437cc2e127b57d2a70b7b4f11308"

      try:
         connection = mysql.connector.connect(host=hostname, database=database, user=username, password=password, port=port)
         if connection.is_connected():
               print("Connecting to Database, Thanks for the wait❤️")
               return connection
      except Error as e:
         print("Error while connecting to MySQL", e)
         return None
```

Untuk membuat koneksi antara program ke database
```
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
               self.update_menu_and_stock()
               print(Fore.GREEN + f"Laptop '{laptop_name}' added successfully.")
      except Exception as e:
         print(Fore.RED + f"Invalid Input data.")

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
               self.update_menu_and_stock()
               print(Fore.GREEN + f"Laptop with ID '{laptop_id}' updated successfully.")
      except Exception as e:
         print(Fore.RED + f"Invalid Input data.")

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
               self.update_menu_and_stock()
               print(Fore.GREEN + f"Laptop with ID '{laptop_id}' deleted successfully.")
      except Exception as e:
         print(Fore.RED + f"Invalid Input data.")

   def display_pembelian_history(shop):
      try:
         return shop.order_queue
      except Exception as e:
         print(Fore.RED + f"Invalid Input data.")
         return []

   def display_penyewaan_history(shop):
      try:
         return shop.order_queue
      except Exception as e:
         print(Fore.RED + f"Invalid Input data.")
         return []

   def display_menu_and_stock(self, order_type="pembelian", sorting_order=None):
      try:
         if order_type == "pembelian" or order_type == "penyewaan":
               connection = self.connect_to_database()
               if connection:
                  cursor = connection.cursor(dictionary=True)
                  cursor.execute("SELECT id_barang, nama_barang, harga, stock, spek FROM barang;")
                  menu = cursor.fetchall()
                  connection.close()
                  if sorting_order:
                     self.sort_menu(sorting_order)
                  if order_type == "pembelian":
                     return self.barang
                  elif order_type == "penyewaan":
                     rented_menu = []
                     for laptop in self.barang:
                           laptop_copy = laptop.copy()
                           rented_menu.append(laptop_copy)
                     return rented_menu
         else:
               raise ValueError("Invalid order type. Please choose 'pembelian' or 'penyewaan'.")
      except Exception as e:
         print(Fore.RED + f"Invalid Input data.")
         return []
```

program di atas untuk CRUD(Create,Read,Update,Delete) dan juga untuk menambahkan barang baru
def add_new_laptop : Untuk menambahkan barang baru
def update_laptop : Untuk menambahkan barang 
def del_laptop : Untuk menghapus barang
def display_pembelian_history : Untuk menampilkan riwayat pembelian barang
def display_penyewaan_history : Untuk menampilkan riwayat penyewaan barang
def display_menu_and_stock( : Untuk menampilkan menu dan stok barang 

```
def sort_menu(self, sorting_order='asc'):
      try:
         if sorting_order.lower() == 'asc':
               self.barang = sorted(self.barang, key=lambda x: x['harga'])
         elif sorting_order.lower() == 'desc':
               self.barang = sorted(self.barang, key=lambda x: x['harga'], reverse=True)
         else:
               raise ValueError("Invalid sorting order. Please choose 'asc' for ascending or 'desc' for descending.")
      except Exception as e:
         print(Fore.RED + f"Invalid Input data.")

   def update_menu_and_stock(self):
      try:
         return self.barang
      except Exception as e:
         print(Fore.RED + f"Invalid Input data.")
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
         print(Fore.RED + f"Invalid Input data.")
         return []

   def update_menu_and_stock(self):
      try:
         self.barang = self.fetch_laptops_from_database()
      except Exception as e:
         print(Fore.RED + f"Invalid Input data.")
```
def sort_menu : Untuk mengurutkan barang secara ascending atau descending
def update_menu_and_stock : Untuk mengembalikan menu dan stok laptop yang telah di perbarui
def search_menu : Untuk mencari barang dengan kata kunci tertentu
def update_menu_and_stock : Untuk memperbarui menu dan stok laptop dari database dengan memanggil metode fetch_laptops_from_database.


```
def add_new_admin(self, username, password, jobdesk):
      try:
            if not username.isalpha():
               raise ValueError("Username should only contain letters.")
            connection = self.connect_to_database()
            if connection:
               cursor = connection.cursor()
               cursor.execute("SELECT * FROM admin WHERE nama_admin = %s", (username,))
               existing_admin = cursor.fetchone()
               if existing_admin:
                  raise ValueError("Admin with this username already exists.")
               else:
                  cursor.execute("INSERT INTO admin (nama_admin, password, jobdesk) VALUES (%s, %s, %s)", (username, password, jobdesk))
                  connection.commit()
                  connection.close()
                  print(Fore.GREEN + "Admin registered successfully!")
      except Exception as e:
            print(Fore.RED + f"Invalid Input data.")

   def add_new_customer(self, username, password, email, nohp):
      try:
            if not username.isalpha():
               raise ValueError("Username should only contain letters.")
            connection = self.connect_to_database()
            if connection:
               cursor = connection.cursor()
               cursor.execute("SELECT * FROM pelanggan WHERE nama_pelanggan = %s", (username,))
               existing_customer = cursor.fetchone()
               if existing_customer:
                  raise ValueError("Customer with this username already exists.")
               else:
                  cursor.execute("INSERT INTO pelanggan (nama_pelanggan, password, email, nohp) VALUES (%s, %s, %s, %s)", (username, password, email, nohp))
                  connection.commit()
                  connection.close()
                  print(Fore.GREEN + "Customer registered successfully!")
      except Exception as e:
            print(Fore.RED + f"Invalid Input data.")
```  
def add_new_admin : Untuk menambahkan admin baru
def add_new_customer : Untuk menambahkan customer baru
Keduanya menggunakan try except untuk menangani kesalahan saat proses penambahan data ke dalam database


VIEW
```
from prettytable import PrettyTable
from colorama import Fore

```  
Import PrettyTable : untuk  membuat tabel agar lebih rapi
Import fore : untuk memberikan warna pada teks


```
def display_menu_and_stock(menu, order_type="pembelian", limit=20, start_index=0):
    try:
        if menu:
            print("Menu and Stock:")
            table = PrettyTable()
            table.field_names = ["ID", "Nama Barang", "Harga", "Stock", "Spek"]
            if start_index == 0:
                items_to_display = menu[:limit]
            else:
                items_to_display = menu[start_index:start_index+limit]
            for item in items_to_display:
                if order_type == "penyewaan":
                    harga = int(item['harga']) // 50
                else:
                    harga = item['harga']
                table.add_row([item['id_barang'], item['nama_barang'], harga, item['stock'], item['spek']])
            print(table)
            if len(menu) > limit + start_index:
                choice = input("Input '0' to view more items or press any other key to continue: ")
                if choice == '0':
                    display_menu_and_stock(menu, order_type, limit, start_index+limit)
        else:
            print(Fore.YELLOW + "No items found.")
    except Exception as e:
        print(Fore.RED + f"Invalid Input data.")
```
def display_menu_and_stock : Untuk Menampilkan menu dan stok barang dalam bentuk  tabel 


```
def display_pembelian_history(shop):
    try:
        connection = shop.connect_to_database()
        if connection:
            cursor = connection.cursor(dictionary=True)
            cursor.execute("""
                SELECT pembelian.id_pembelian, pembelian.tanggal_pembelian, pembelian.total_harga, 
                SUM(transaksi.total_barang) AS total_barang
                FROM pembelian
                INNER JOIN transaksi ON pembelian.id_pembelian = transaksi.id_transaksi
                GROUP BY pembelian.id_pembelian;
            """)
            pembelian_history = cursor.fetchall()
            connection.close()
            if pembelian_history:
                table = PrettyTable()
                table.field_names = ["id_pembelian", "tanggal_pembelian", "total_harga", "total_barang"]
                for order in pembelian_history:
                    id_pembelian = order["id_pembelian"]
                    tanggal_pembelian = order["tanggal_pembelian"]
                    total_harga = order["total_harga"]
                    total_barang = int(order["total_barang"])
                    table.add_row([id_pembelian, tanggal_pembelian, total_harga, total_barang])
                print(table)
            else:
                print(Fore.YELLOW + "No pembelian history found.")
        else:
            print(Fore.RED + "Failed to connect to database")
    except Exception as e:
        print(Fore.RED + f"Invalid Input data.")
```
def display_pembelian_history : Menampilkan Riwayat pembeliann dari database secara terstruktur

```
def display_penyewaan_history(shop):
    try:
        connection = shop.connect_to_database()
        if connection:
            cursor = connection.cursor(dictionary=True)
            cursor.execute("""
                SELECT penyewaan.id_penyewaan, penyewaan.tanggal_minjam, penyewaan.jaminan, penyewaan.tanggal_kembali, penyewaan.total_harga, 
                transaksi.total_barang AS total_barang
                FROM penyewaan
                INNER JOIN transaksi ON penyewaan.id_transaksi = transaksi.id_transaksi
            """)
            penyewaan_history = cursor.fetchall()
            connection.close()
            if penyewaan_history:
                table = PrettyTable()
                table.field_names = ["id_penyewaan", "tanggal_minjam", "tanggal_kembali", "jaminan", "total_harga", "total_barang"]
                for order in penyewaan_history:
                    id_penyewaan = order["id_penyewaan"]
                    tanggal_minjam = order["tanggal_minjam"]
                    jaminan = order["jaminan"]
                    tanggal_kembali = (order["tanggal_kembali"])
                    total_harga = order["total_harga"]
                    total_barang = int(order["total_barang"])
                    table.add_row([id_penyewaan, tanggal_minjam, tanggal_kembali, jaminan, total_harga, total_barang])  
                print(table)
            else:
                print(Fore.YELLOW + "No penyewaan history found.")
        else:
            print(Fore.RED + "Failed to connect to database")
    except Exception as e:
        print(Fore.RED + f"Invalid Input data.")
```

def display_penyewaan_history : Menampilkan Riwayat Penyewaan dari database secara terstruktur

MAIN
```
from Model.model import  LaptopShop, SingletonLogger
from Controller.controller import customer_actions, admin_actions
from prettytable import PrettyTable 
from colorama import Fore, Style
```
from Model.model import  LaptopShop, SingletonLogger : Untuk mewakili toko laptop dalam aplikasi
from Controller.controller import customer_actions, admin_actions : Mengatur tindakan pengguna dalam aplikasi
from prettytable import PrettyTable : Menampilkan tabel
from colorama import Fore, Style : memberikan warna pada teks dalam konsol

```
def mainsingleton():
    SingletonLogger1 =SingletonLogger.get_instance()
    SingletonLogger2 =SingletonLogger.get_instance()
    
    if SingletonLogger1 is SingletonLogger2:
        print("Instance Checking for Singleton")
        
    SingletonLogger2.log("this is logged using a singleton logging system")
```
Def mainsingleton : untuk menggunakan pola desain untuk logger

```
def main():
    shop = LaptopShop()
    try:
        while True:
            print_menu_main()
            choice = input(Fore.BLUE + "Enter your choice: ").lower() 
            if choice == '1':
                login_menu(shop)
            elif choice == '2':
                register_menu(shop)
            elif choice == '3':
                break
            else:
                print(Fore.RED + "Invalid choice. Please choose again.")

    except KeyboardInterrupt:
        print(Fore.RED + "Program interrupted by the user.")
        main()

```
def main : Untuk menjalankan aplikasi toko laptop

```
def print_menu_main():
    table = PrettyTable()
    table.field_names = ["Number", "Option"]
    table.add_row(["1.", "Login"])
    table.add_row(["2.", "Register"])
    table.add_row(["3.", "Exit"])

    print(Fore.YELLOW + "Welcome to Perusahaan Reytop! 💻")
    print(table)
    print(Style.RESET_ALL) 
```
def print_menu_main : Untuk mencetak menu utama ke konsol

```
def login_menu(shop):
    print(Fore.YELLOW + "Login Menu")
    role = input("Enter your role (Admin/Customer): ").capitalize()

    if role == 'Admin':
        try:
            admin_actions(shop)
        except ValueError as e:
            print(Fore.RED + str(e))
    elif role == 'Customer':
        try:
            customer_actions(shop)
        except ValueError as e:
            print(Fore.RED + str(e))
    else:
        print(Fore.RED + "Invalid role. Please choose 'Admin' or 'Customer'.")

```
def login_menu : untuk menampilkan menu login (sebagai admin/user)

```
def register_menu(shop):
    print(Fore.YELLOW + "Register Menu")
    role = input("Enter your role (Admin/Customer): ").capitalize()
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if role == 'Admin':
        jobdesk = input("Enter your jobdesk: ")
        try:
            shop.add_new_admin(username, password, jobdesk)
        except ValueError as e:
            print(Fore.RED + str(e))
    elif role == 'Customer':
        email = input("Enter your email: ")
        nohp = input("Enter your phone number: ")
        try:
            shop.add_new_customer(username, password, email, nohp)
        except ValueError as e:
            print(Fore.RED + str(e))
    else:
        print(Fore.RED + "Invalid role. Please choose 'Admin' or 'Customer'.")


if __name__ == "__main__":
    main()

```
Def register_menu : untuk menampilkan menu pendaftaran agar pengguna bisa mendaftar sebagai admin atau customer.


*Cara Penggunaan*
![image](https://github.com/PAB23KELOMPOK5/PA_B23_KELOMPOK5/assets/145863352/288362d7-56f1-4318-9fcb-7166ca689a52)

pilih menu yang di inginkan 


jika memilih menu Login akan muncul seperti di bawah ini 
![image](https://github.com/PAB23KELOMPOK5/PA_B23_KELOMPOK5/assets/145863352/10cf2f98-d9d5-4d54-b324-fa794fbf3e11)

pilih  rolenya dan masukkan username dan password anda jika ingin kembali ke menu utama ketik X
setelah itu pilih pilih opsi yang tersedia

![image](https://github.com/PAB23KELOMPOK5/PA_B23_KELOMPOK5/assets/145863352/bc6feaa2-1122-4d67-bc76-e1d99c1053e3)


Jika anda memilih opsi 1 maka akan menampilkan nama barang yang ada beserta harga,stok dan spek barang jika ingin melihat semua daftar barang ketik 0,jika ingin langsung tekan enter.


![image](https://github.com/PAB23KELOMPOK5/PA_B23_KELOMPOK5/assets/145863352/9999cca3-f8c0-4875-b979-97831865e9b1)


![image](https://github.com/PAB23KELOMPOK5/PA_B23_KELOMPOK5/assets/145863352/bc78bac0-72ce-4c9d-97c9-7aff99617911)


Jika ingin menambahkan barang ke dalam database pilih opsi 2 lalu masukkan nama.harga.stok dan spec laptop yang ingin di tambahkan ke database.
![image](https://github.com/PAB23KELOMPOK5/PA_B23_KELOMPOK5/assets/145863352/3ef7cd82-3367-4d1a-aed7-7934c7644a82)



jika ingin update laptop pilih opsi 3 lalu masukkan id laptop,harga,stok dan spec laptop yang ingin di tambahkan ke database, laptop yang di update akan masuk ke dalam daftar barang.

![image](https://github.com/PAB23KELOMPOK5/PA_B23_KELOMPOK5/assets/145863352/0d09d33e-dd13-4809-8749-b8aaa1c731dd)


![image](https://github.com/PAB23KELOMPOK5/PA_B23_KELOMPOK5/assets/145863352/3caf4bc3-b62a-4d93-bf36-537365c9292e)


jika ingin menghapus laptop dari database pilih opsi 4, lalu masukkan id laptop yang ingin di hapus dari database, laptop yang dihapus hilang dari tabel.


![image](https://github.com/PAB23KELOMPOK5/PA_B23_KELOMPOK5/assets/145863352/67fa476a-3abb-41dc-9d6c-381a53db784c)


![image](https://github.com/PAB23KELOMPOK5/PA_B23_KELOMPOK5/assets/145863352/c475e8e9-9145-4669-84d9-9918bda8333e)


![image](https://github.com/PAB23KELOMPOK5/PA_B23_KELOMPOK5/assets/145863352/095e5fed-6e61-4213-bdea-d2597d72c9ca)





jika ingin melihat riwayat pesanan pilih opsi 5, jika ingin melihat riwayat pembelian ketik 1

![image](https://github.com/PAB23KELOMPOK5/PA_B23_KELOMPOK5/assets/145863352/cdbd190f-322d-4a4a-a578-e18e59d13ec4)

Jika ingin melihat riwayat penyewaan ketik 2

![image](https://github.com/PAB23KELOMPOK5/PA_B23_KELOMPOK5/assets/145863352/cee7b9b0-b414-4e49-bb6e-a1c4ca37af92)


jika ingin keluar pilih opsi 0
![image](https://github.com/PAB23KELOMPOK5/PA_B23_KELOMPOK5/assets/145863352/dd508a41-c0e8-4ebe-b434-e1a6e38b19fa)


Jika ingin masuk sebagai Customer pilih login lalu ketik Customer,setelah itu masukkan username dan password anda, Ketik X jika ingin kembali,jika berhasil tampilannya akan mejadi seperti di bawah ini 
![image](https://github.com/PAB23KELOMPOK5/PA_B23_KELOMPOK5/assets/145863352/bc8a15e9-e8a1-4066-b4e4-b991d5c7afd0)


pilih opsi 1 jika ingin melihat daftar barang dan stok yang tersedia, ketik 0 jika ingin melihat semua daftar barang 

![image](https://github.com/PAB23KELOMPOK5/PA_B23_KELOMPOK5/assets/145863352/0731e88e-a621-45e2-b5c3-231d49b12f70)


![image](https://github.com/PAB23KELOMPOK5/PA_B23_KELOMPOK5/assets/145863352/9dce5374-24d9-46a5-bf68-e046945ff24d)

Pilih opsi 2 untuk mengurutkan barang
![image](https://github.com/PAB23KELOMPOK5/PA_B23_KELOMPOK5/assets/145863352/27159a26-abce-4775-8cb7-f4780cee60c6)

ketik asc jika ingin mengurutkan secara ascending

![image](https://github.com/PAB23KELOMPOK5/PA_B23_KELOMPOK5/assets/145863352/c627734b-0ac2-4a43-942b-552489cf01e8)

![image](https://github.com/PAB23KELOMPOK5/PA_B23_KELOMPOK5/assets/145863352/8530e1b2-adf0-4611-a0db-d939b1b20019)


ketik desc untuk mengurutkan secara descending

![image](https://github.com/PAB23KELOMPOK5/PA_B23_KELOMPOK5/assets/145863352/f3361e7d-dbec-40cb-9145-e592ca266692)


![image](https://github.com/PAB23KELOMPOK5/PA_B23_KELOMPOK5/assets/145863352/433fada6-292e-4d7f-98b4-5429a6c876e7)



Jika ingin mencari barang dalam toko pili opsi 3 lalu masukkan kategori laptop yang ingin di cari spserti nama,spec,harga,atau stok

![image](https://github.com/PAB23KELOMPOK5/PA_B23_KELOMPOK5/assets/145863352/b669d612-a5fd-4645-9b0c-fade231beb0e)


![image](https://github.com/PAB23KELOMPOK5/PA_B23_KELOMPOK5/assets/145863352/49be3742-186b-4155-be55-df8683f9e7c7)



Untuk melakukan pesanan pilih opsi 4
![image](https://github.com/PAB23KELOMPOK5/PA_B23_KELOMPOK5/assets/145863352/f50639ed-74f8-498d-8e26-cc9c5ef3821d)

Jika ingin melakukan pembelian ketik pembelian, lalu masukkan id laptop dan jumlah barang yang akan di beli

![image](https://github.com/PAB23KELOMPOK5/PA_B23_KELOMPOK5/assets/145863352/6fcfa6d6-5408-41e5-a190-a0e7ecf0d4ba)


Jika ingin melakukan penyewaan ketik penyewaan, lalu masukkan id barang yang akan di sewa dan jumlah barangnya, setelah itu masukkan berapa lama barang akan di sewa beserta jaminannya, setelah itu program akan menampilkan barang yang di order,waktu sewa dan total harganya.


![image](https://github.com/PAB23KELOMPOK5/PA_B23_KELOMPOK5/assets/145863352/18a2971a-a323-451c-be95-6fe7d2a27ba2)


Jika ingin mendaftar pilih menu register, lalu  pilih role, jika memilih admin masukkan username,password, dan jobdesk untuk regist.


![image](https://github.com/PAB23KELOMPOK5/PA_B23_KELOMPOK5/assets/145863352/dbb2daa8-1b03-41ca-806a-0dd6247bddf5)


Jika ingin mendaftarc pilih menu register, lalu pilih role, jika rolenya Customer masukkan username,password,email dan nomor hp.


![image](https://github.com/PAB23KELOMPOK5/PA_B23_KELOMPOK5/assets/145863352/9037188f-517c-4310-bdc9-53a4168ee6ca)



Jika ingin keluar dari program pilih menu exit
![image](https://github.com/PAB23KELOMPOK5/PA_B23_KELOMPOK5/assets/145863352/c2cdb1be-3483-4200-b5b1-bd6a2efb2316)










