from prettytable import PrettyTable
from colorama import Fore

def display_menu_and_stock(barang, order_type="pembelian"):
    from prettytable import PrettyTable
    from colorama import Fore

    table = PrettyTable()
    table.field_names = [Fore.BLUE + "id_barang", Fore.BLUE + "nama_barang", Fore.BLUE + "harga", Fore.BLUE + "Stock"]

    for laptop in barang:
        try:
            id_barang = laptop.get('id_barang', 'ID not available')
            name = laptop['nama_barang']
            price = laptop.get('harga', 'Price not available')
            stock = laptop.get('stock', 'Stock not available')

            if order_type == "penyewaan":
                price /= 50

            table.add_row([Fore.BLUE + str(id_barang), Fore.BLUE + name, Fore.BLUE + str(price), Fore.BLUE + str(stock)])
        except KeyError as e:
            print(f"Error: Missing key in laptop data - {e}")

    print(table.get_string().capitalize())

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
        print(Fore.RED + f"An error occurred: {str(e)}")

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
                    table.add_row([id_penyewaan, tanggal_minjam, tanggal_kembali, jaminan, total_harga, total_barang])  # Perubahan urutan kolom sesuai dengan struktur tabel
                print(table)
            else:
                print(Fore.YELLOW + "No penyewaan history found.")
        else:
            print(Fore.RED + "Failed to connect to database")
    except Exception as e:
        print(Fore.RED + f"An error occurred: {str(e)}")





