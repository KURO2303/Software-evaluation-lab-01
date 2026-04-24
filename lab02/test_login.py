import unittest
from unittest.mock import patch
import tkinter as tk
import login  # Nạp file login.py của bạn vào để test

class TestLoginApp(unittest.TestCase):
    
    def setUp(self):
        """Hàm này chạy trước mỗi kịch bản test để reset lại trạng thái ban đầu"""
        login.so_lan_sai = 0 # Reset bộ đếm
        login.entry_user.delete(0, tk.END) # Xóa text cũ trong ô user
        login.entry_pass.delete(0, tk.END) # Xóa text cũ trong ô pass
        login.label_msg.config(text="")    # Xóa thông báo lỗi

    @patch('login.messagebox.showinfo')
    def test_dang_nhap_thanh_cong(self, mock_showinfo):
        """Test Case: Đăng nhập đúng tài khoản và mật khẩu"""
        # Giả lập nhập liệu
        login.entry_user.insert(0, "admin")
        login.entry_pass.insert(0, "111111")
        
        # Gọi hàm kiểm tra (giả lập việc bấm nút)
        login.kiem_tra_dang_nhap()

        # Kiểm tra xem messagebox thông báo thành công có bật lên không
        mock_showinfo.assert_called_with("Thành công", "Đăng nhập thành công!")
        # Kiểm tra bộ đếm có bằng 0 không
        self.assertEqual(login.so_lan_sai, 0)

    def test_dang_nhap_that_bai(self):
        """Test Case: Đăng nhập sai (dưới 5 lần)"""
        login.entry_user.insert(0, "admin")
        login.entry_pass.insert(0, "mat_khau_sai")
        
        login.kiem_tra_dang_nhap()

        # Kiểm tra bộ đếm tăng lên 1
        self.assertEqual(login.so_lan_sai, 1)
        # Kiểm tra dòng chữ báo lỗi hiển thị đúng không
        self.assertEqual(login.label_msg.cget("text"), "Sai tài khoản hoặc mật khẩu! (Lần 1/5)")

    @patch('login.messagebox.showerror')
    @patch('login.root.destroy')
    def test_khoa_tai_khoan_qua_5_lan(self, mock_destroy, mock_showerror):
        """Test Case: Đăng nhập sai 5 lần và ứng dụng bị tắt"""
        login.entry_user.insert(0, "admin")
        login.entry_pass.insert(0, "mat_khau_sai")

        # Cho chạy vòng lặp sai 5 lần liên tiếp
        for i in range(5):
            login.kiem_tra_dang_nhap()

        # Kiểm tra bộ đếm có ghi nhận đúng 5 lần không
        self.assertEqual(login.so_lan_sai, 5)
        # Kiểm tra xem messagebox báo lỗi khóa có xuất hiện không
        mock_showerror.assert_called_with("Cảnh báo", "Bạn đã nhập sai quá 5 lần! Hệ thống sẽ tắt.")
        # Kiểm tra xem lệnh tắt màn hình (root.destroy) có được gọi không
        mock_destroy.assert_called_once()

if __name__ == '__main__':
    unittest.main()