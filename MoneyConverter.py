jawab = "Y"

def usdtoidr(usd):
    hasil = usd * float(15000)
    return hasil

def idrtousd(idr):
    hasil = idr / float(15000)
    return hasil

while(jawab == "Y"):
    print("PROGRAM KONVEKSI MATA UANG")
    print("==========================")
    print("MENU PILIHAN :")
    print("1.Konversi dari DOLLAR ke RUPIAH")
    print("2.Konversi dari RUPIAH ke DOLLAR")
    print("3.Keluar")
    print("==========================")
    pilihan = input("Masukan Pilihan Konversi : ")
    if pilihan == 1:
        joko = input("Masukan Jumlah DOLLAR : $")
        print"Nilai USD $",joko,"= RP",usdtoidr(joko)
    elif pilihan == 2:
        joko = input("Masukan Jumlah RUPIAH : RP")
        print"Nilai Rupiah RP", joko, "= $", idrtousd(joko)
    else:
        jawab="N"
    if jawab == "Y":
        jawab = raw_input("Kembali ke menu pilihan ? [Y/N] : ")

print("Terima Kasih")
