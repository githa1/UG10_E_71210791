#4

a = int(input("Masukkan bilangan 1 : "))
b = int(input("Masukkan bilangan 2 : "))
c = int(input("Masukkan bilangan 3 : "))


if a>b and a>c:
     if b>c:
         r = c,b,a
         print("Urutan bilangan dari yang terkecil adalah ",r)
     else:
         r = b,c,a
         print ("Urutan bilangan dari yang terkecil adalah ",r)
elif b>a and b>c:
    if a>c:
        r = c,a,b
        print ("Urutan bilangan dari yang terkecil adalah ",r)
    else:
        r = a,c,b
        print ("Urutan bilangan dari yang terkecil adalah ",r)
else:
    if a>b:
        r = b,a,c
        print("Urutan bilangan dari yang terkecil adalah ",r)
    else:
        r = a,b,c
        print ("Urutan bilangan dari yang terkecil adalah ",r)
