import tkinter as tk

def tambah():
    hasil = float(angka1_entry.get()) + float(angka2_entry.get())
    hasil_label.config(text="Hasil: " + str(hasil))

def kurang():
    hasil = float(angka1_entry.get()) - float(angka2_entry.get())
    hasil_label.config(text="Hasil: " + str(hasil))

def kali():
    hasil = float(angka1_entry.get()) * float(angka2_entry.get())
    hasil_label.config(text="Hasil: " + str(hasil))

def bagi():
    try:
        hasil = float(angka1_entry.get()) / float(angka2_entry.get())
        hasil_label.config(text="Hasil: " + str(hasil))
    except ZeroDivisionError:
        hasil_label.config(text="Error! Pembagian dengan nol tidak diperbolehkan.")

# Membuat GUI
root = tk.Tk()
root.title("Kalkulator")

# Input angka pertama
tk.Label(root, text="Angka Pertama:").grid(row=0, column=0)
angka1_entry = tk.Entry(root)
angka1_entry.grid(row=0, column=1)

# Input angka kedua
tk.Label(root, text="Angka Kedua:").grid(row=1, column=0)
angka2_entry = tk.Entry(root)
angka2_entry.grid(row=1, column=1)

# Tombol operasi
tk.Button(root, text="+", command=tambah).grid(row=2, column=0)
tk.Button(root, text="-", command=kurang).grid(row=2, column=1)
tk.Button(root, text="*", command=kali).grid(row=3, column=0)
tk.Button(root, text="/", command=bagi).grid(row=3, column=1)

# Label hasil
hasil_label = tk.Label(root, text="Hasil: ")
hasil_label.grid(row=4, columnspan=2)

root.mainloop()
