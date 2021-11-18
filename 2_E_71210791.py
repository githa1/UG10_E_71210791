#2

suhu = (float(input ("Masukkan suhu tubuh Anda : ")))

if suhu < 32:
    print ("Anda kedinginan! Silahkan cari sesuatu yang hangat!")
elif suhu >= 32 and suhu <= 37.5:
    print ("Suhu Anda normal!")
elif suhu > 37.5 and suhu <= 50:
    print ("Anda demam! Jangan berpergian ke tempat fasilitas Umum.")
elif suhu > 50:
    print ("Anda bukan Manusia :)")
