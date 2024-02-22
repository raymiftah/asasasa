product = {
    "Beras": 18000,
     "Kopi": 12500,
     "Telur": 35000,
     "Tepung": 18000,
     "Garam": 9000,
}

def belanja():
    print*("Selamat datang, selamat berbelanja")
    print("Berikut adalah daftar barang yang tersedia")
    for barang, harga in product.items():
        print(f"{barang}: Rp{harga} per kg")

    total_belanja = 0
    while True:
         barang_dipilih = input("\nMasukkan nama barang yang ingin anda beli (atau 'selesai' untuk selesai)")
         if barang_dipilih.lower () == 'selesai':
             break
         if barang_dipilih not in product:
            print('Maaf, Barang tidak tersedia')
            continue
        jumlah = float(input(f"Berapa kg {barang_dipilih} yang anda inginkan"))
        total_belanja += product[barang_dipilih] * jumlah
    print(f"total belanja anda adalah: Rp{total_belanja}")

belanja()  
           
