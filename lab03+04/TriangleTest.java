import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class TriangleTest {

    @Test
    public void testPath1_Invalid() {
        // Path 1: a <= 0
        assertEquals("Invalid", Triangle.classify(0, 5, 5));
    }

    @Test
    public void testPath2_NotATriangle() {
        // Path 2: a + b <= c
        assertEquals("Not a triangle", Triangle.classify(1, 2, 3));
    }

    @Test
    public void testPath3_Equilateral() {
        // Path 3: a == b && b == c
        assertEquals("Equilateral", Triangle.classify(5, 5, 5));
    }

    @Test
    public void testPath4_Isosceles() {
        // Path 4: a == b (nhưng khác c)
        assertEquals("Isosceles", Triangle.classify(5, 5, 8));
    }

    @Test
    public void testPath5_Scalene() {
        // Path 5: Ba cạnh khác nhau và hợp lệ
        assertEquals("Scalene", Triangle.classify(3, 4, 5));
    }
}