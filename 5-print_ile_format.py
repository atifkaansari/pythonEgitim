#Girilen Sayı kadar tablo oluşturu ve sayıları içine yazar.
#Örnek 5 girdiniz 5x5'lik yani 5 satır 5 sütunluk bir tablo oluşturur.

sayi = int(input("Lütfen tablo ölçüsünü giriniz: "))
genislik = len(str(sayi * sayi))
for satir in range(1, sayi + 1 ) :
    for sutun in range(1, sayi + 1):
        deger = satir*sutun
        print(f"{deger:>{genislik}}", end=" ")
    print()