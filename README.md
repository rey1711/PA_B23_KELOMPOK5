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


  
![Screenshot 2024-04-30 124346](https://github.com/PAB23KELOMPOK5/PA_B23_KELOMPOK5/assets/145863352/26bf2b07-24be-437c-9856-dce17296dea3)

  
![Screenshot 2024-04-30 130515](https://github.com/PAB23KELOMPOK5/PA_B23_KELOMPOK5/assets/145863352/a0bb19dc-76f5-4dfe-b864-b2ad68eaf414)

 
![Screenshot 2024-04-30 130533](https://github.com/PAB23KELOMPOK5/PA_B23_KELOMPOK5/assets/145863352/a62e3d5f-9d3c-4ccc-81cf-c2c895c255cf)


![Screenshot 2024-04-30 130547](https://github.com/PAB23KELOMPOK5/PA_B23_KELOMPOK5/assets/145863352/fb333b97-2881-43d4-b723-8011c2faa5e6)


![Screenshot 2024-04-30 130601](https://github.com/PAB23KELOMPOK5/PA_B23_KELOMPOK5/assets/145863352/43418805-2ebc-49b9-81d1-ef44ffef2ceb)



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

Controller

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


View




apa saja fitur yang ada di program
*Cara Penggunaan*
cara
bagaimana implementasinya
