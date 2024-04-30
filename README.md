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



``` 
from Model.model import  LaptopShop, SingletonLogger
from Controller.controller import customer_actions, admin_actions
from prettytable import PrettyTable 
from colorama import Fore, Style
Fitur dan Fungsionalitas
```


diatas adalah dictionary
model    : berisi definisi kelas untuk model bisnis, seperti LaptopShop yang mungkin mengatur logika terkait penjualan laptop, dan SingletonLogger yang mungkin bertanggung jawab atas logging dalam aplikasi.
Controller    : Berkemungkinan terdapat dua modul di sini, customer_actions dan admin_actions, yang berisi logika terkait dengan tindakan yang dapat dilakukan oleh pelanggan dan administrator sistem, seperti menambahkan produk, mengelola inventaris, memproses pembayaran, dll.





apa saja fitur yang ada di program
*Cara Penggunaan*
cara
bagaimana implementasinya
