import tkinter as tk
from tkinter import messagebox

# Biến đếm số lần sai
so_lan_sai = 0

def kiem_tra_dang_nhap():
    global so_lan_sai
    
    # Lấy dữ liệu từ ô nhập
    user = entry_user.get()
    password = entry_pass.get()

    # Kiểm tra điều kiện
    if user == "admin" and password == "111111":
        messagebox.showinfo("Thành công", "Đăng nhập thành công!")
        so_lan_sai = 0  # Reset bộ đếm
    else:
        so_lan_sai += 1
        if so_lan_sai >= 5:
            messagebox.showerror("Cảnh báo", "Bạn đã nhập sai quá 5 lần! Hệ thống sẽ tắt.")
            root.destroy()  # Lệnh này sẽ tắt luôn màn hình ứng dụng
        else:
            label_msg.config(text=f"Sai tài khoản hoặc mật khẩu! (Lần {so_lan_sai}/5)")

# Tạo cửa sổ giao diện chính
root = tk.Tk()
root.title("Đăng Nhập Hệ Thống")
root.geometry("300x250")

# Các thành phần trên giao diện
tk.Label(root, text="Tên đăng nhập:", font=("Arial", 10)).pack(pady=(20, 0))
entry_user = tk.Entry(root, font=("Arial", 12))
entry_user.pack(pady=5)

tk.Label(root, text="Mật khẩu:", font=("Arial", 10)).pack()
entry_pass = tk.Entry(root, font=("Arial", 12), show="*") # show="*" để che mật khẩu
entry_pass.pack(pady=5)

tk.Button(root, text="Đăng nhập", command=kiem_tra_dang_nhap, bg="green", fg="white", font=("Arial", 10, "bold")).pack(pady=15)

# Nơi hiển thị dòng chữ báo lỗi
label_msg = tk.Label(root, text="", fg="red", font=("Arial", 10))
label_msg.pack()

if __name__ == "__main__":
    root.mainloop()