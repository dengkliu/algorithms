// https://www.lintcode.com/problem/1849/
// There is a bookstore. On the next n days, customer[i] will arrive on the i-th day and leave at the end of that day.
// However, the bookstore owner's temper is sometimes good but sometimes bad. We use an array of grumpy to indicate his temper is good or bad every day. 
// If grumpy[i] = 1, it means that the owner's temper is very bad on the day of i. If grumpy[i] = 0, it means that the owner has a good temper on the first day.
// If the owner of the bookstore has a bad temper one day, it will cause all customers who come on that day to give bad reviews to the bookstore. 
// But if one day you have a good temper, then all customers will give the bookstore favorable comments on that day.
// The boss wanted to increase the number of people who gave favorable comments to the bookstore as much as possible and came up with a way. 
// He can keep a good temper for XX days in a row. But this method can only be used once.
// So how many people in this bookstore can give favorable comments to the bookstore when they leave on this n day?

// 1 <= X <= customers.length <= grumpy.length <= 20000
// 0 <= customers[i] <= 100
// 0 <= grumpy[i] <= 1

// It is 10^4, so got to be O(N) or even better time complexity

// Maintian a fixed size sliding window.

public class Solution {
    /**
     * @param customers: the number of customers
     * @param grumpy: the owner's temper every day
     * @param X: X days
     * @return: calc the max satisfied customers
     */
    public int maxSatisfied(int[] customers, int[] grumpy, int X) {
       
       if (grumpy == null || grumpy.length == 0) {
           return 0;
       }

       int daysCnt = grumpy.length;

       int totalSatisfied = 0;

       for (int i = 0; i < daysCnt; i ++) {
           if (i < X) {
               totalSatisfied += customers[i];
           } else {
               totalSatisfied += customers[i] * (1 - grumpy[i]);
           }
       }

       int maxSatisfied = totalSatisfied;
       
       System.out.println(maxSatisfied);

       for (int end = X; end < daysCnt; end ++) {
           // 对于当前end
           // 假如当前end对应的心情是1，那现在可以加上
           totalSatisfied += customers[end] * grumpy[end];
           // 对于要去掉的start，假如start对于的心情是 1，那只能减去
           totalSatisfied -= customers[end - X] * grumpy[end - X];

           maxSatisfied = Math.max(maxSatisfied, totalSatisfied);
       }
       
       return maxSatisfied;
    }

}