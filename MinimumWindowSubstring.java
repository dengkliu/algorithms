// https://www.lintcode.com/problem/32

// Given two strings source and target. 
// Return the minimum substring of source which contains each char of target.

// If there is no answer, return "".
// You are guaranteed that the answer is unique.
// target may contain duplicate char, while the answer need to contain at least the same number of that char.
// 0 <= len(source) <= 1000000<=len(source)<=100000
// 0<=len(target)<=100000

// 思路 - 字符在substring出现的次数 大于 字符在target中出现的次数
// 先用hashmap统计target中所有字符出现的次数
// 再用双指针来扫原数组
// 以每个index位置作为左端点分组



public class Solution {
    /**
     * @param source : A string
     * @param target: A string
     * @return: A string denote the minimum window, return "" if there is no such a string
     */
    public String minWindow(String source , String target) {

        if (source == null || source.length() == 0) {
            return "";
        }

        // 先求出在target sting中每个字母对应出现的次数
        Map<Character, Integer> countOfCharsInTarget = new HashMap<>();

        for (int i = 0; i < target.length(); i ++) {
            int num = countOfCharsInTarget.getOrDefault(target.charAt(i), 0);
            num ++;
            countOfCharsInTarget.put(target.charAt(i), num);
        }
        
        int end = 0;
        // 需要一个变量记录当前有多少字母被cover到了
        // 总共的unique的字母是之前hashmap的size
        // 每当我们cover了所有字母 我们就找到了一个满足条件的string
        int numOfCharsCoverred = 0;
        
        // 需要一个变量记录当前最短的满足条件的string的长度
        // 根据这个长度更新我们的结果
        int minimumLength = Integer.MAX_VALUE;
        String result = "";

        Map<Character, Integer> countOfCharsInSource = new HashMap<>();

        for (int start = 0; start < source.length(); start ++) {

            while (end < source.length() && numOfCharsCoverred < countOfCharsInTarget.size()) {

                // 如果当前这个字母并不存在于target中，直接移动end到下一个
                if (!countOfCharsInTarget.containsKey(source.charAt(end))) {
                    end ++;
                    continue;
                }

                int num = countOfCharsInSource.getOrDefault(source.charAt(end), 0);
                num ++;
                countOfCharsInSource.put(source.charAt(end), num);

                // 加了1之后假如等于target中出现的次数
                // 那这个字母就被cover了
                if (num == countOfCharsInTarget.get(source.charAt(end))) {
                    numOfCharsCoverred++;
                }

                end ++;
            }

            // 有可能end到头了还是没有找到满足条件的 那就直接跳出for循环了
            // 因为接下来的start也没必要看了
            if (end == source.length() && numOfCharsCoverred < countOfCharsInTarget.size()) {
                break;
            }

            // 如果找到了更小的，那就更新结果
            if (end - start < minimumLength) {
                result = source.substring(start, end);
                minimumLength = end - start;
            }

            // 把start移除window
            // 假如start是target中的一个char的话，更新它的次数
            // 假如现在正好cover 那就暂时不能cover了
            if (countOfCharsInSource.containsKey(source.charAt(start))) {
                int num = countOfCharsInSource.get(source.charAt(start));
                if (num == countOfCharsInTarget.get(source.charAt(start))) {
                    numOfCharsCoverred--;
                }
                num--;
                countOfCharsInSource.put(source.charAt(start), num);
            }
        }

        return result;

    }
}