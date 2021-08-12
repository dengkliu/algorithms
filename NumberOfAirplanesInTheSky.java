// https://www.lintcode.com/problem/391/
// Given an list interval, which are taking off and landing time of the flight. How many airplanes are there at most at the same time in the sky?
// Input: [(1, 10), (2, 3), (5, 8), (4, 7)]
// Output: 3
// Explanation:
// The first airplane takes off at 1 and lands at 10.
// The second ariplane takes off at 2 and lands at 3.
// The third ariplane takes off at 5 and lands at 8.
// The forth ariplane takes off at 4 and lands at 7.
// During 5 to 6, there are three airplanes in the sky.

// Use scanning line to scan through the timeline
// For starts, add 1
// For ends, substract 1
// Use heap to sort the intervals
// Time complexity O(NlogN)

 public classs Interval {
 	int start, end;
 	Interval(int start, int end) {
 		this.start = start;
 		this.end = end;
 	}
 }

 class Point {
     int time;
     int flag;

     Point(int time, int flag) {
         this.time = time;
         this.flag = flag;
     }
 }

public class Solution {
    
    /**
     * @param airplanes: An interval array
     * @return: Count of airplanes are in the sky.
     */
    public int countOfAirplanes(List<Interval> airplanes) {

        Queue<Point> heap = new PriorityQueue<>(
            new Comparator<Point>() {
                @Override
                public int compare(Point p1, Point p2) {
                    if (p1.time == p2.time) {
                        return p1.flag - p2.flag;
                    } else {
                        return p1.time - p2.time;
                    }
                }
            }
        );

        for (Interval airplane : airplanes) {

            heap.add(new Point(airplane.start, 1));
            heap.add(new Point(airplane.end, -1));
        }

        int result = 0;

        int numberOfAirplane = 0;

        while(!heap.isEmpty()) {

            Point p = heap.poll();

            numberOfAirplane += p.flag;

            result = Math.max(numberOfAirplane, result);
        }

        return result;
        
    }
}

