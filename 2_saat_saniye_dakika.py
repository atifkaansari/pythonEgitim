sayı=int(input("Saniye Giriniz: "))
saat=sayı//3600
kalan=sayı%3600
dakika=kalan//60
saniye=sayı%60
print(saat,dakika,saniye,sep=":")