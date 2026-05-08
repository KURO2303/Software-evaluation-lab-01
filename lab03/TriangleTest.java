import static org.junit.jupiter.api.Assertions.assertEquals;
import org.junit.jupiter.api.Test;

public class TriangleTest {

    // TC1: Kiểm tra đầu vào không hợp lệ (Path 1)
    @Test
    public void testInvalidTriangle() {
        String result = Triangle.classify(0, 4, 5);
        assertEquals("Invalid", result, "Nên trả về Invalid khi có cạnh <= 0");
    }

    // TC2: Kiểm tra không phải tam giác (Path 2)
    @Test
    public void testNotATriangle() {
        String result = Triangle.classify(1, 2, 4);
        assertEquals("Not a triangle", result, "Nên trả về Not a triangle khi tổng 2 cạnh nhỏ hơn cạnh còn lại");
    }

    // TC3: Kiểm tra tam giác đều (Path 3)
    @Test
    public void testEquilateralTriangle() {
        String result = Triangle.classify(3, 3, 3);
        assertEquals("Equilateral", result, "Nên trả về Equilateral khi 3 cạnh bằng nhau");
    }

    // TC4: Kiểm tra tam giác cân (Path 4)
    @Test
    public void testIsoscelesTriangle() {
        String result = Triangle.classify(3, 3, 4);
        assertEquals("Isosceles", result, "Nên trả về Isosceles khi có 2 cạnh bằng nhau");
    }

    // TC5: Kiểm tra tam giác thường (Path 5)
    @Test
    public void testScaleneTriangle() {
        String result = Triangle.classify(3, 4, 5);
        assertEquals("Scalene", result, "Nên trả về Scalene khi 3 cạnh khác nhau và tạo thành tam giác hợp lệ");
    }
}