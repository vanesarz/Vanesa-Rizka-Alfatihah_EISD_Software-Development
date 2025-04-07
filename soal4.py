import pandas as pd

def cek_duplikasi(data):
    df = pd.DataFrame(data)

    duplikat = df[df.duplicated(keep=False)]

    print("\n=================================== Duplikasi Data ====================================\n")
    print("Data\t  :", df[0].tolist())

    if not duplikat.empty:
        print("Duplikasi : True")
    else:
        print("Duplikasi : False")
        
    print("Duplikat  :", duplikat[0].tolist())
    print("\n=======================================================================================\n")

angka = [20, 1, 3, 2, 4, 6, 8, 5, 7, 9, 11, 13, 15, 10,  12, 14, 16, 18, 20, 17, 19]

cek_duplikasi(angka)