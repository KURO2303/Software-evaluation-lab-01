import unittest

# ==========================================
# 1. HÀM XỬ LÝ NGHIỆP VỤ (HỆ THỐNG BÁN VÉ)
# ==========================================
def xac_dinh_loai_ve(thoi_gian_str):
    """
    Hàm nhận vào chuỗi thời gian định dạng HH:MM và trả về loại vé.
    """
    try:
        # Tách giờ và phút
        gio, phut = map(int, thoi_gian_str.split(':'))
    except ValueError:
        return "Lỗi định dạng thời gian"

    # Xử lý ngoại lệ thời gian không hợp lệ (V5, V6)
    if gio < 0 or gio > 23 or phut < 0 or phut > 59:
        return "Thời gian không hợp lệ"

    # Quy đổi tất cả ra số phút tính từ 00:00 để dễ so sánh
    tong_phut = gio * 60 + phut

    # Các mốc thời gian quy đổi ra phút
    moc_0930 = 9 * 60 + 30   # 570 phút
    moc_1600 = 16 * 60       # 960 phút
    moc_1930 = 19 * 60 + 30  # 1170 phút

    # Vùng 1: [00:00 - 09:29]
    if tong_phut < moc_0930:
        return "Vé thường"
    # Vùng 2: [09:30 - 16:00]
    elif moc_0930 <= tong_phut <= moc_1600:
        return "Vé tiết kiệm"
    # Vùng 3: [16:01 - 19:30]
    elif moc_1600 < tong_phut <= moc_1930:
        return "Vé thường"
    # Vùng 4: [19:31 - 23:59]
    else:
        return "Vé tiết kiệm"

# ==========================================
# 2. MÃ KIỂM THỬ TỰ ĐỘNG BẰNG UNITTEST
# ==========================================
class TestHeThongBanVe(unittest.TestCase):

    # --- KIỂM THỬ VÙNG 1: Trước 09:30 sáng ---
    def test_tc_01_v1_bien_duoi(self):
        self.assertEqual(xac_dinh_loai_ve("00:00"), "Vé thường")

    def test_tc_02_v1_trong_vung(self):
        self.assertEqual(xac_dinh_loai_ve("05:30"), "Vé thường")

    def test_tc_03_v1_bien_tren(self):
        self.assertEqual(xac_dinh_loai_ve("09:29"), "Vé thường")

    # --- KIỂM THỬ VÙNG 2: 09:30 sáng đến 16:00 ---
    def test_tc_04_v2_bien_duoi(self):
        self.assertEqual(xac_dinh_loai_ve("09:30"), "Vé tiết kiệm")

    def test_tc_05_v2_trong_vung(self):
        self.assertEqual(xac_dinh_loai_ve("13:15"), "Vé tiết kiệm")

    def test_tc_06_v2_bien_tren(self):
        self.assertEqual(xac_dinh_loai_ve("16:00"), "Vé tiết kiệm")

    # --- KIỂM THỬ VÙNG 3: 16:01 chiều đến 19:30 ---
    def test_tc_07_v3_bien_duoi(self):
        self.assertEqual(xac_dinh_loai_ve("16:01"), "Vé thường")

    def test_tc_08_v3_trong_vung(self):
        self.assertEqual(xac_dinh_loai_ve("18:00"), "Vé thường")

    def test_tc_09_v3_bien_tren(self):
        self.assertEqual(xac_dinh_loai_ve("19:30"), "Vé thường")

    # --- KIỂM THỬ VÙNG 4: 19:31 tối đến 23:59 ---
    def test_tc_10_v4_bien_duoi(self):
        self.assertEqual(xac_dinh_loai_ve("19:31"), "Vé tiết kiệm")

    def test_tc_11_v4_trong_vung(self):
        self.assertEqual(xac_dinh_loai_ve("21:45"), "Vé tiết kiệm")

    def test_tc_12_v4_bien_tren(self):
        self.assertEqual(xac_dinh_loai_ve("23:59"), "Vé tiết kiệm")

    # --- KIỂM THỬ NGOẠI LỆ (VÙNG 5, VÙNG 6 & LỖI) ---
    def test_tc_13_ngoai_le_am(self):
        self.assertEqual(xac_dinh_loai_ve("-01:00"), "Lỗi định dạng thời gian")

    def test_tc_14_ngoai_le_vuot_24h(self):
        self.assertEqual(xac_dinh_loai_ve("24:00"), "Thời gian không hợp lệ")

    def test_tc_15_ngoai_le_sai_phut(self):
        self.assertEqual(xac_dinh_loai_ve("10:99"), "Thời gian không hợp lệ")
        
    def test_tc_16_ngoai_le_chu_cai(self):
        self.assertEqual(xac_dinh_loai_ve("ABC:XYZ"), "Lỗi định dạng thời gian")

# Khởi chạy kiểm thử
if __name__ == '__main__':
    unittest.main()