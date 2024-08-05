print(15*"-")
print("Üstün Başarı Belgesi sorgulama ekranına hoşgeldiniz !")
print("Not ortalamanız 90 ve üzeriyse Üstün Başarı Belgesi almaya hak kazandınız!")
print("Vize sınavınız ortalamanızı %30 , Final sınavınız ise %70 etkilemektedir!")
print(15*"-")

vize=int(input("Vize notunuzu giriniz: " ))
final=int(input("Final notunuzu giriniz: " ))
print(15*"-")

ort=(final + vize)/2
if ort >= 90:
    print("Not Ortalamanız: ", ort)
    print("Üstün Başarı Belgesi Almaya Hak Kazandınız, Tebrikler!")
else:
    print("Ortalamanız: ", ort)
    print("Üzgünüz, Maalesef Üstün Başarı Belgesi kazanamadınız...")
    
print(15*"-")
