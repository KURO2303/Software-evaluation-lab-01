public class NumberChecker {
    
    // Phương thức kiểm tra chẵn lẻ, chứa vòng lặp và rẽ nhánh
    public String processNumbers(int n) {
        // Lệnh rẽ nhánh phụ xử lý ngoại lệ để tạo thêm đường đi
        if (n < 1) {
            return "Khong hop le";
        }
        
        StringBuilder result = new StringBuilder();
        
        // Vòng lặp
        for (int i = 1; i <= n; i++) {
            // Lệnh rẽ nhánh chính
            if (i % 2 == 0) {
                result.append("Chan ");
            } else {
                result.append("Le ");
            }
        }
        
        return result.toString().trim();
    }
}