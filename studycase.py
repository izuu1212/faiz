# Fungsi untuk menghitung penjualan setelah pemasaran digital
def penjualan_digital(penjualan_sebelum, persentase_peningkatan):
    penjualan_setelah = penjualan_sebelum * (1 + persentase_peningkatan)
    return penjualan_setelah

# Input penjualan saat ini
penjualan_sebelum = float(input("Masukkan jumlah penjualan saat ini: "))

# Input persentase peningkatan penjualan dengan pemasaran digital
persentase_peningkatan = float(input("Masukkan persentase peningkatan penjualan dengan pemasaran digital (dalam desimal): "))

# Hitung penjualan setelah pemasaran digital
penjualan_setelah = penjualan_digital(penjualan_sebelum, persentase_peningkatan)

print("Penjualan setelah pemasaran digital:", penjualan_setelah)

