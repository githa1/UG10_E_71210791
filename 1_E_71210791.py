
print ("==== Kalkulator Akar dan Pangkat ====")
print ("Pilihan menu :")
pil1 = print ("1. Pangkat 2 (Kuadrat)")
pil2 = print ("2. Pangkat 3 (Kubik)")
pil3 = print("3. Akar Kuadrat")
pilihan = int(input ("Masukkan menu yang anda pilih : "))

if (pilihan >=1) and (pilihan <=2):
    bil = int(input("Masukkan bilangan yang ingin di pangkatkan : "))
    if pilihan ==1:
        r = (bil**2)
        print ("Hasil dari pemangkatan bilangan", (bil), "dengan 2 (Kuadrat) adalah ", r)
    elif pilihan ==2:
        r = (bil**3)
        print ("Hasil dari pemangkatan bilangan", (bil), "dengan 3 (Kubik) adalah ", r)
    elif pilihan ==3:
        r = (bil**0.5)
        print ("Hasil akar kuadrat dari", (bil), "adalah", r)
    else:
        print ("Pilihan menu yang dimasukkan tidak sesuai!")
        
        
