import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class NumberProcessorTest {

    NumberProcessor processor = new NumberProcessor();

    @Test
    public void testStatementCoverage() {
        // Bao phủ dòng: return -1;
        assertEquals(-1, processor.sumEvenNumbers(0));

        // Bao phủ dòng khởi tạo, vòng lặp for, nhánh if(i%2==0) và dòng return sum;
        assertEquals(2, processor.sumEvenNumbers(2));
    }
}
