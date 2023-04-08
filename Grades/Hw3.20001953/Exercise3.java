package hw3;

import static java.lang.Math.*;

public class Exercise3 {
    public static void main(String[] args) {
        int v[] = new int[] { 60, 100, 90 };
        int w[] = new int[] { 10, 25, 40 };
        int W = 50;
        int n = v.length;
        System.out.println(knapsack(w, v, n, W));
    }

    public static int knapsack(int[] w, int[] v, int n, int W) {
        if (n <= 0) {
            return 0;
        } else if (w[n - 1] > W) {
            return knapsack(w, v, n - 1, W);
        } else {
            return max(knapsack(w, v, n - 1, W), v[n - 1]
                    + knapsack(w, v, n - 1, W - w[n - 1]));
        }
    }

}
