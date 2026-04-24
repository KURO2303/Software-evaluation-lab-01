import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class NumberProcessorTest {

    NumberProcessor processor = new NumberProcessor();

    // ... (Giữ lại testStatementCoverage ở trên) ...

    @Test
    public void testPathCoverage_LoopBoundaries() {
        // Đường đi 1: Bỏ qua hoàn toàn vòng lặp (limit <= 0)
        assertEquals(-1, processor.sumEvenNumbers(-5));

        // Đường đi 2: Lặp đúng 1 lần (limit = 1) - Vào nhánh điều kiện Sai
        assertEquals(0, processor.sumEvenNumbers(1));

        // Đường đi 3: Lặp đúng 2 lần (limit = 2) - Vào nhánh điều kiện Sai, rồi Đúng
        assertEquals(2, processor.sumEvenNumbers(2));

        // Đường đi 4: Lặp nhiều lần (limit = 5) - Kiểm tra tính ổn định của luồng lặp lại
        // 1 (Sai) -> 2 (Đúng, sum=2) -> 3 (Sai) -> 4 (Đúng, sum=6) -> 5 (Sai)
        assertEquals(6, processor.sumEvenNumbers(5));
    }
}