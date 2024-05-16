import tkinter as tk
from tkinter import messagebox
import csv
import random

total_harga = 0

def read_csv(datauser):
    data = []
    with open(datauser, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    return data

def write_csv(datauser, data):
    with open(datauser, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

def signin_window():
    def attempt_signin():
        username = username_entry.get()
        password = password_entry.get()
        data = read_csv('datauser.csv')
        for row in data:
            if (row[0] == username or row[1] == username) and row[2] == password:
                messagebox.showinfo("Sign In", "Sign In berhasil. Selamat datang, " + row[1])
                signin_win.destroy()
                main_application()
                return
        messagebox.showerror("Error", "Username atau password tidak valid.")
    
    signin_win = tk.Toplevel()
    signin_win.title("Sign In")
    
    tk.Label(signin_win, text="Masukkan email atau username akun Anda:").grid(row=0, column=0)
    username_entry = tk.Entry(signin_win)
    username_entry.grid(row=0, column=1)
    
    tk.Label(signin_win, text="Masukkan password akun Anda:").grid(row=1, column=0)
    password_entry = tk.Entry(signin_win, show="*")
    password_entry.grid(row=1, column=1)
    
    tk.Button(signin_win, text="Sign In", command=attempt_signin).grid(row=2, columnspan=2)

def signup_window():
    def attempt_signup():
        email = email_entry.get()
        username = username_entry.get()
        password = password_entry.get()
        data = read_csv('datauser.csv')
        for row in data:
            if row[0] == email or row[1] == username:
                messagebox.showerror("Error", "Email atau username telah digunakan.")
                return
        data.append([email, username, password])
        write_csv('datauser.csv', data)
        messagebox.showinfo("Sign Up", "Akun berhasil dibuat, silakan lakukan Sign In.")
        signup_win.destroy()
        signin_window()
    
    signup_win = tk.Toplevel()
    signup_win.title("Sign Up")
    
    tk.Label(signup_win, text="Masukkan email:").grid(row=0, column=0)
    email_entry = tk.Entry(signup_win)
    email_entry.grid(row=0, column=1)
    
    tk.Label(signup_win, text="Masukkan username:").grid(row=1, column=0)
    username_entry = tk.Entry(signup_win)
    username_entry.grid(row=1, column=1)
    
    tk.Label(signup_win, text="Masukkan password:").grid(row=2, column=0)
    password_entry = tk.Entry(signup_win, show="*")
    password_entry.grid(row=2, column=1)
    
    tk.Button(signup_win, text="Sign Up", command=attempt_signup).grid(row=3, columnspan=2)

def main_application():
    def search_kost():
        def show_kost_detail(pilihkost):
            for i in daftar_kost:
                if i[0] == pilihkost:
                    detail_win = tk.Toplevel()
                    detail_win.title("Detail Kost")
                    
                    detail_text = f"""
Nama Kost: {i[1]}
Alamat: {i[3]}
Ukuran: {i[4]}
Harga Kost/Tahun: {i[5]}
Fasilitas: {i[6]}
Narahubung: {i[7]}
Jumlah Kamar yang Tersedia: {i[8]}
"""
                    tk.Label(detail_win, text=detail_text).pack()
                    
                    def proceed_payment():
                        try:
                            jumlah_kamar = int(kamar_entry.get())
                            if 1 <= jumlah_kamar <= int(i[8]):
                                global total_harga
                                total_harga = jumlah_kamar * int(i[5])
                                detail_win.destroy()
                                payment_window()
                            else:
                                messagebox.showerror("Error", "Jumlah kamar tidak valid.")
                        except ValueError:
                            messagebox.showerror("Error", "Masukan harus berupa angka.")
                    
                    tk.Label(detail_win, text="Masukkan jumlah kamar kost yang ingin disewa:").pack()
                    kamar_entry = tk.Entry(detail_win)
                    kamar_entry.pack()
                    tk.Button(detail_win, text="Lanjutkan ke Pembayaran", command=proceed_payment).pack()
                    return

        jeniskost = jenis_kost_var.get()
        harga = harga_var.get()
        if jeniskost not in ('L', 'P') or harga not in (1, 2, 3):
            messagebox.showerror("Error", "Pilihan tidak valid.")
            return
        
        daftar_kost = []
        kost_listbox.delete(0, tk.END)
        
        with open('datakost.txt') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for i in csv_reader:
                if (jeniskost == 'L' and i[2] == 'L') or (jeniskost == 'P' and i[2] == 'P'):
                    if (harga == 1 and int(i[5]) <= 5000000) or (harga == 2 and 5000000 < int(i[5]) <= 10000000) or (harga == 3 and int(i[5]) > 10000000):
                        daftar_kost.append(i)
                        kost_listbox.insert(tk.END, f"{i[0]}. {i[1]}")
        
        def on_select(evt):
            w = evt.widget
            index = int(w.curselection()[0])
            value = w.get(index)
            pilihkost = value.split(".")[0]
            show_kost_detail(pilihkost)
        
        kost_listbox.bind('<<ListboxSelect>>', on_select)
    
    main_app_win = tk.Toplevel()
    main_app_win.title("Program Pencarian Kost")
    
    tk.Label(main_app_win, text="Pilih Jenis Kost (L/P)").grid(row=0, column=0)
    jenis_kost_var = tk.StringVar(value='L')
    tk.Entry(main_app_win, textvariable=jenis_kost_var).grid(row=0, column=1)
    
    tk.Label(main_app_win, text="Pilih Daftar Harga Kost/Tahun (1/2/3)").grid(row=1, column=0)
    harga_var = tk.IntVar(value=1)
    tk.Entry(main_app_win, textvariable=harga_var).grid(row=1, column=1)
    
    tk.Button(main_app_win, text="Cari Kost", command=search_kost).grid(row=2, columnspan=2)
    
    kost_listbox = tk.Listbox(main_app_win)
    kost_listbox.grid(row=3, columnspan=2)

def payment_window():
    def generate_kode_pembayaran():
        kode_bayar = ''.join(random.choices('0123456789', k=6))
        return kode_bayar
    
    def validate_payment():
        metode_pembayaran = metode_var.get()
        kode_input = kode_entry.get()
        if kode_input == kode_bayar:
            messagebox.showinfo("Pembayaran", "Pembayaran berhasil. Kode valid.")
            payment_win.destroy()
            bukti_pembayaran(metode_pembayaran)
        else:
            messagebox.showerror("Pembayaran", "Kode pembayaran tidak valid, pembayaran gagal.")
    
    def bukti_pembayaran(metode):
        metode_dict = {1: "BANK MANDIRI", 2: "BANK BCA", 3: "GOPAY", 4: "CASH"}
        metode_pembayaran = metode_dict[metode]
        receipt_text = f"""
Bukti Pembayaran:
Metode Pembayaran: {metode_pembayaran}
Kode Bayar: {kode_bayar}
Total Pembayaran: Rp {total_harga}
Pemesanan kost sudah otomatis masuk ke dalam sistem.
Terima kasih atas pembayaran Anda.
"""
        messagebox.showinfo("Bukti Pembayaran", receipt_text)
    
    kode_bayar = generate_kode_pembayaran()
    
    payment_win = tk.Toplevel()
    payment_win.title("Pembayaran")
    
    tk.Label(payment_win, text="Pilih metode pembayaran:").grid(row=0, column=0)
    metode_var = tk.IntVar(value=1)
    tk.Radiobutton(payment_win, text="BANK MANDIRI", variable=metode_var, value=1).grid(row=1, column=0)
    tk.Radiobutton(payment_win, text="BANK BCA", variable=metode_var, value=2).grid(row=2, column=0)
    tk.Radiobutton(payment_win, text="GOPAY", variable=metode_var, value=3).grid(row=3, column=0)
    tk.Radiobutton(payment_win, text="CASH", variable=metode_var, value=4).grid(row=4, column=0)
    
    tk.Label(payment_win, text="Masukkan kode pembayaran:").grid(row=5, column=0)
    kode_entry = tk.Entry(payment_win)
    kode_entry.grid(row=5, column=1)
    
    tk.Label(payment_win, text=f"Kode Pembayaran Anda: {kode_bayar}").grid(row=6, columnspan=2)
    
    tk.Button(payment_win, text="Konfirmasi Pembayaran", command=validate_payment).grid(row=7, columnspan=2)

def main_window():
    root = tk.Tk()
    root.title("Program Pencarian Kost")
    
    tk.Label(root, text="Selamat Datang di Program Pencarian Kost!").pack()
    tk.Button(root, text="Sign In", command=signin_window).pack()
    tk.Button(root, text="Sign Up", command=signup_window).pack()
    
    root.mainloop()

main_window()