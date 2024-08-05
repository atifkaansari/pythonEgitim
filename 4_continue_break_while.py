sayi=1
toplam=0
print("Negatif Sayı girilince Program sonlanır. 0 girilince döngüden çıkar")
print("99'a kadr giriniz. 100 ve üzeri sayılar toplama alınmaz")
while sayi>0:
    sayi=int(input("Sayı giriniz: "))
    if sayi==0:break
    if sayi>99:
        print("99'dan büyük sayı girdiniz. İşleme alınamaz")
        continue
    if sayi>0:
        toplam+=sayi
print("Toplam: ",toplam)