public class Triangle {
    
    public static String classify(int a, int b, int c) {
        // Path 1: Nút 1 -> 2
        if (a <= 0 || b <= 0 || c <= 0) {
            return "Invalid";
        }
        // Path 2: Nút 1 -> 3 -> 4
        if (a + b <= c || a + c <= b || b + c <= a) {
            return "Not a triangle";
        }
        // Path 3: Nút 1 -> 3 -> 5 -> 6
        if (a == b && b == c) {
            return "Equilateral";
        } 
        // Path 4: Nút 1 -> 3 -> 5 -> 7 -> 8
        else if (a == b || b == c || a == c) {
            return "Isosceles";
        } 
        // Path 5: Nút 1 -> 3 -> 5 -> 7 -> 9
        else {
            return "Scalene";
        }
    }
}