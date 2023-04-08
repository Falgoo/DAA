package hw3;

import java.util.Date;

public class Exercise2 {
    public static void main(String[] args) {
        int n = 6;
        System.out.println("Print the binary representation of " + n + " is:");
        System.out.println(decToBin(n));
        System.out.println("Print the " + n + "th Fibonacci number:");
        System.out.println(fibonacci(6));
        System.out.println("Tower of Hanoi:");
        towerOfHanoi(3, 'A', 'C', 'B');

        for (int i = 1; i <= 5; i++) {
            int m = 10;
            m = m * i;
            long startTime = new Date().getTime();
            fibonacci(m);
            long endTime = new Date().getTime();
            System.out.println("n = " + m + ", execution time in milliseconds: " + (endTime - startTime));

        }
    }


    public static int decToBin(int n) {
        if (n == 1) {

            return 1;
        }
        return decToBin(n / 2) * 10 + n % 2;
    }

    public static int fibonacci(int n) {
        if (n <= 1)
            return n;
        return fibonacci(n - 1) + fibonacci(n - 2);
    }

    public static void towerOfHanoi(int n, char start,
                                    char dest, char temp) {
        if (n == 0) {
            return;
        }
        towerOfHanoi(n - 1, start, temp, dest);
        System.out.println("Move disk " + n + " from "
                + start + " to "
                + dest);
        towerOfHanoi(n - 1, temp, dest, start);
    }
}
