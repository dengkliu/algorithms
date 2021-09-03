// https://www.lintcode.com/problem/1219

// Winter is coming! Your first job during the contest is to design a standard heater
// with fixed warm radius to warm all the houses.
// Now, you are given positions of houses and heaters on a horizontal line, 
// find out minimum radius of heaters so that all houses could be covered by those heaters.
// So, your input will be the positions of houses and heaters seperately, 
// and your expected output will be the minimum radius standard of heaters.

// Input: [1,2,3],[2]
// Output: 1
// Explanation: The only heater was placed in the position 2, 
// and if we use the radius 1 standard, then all the houses can be warmed.

// 基本想法：
// 1. 针对每个加热器 找到所有可以找它加热的房子。这样对于每个房子，需要比较这个加热器和其他加热器到房子的距离，不方便。
// 2. 针对每个房子 找到离其最近的加热器 这样才能节省加热器的距离。对于每个房子，不用考虑其他房子，只考虑它自己就好了。

// 解法
// 1. Binary search
//    针对一个target 找到数组里离它最近的一个数 可以用二分法

public class Solution {
    /**
     * @param houses: positions of houses
     * @param heaters: positions of heaters
     * @return: the minimum radius standard of heaters
     */
    public int findRadius(int[] houses, int[] heaters) {

        // O(mlog(m))
        Arrays.sort(heaters);

        int minHeatRadius = 0;

        for (int i = 0; i < houses.length; i ++) {

            int radius = getMinimumRadius(houses[i], heaters);

            minHeatRadius = Math.max(minHeatRadius, radius);
        }

        return minHeatRadius;
    }

    int getMinimumRadius(int house, int[] heaters) {

        int leftHeater = 0, rightHeater = heaters.length - 1;

        while (leftHeater + 1 < rightHeater) {

            int midHeater = leftHeater + (rightHeater - leftHeater)/2;

            if (house < heaters[midHeater]) {
                rightHeater = midHeater;
            } else {
                leftHeater = midHeater;
            }
        }

        int leftDistance = Math.abs(house - heaters[leftHeater]);
        int rightDistance = Math.abs(heaters[rightHeater] - house);

        return Math.min(leftDistance, rightDistance);
    }
}

// 2. 双指针
//    一个指针放在房子数组上，一个指针放在加热器数组上
//    对于当前房子，假如当前加热器比下一个加热器更近，那么当前加热器一定是最优的，则可以看下一个房子。
//    对于当前房子，假如下一个加热器比当前加热器更近，那么下一个加热器不一定是最优，需要继续往下看。
//    这个挺难想的


public class Solution {
    /**
     * @param houses: positions of houses
     * @param heaters: positions of heaters
     * @return: the minimum radius standard of heaters
     */
    public int findRadius(int[] houses, int[] heaters) {

        Arrays.sort(houses);
        Arrays.sort(heaters);

        int houseCnt = houses.length;
        int heaterCnt = heaters.length;

        int houseIndex = 0;
        int heaterIndex = 0;

        int minRadius = 0;

        while (houseIndex < houseCnt && heaterIndex < heaterCnt) {

            int currRadius = Math.abs(houses[houseIndex] - heaters[heaterIndex]);

            int nextRadius = heaterIndex + 1 == heaterCnt ? 
                Integer.MAX_VALUE : 
                Math.abs(houses[houseIndex] - heaters[heaterIndex + 1]);

            // 对于当前house 找到了最佳heater
            if (currRadius < nextRadius) {
                minRadius = Math.max(minRadius, currRadius);
                houseIndex ++;
                continue;
            }
            heaterIndex++;
        }

        return minRadius;
    }
}



