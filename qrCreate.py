import qrcode

code = qrcode.QRCode(
    version=1,
    error_correction = qrcode.constants.ERROR_CORRECT_L,
    box_size=50,
    border=2
)

code.add_data('') #İki tırnak arasına üretilecek linki giriniz
code.make(fit=True)

image = code.make_image(fill_color="black",back_color="white")
image.save('.png') #Dosya adını uzantıdan önce giriniz ve kodu çalıştırınız. Dosya kodun bulunduğu klasöre kaydedilecektir.
