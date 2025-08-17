import tkinter as tk
from tkinter import ttk  # Daha modern görünümlü widget'lar için
from tkinter import messagebox # Hata mesajları için
import random
import string
import pyperclip # panoya kopyalama özelliği için (pip install pyperclip)

# --- ANA UYGULAMA PENCERESİ ---
root = tk.Tk()
root.title("Güvenli Şifre Oluşturucu")
root.geometry("450x350") # Pencere boyutunu ayarla
root.resizable(False, False) # Pencere yeniden boyutlandırmayı engelle

# Stil ayarları için ttk kullanıyoruz
style = ttk.Style()
style.configure("TLabel", font=("Arial", 11))
style.configure("TButton", font=("Arial", 11, "bold"))
style.configure("TCheckbutton", font=("Arial", 10))

# --- ÇEKİRDEK ŞİFRE OLUŞTURMA MANTIĞI ---
# Bu fonksiyon Turtle versiyonuyla neredeyse aynıdır.
def generate_password(length, use_numbers, use_symbols):
    """Belirtilen kriterlere göre rastgele bir şifre oluşturur."""
    characters = string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
        
    if not characters:
        return "" # Karakter havuzu boşsa boş string döndür

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# --- ARAYÜZ İLE ETKİLEŞİM FONKSİYONLARI ---

def create_and_display_password():
    """Butona tıklandığında şifreyi oluşturur ve arayüzde gösterir."""
    try:
        # 1. Kullanıcı girdilerini al
        length = int(length_entry.get())
        use_numbers = use_numbers_var.get()
        use_symbols = use_symbols_var.get()

        # 2. Girdiyi doğrula
        if length <= 0:
            messagebox.showerror("Hata", "Şifre uzunluğu pozitif bir sayı olmalıdır!")
            return
        
        # 3. Şifreyi oluştur
        password = generate_password(length, use_numbers, use_symbols)

        # 4. Sonucu ekrandaki Entry widget'ına yazdır
        result_var.set(password)

    except ValueError:
        messagebox.showerror("Hata", "Lütfen geçerli bir sayısal uzunluk girin!")

def copy_to_clipboard():
    """Oluşturulan şifreyi panoya kopyalar."""
    password = result_var.get()
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Bilgi", "Şifre panoya kopyalandı!")
    else:
        messagebox.showwarning("Uyarı", "Kopyalanacak bir şifre bulunmuyor.")


# --- ARAYÜZ BİLEŞENLERİ (WIDGET'LAR) ---

# Widget'ları organize etmek için bir ana çerçeve (frame)
main_frame = ttk.Frame(root, padding="20 20 20 20")
main_frame.pack(fill="both", expand=True)

# Başlık
title_label = ttk.Label(main_frame, text="Şifre Oluşturucu Ayarları", font=("Arial", 14, "bold"))

# Şifre Uzunluğu için Label ve Entry (Girdi Kutusu)
length_label = ttk.Label(main_frame, text="Şifre Uzunluğu:")
length_entry = ttk.Entry(main_frame, width=10)
length_entry.insert(0, "12") # Başlangıç değeri olarak 12 gir

# Seçenekler için Checkbutton'lar (Onay Kutuları)
use_numbers_var = tk.BooleanVar(value=True) # Checkbox durumunu tutan değişken
numbers_check = ttk.Checkbutton(main_frame, text="Sayıları Dahil Et (0-9)", variable=use_numbers_var)

use_symbols_var = tk.BooleanVar(value=True) # Checkbox durumunu tutan değişken
symbols_check = ttk.Checkbutton(main_frame, text="Özel Karakterleri Dahil Et (!@#$)", variable=use_symbols_var)

# Şifre Oluşturma Butonu
generate_button = ttk.Button(main_frame, text="Şifre Oluştur", command=create_and_display_password)

# Sonucu göstermek için Entry
result_var = tk.StringVar() # Sonucu tutan değişken
result_entry = ttk.Entry(main_frame, textvariable=result_var, font=("Courier New", 12), state="readonly", width=35)

# Panoya Kopyala Butonu
copy_button = ttk.Button(main_frame, text="Panoya Kopyala", command=copy_to_clipboard)

# --- WIDGET'LARIN EKRANA YERLEŞTİRİLMESİ (LAYOUT) ---
# grid() metodu ile widget'ları bir tablo gibi düzenliyoruz.

title_label.grid(row=0, column=0, columnspan=2, pady=10)

length_label.grid(row=1, column=0, sticky="w", padx=5, pady=5)
length_entry.grid(row=1, column=1, sticky="w", padx=5, pady=5)

numbers_check.grid(row=2, column=0, columnspan=2, sticky="w", padx=5, pady=5)
symbols_check.grid(row=3, column=0, columnspan=2, sticky="w", padx=5, pady=5)

generate_button.grid(row=4, column=0, columnspan=2, pady=20)

result_entry.grid(row=5, column=0, columnspan=2, pady=10)
copy_button.grid(row=6, column=0, columnspan=2, pady=5)

# --- UYGULAMAYI BAŞLAT ---
# root.mainloop() pencerenin ekranda kalmasını ve kullanıcı etkileşimlerini dinlemesini sağlar.
root.mainloop()