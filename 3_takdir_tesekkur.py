top_ort=0
tak=0
tsk=0
bas=0
ogrenci=1
while ogrenci<=10:
    print(str(ogrenci))
    sinav=float(input(" Öğrenci Sınav Notu Giriniz: "))
    sozlu=float(input(" Öğrenci Sözlü Notu Giriniz: "))
    ogr_ort=sinav+sozlu//2
    if ogr_ort in range(0,101):
        top_ort=top_ort+ogr_ort
        if ogr_ort>=80:
            tak+=1
        if ogr_ort>=70 and ogr_ort<85:
            tsk+=1
        ogrenci+=1
    else:
        print("0-100 arası sayı giriniz")
        continue

print("Sınıf Ortalaması= ", round (top_ort/10,2))
print("Takdir Belgesi Sayısı = ",tak)
print("Teşekkür Belgesi Sayısı = ",tsk)