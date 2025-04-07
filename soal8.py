list_produk = {
    "Produk"    : ["TV", "headphone", "baju", "gitar", "sepatu", "kamera"],
    "Kategori"  : ["elektronik", "elektronik", "fashion", "musik", "olahraga", "elektronik"],
    "Harga"     : [1000, 200, 50, 300, 80, 600]
}

list_pelanggan = {
    "Nama"  : ["Rina", "Budi", "Hartono"],
    "Minat" : [["elektronik", "musik"], ["fashion", "musik"], ["olahraga", "elektronik"]],
    "Beli"  : [["TV", "headphone"], ["baju", "gitar"], ["sepatu", "kamera"]]
}

import pandas as pd

df_produk       = pd.DataFrame(list_produk)
df_pelanggan    = pd.DataFrame(list_pelanggan)

def rekomendasi(pelanggan):
    data    = df_pelanggan[df_pelanggan["Nama"] == pelanggan].iloc[0]
    minat   = data["Minat"]

    rekomendasi_produk = df_produk[df_produk["Kategori"].isin(minat)]["Produk"].tolist()

    print(f"{pelanggan}\t: {rekomendasi_produk}")

print()

rekomendasi("Rina")
rekomendasi("Budi")
rekomendasi("Hartono")

print()