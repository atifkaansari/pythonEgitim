def toplama():
    print("\n# Toplama islemi yap")
    sayi1 = float(input("1. sayiyi giriniz giriniz: "))
    sayi2 = float(input("2. sayiyi giriniz giriniz: "))
    toplam = sayi1 + sayi2 
    print(f"sonuc= {toplam}")

def cikarma():
    print("\n# Toplama islemi yap")
    sayi1 = float(input("1. sayiyi giriniz giriniz: "))
    sayi2 = float(input("2. sayiyi giriniz giriniz: "))
    fark = sayi1 - sayi2 
    print(f"sonuc= {fark}")

def carpma():
    print("\n# Toplama islemi yap")
    sayi1 = float(input("1. sayiyi giriniz giriniz: "))
    sayi2 = float(input("2. sayiyi giriniz giriniz: "))
    carpim = sayi1 * sayi2 
    print(f"sonuc= {carpim}")
    
def bolme():
    print("\n# Toplama islemi yap")
    sayi1 = float(input("1. sayiyi giriniz giriniz: "))
    sayi2 = float(input("2. sayiyi giriniz giriniz: "))
    bolum = sayi1 / sayi2 
    print(f"sonuc= {bolum}")
def main():
    while True:
        print("-" * 30)
        print("---Hesap Makinesi---")
        print("-" * 30)
        print("1 - Toplama")
        print("2 - cikartma")
        print("3 - carpma")
        print("4 - Bolme")
        print("0 - Programi sonlandir")
        print("-" * 30)

        choice = input("Seciniz (0/1/2/3/4): ")

        if choice == "1":
            toplama()
        elif choice == "2":
            cikarma()
        elif choice == "3":
            carpma()
        elif choice == "4":
            bolme()
        elif choice == "0":
            print("Program sonlandiriliyor")
            break
        else:
            print("Gecersiz Secim, lütfen 0, 1, 2, 3 veya 4  giriniz.")

main()

print("Program bitti.")