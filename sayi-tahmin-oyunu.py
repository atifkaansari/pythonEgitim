import random
import tkinter as tk
from tkinter import messagebox
def oyun():
    global sayi, hak
    sayi = random.randint(1, 50)
    hak = 5 
    hak_label.config(text=f"Kalan Hakkınız: {hak}")
    tahmin_entry.delete(0, tk.END)
def tahmin_et():
    global hak
    try:
        tahmin = int(tahmin_entry.get())

        if hak > 0:
            if tahmin < sayi:
                messagebox.showinfo("İpucu", "Tahmininiz çok düşük. Daha yüksek bir sayı deneyin!")
            elif tahmin > sayi:
                messagebox.showinfo("İpucu", "Tahmininiz çok yüksek. Daha düşük bir sayı deneyin!")
            else:
                messagebox.showinfo("Tebrikler", f"Tebrikler! {sayi} sayısını doğru tahmin ettiniz.")
                oyun_tekrar()
            hak -= 1
            hak_label.config(text=f"Kalan Hakkınız: {hak}")

            if hak == 0:
                messagebox.showinfo("Bitti", f"Maalesef, tahmin hakkınız bitti! Doğru sayı {sayi} idi.")
                oyun_tekrar()
        else:
            messagebox.showinfo("Bitti", "Tahmin hakkınız bitti!")
            oyun_tekrar()
    except ValueError:
        messagebox.showerror("Hata", "Lütfen geçerli bir sayı girin!")
def oyun_tekrar():
    yeniden = messagebox.askyesno("Tekrar Oyna", "Tekrar oynamak ister misiniz?")
    if yeniden:
        oyun()
    else:
        window.quit()
window = tk.Tk()
window.title("Sayı Tahmin Oyunu")
window.geometry("400x300")
label = tk.Label(window, text="1 ile 50 arasında bir sayı tahmin edin!", font=("Arial", 14))
label.pack(pady=20)
tahmin_entry = tk.Entry(window, font=("Arial", 14))
tahmin_entry.pack(pady=10)
hak_label = tk.Label(window, text="Kalan Hakkınız: 5", font=("Arial", 14))
hak_label.pack(pady=10)
tahmin_button = tk.Button(window, text="Tahmin Et", font=("Arial", 14), command=tahmin_et)
tahmin_button.pack(pady=20)
oyun()
window.mainloop()