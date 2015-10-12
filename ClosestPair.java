import java.awt.geom.Point2D;
import java.util.Arrays;
import java.util.Comparator;

public class Test{
  public static void main(String[] args){
      Point[] points = new Point[] { new Point(2, 7), new Point(4, 13), new Point(5, 8),new Point(10, 5),new Point(14, 9),new Point(15, 5), new Point(17, 7), new Point(19, 10), new Point(22, 7), new Point(25, 10), new Point(29, 14), new Point(30, 2) };

      ClosestPair cl = new ClosestPair(points);
  }
}

class ClosestPair{
  private Point p1,p2;
  private double shortestDistance = Double.POSITIVE_INFINITY;
  private int N;

  public ClosestPair(Point[] points){
      N = points.length;

      if(N<=1)
          return;

      // sort by x-coordinate 
      Point[] pointsByX = new Point[N];
      for(int i = 0; i< N; i++)
          pointsByX[i] = points[i];

      Arrays.sort(pointsByX,new Comparator<Point>(){
               public int compare(Point p, Point q) {
              if (p.getX() < q.getX()) return -1;
                  if (p.getX() > q.getX()) return +1;
              return 0;
            }
        });
      

      // check for identical points
        for (int i = 0; i < N-1; i++) {
            if (pointsByX[i].equals(pointsByX[i+1])) {
                shortestDistance = 0.0;
                p1 = pointsByX[i];
                p2 = pointsByX[i+1];
                displayShortestPoints();
                displayShortestDistance();
                return;
            }
        }

      // used for debug
      // displayPoints(pointsByX);

      Point[] pointsByY = new Point[N];
      for(int i=0; i<N; i++)
          pointsByY[i] = pointsByX[i];

      //auxiliary array
      Point[] temp = new Point[N];

      System.out.println("");
      System.out.println("shortest distance: "+closest(pointsByX, pointsByY, temp, 0, N-1));

      displayShortestPoints();
  }

  // find closest pair of points in pointsByX[lo..hi]
    // precondition:  pointsByX[lo..hi] and pointsByY[lo..hi] are the same sequence of points
    // precondition:  pointsByX[lo..hi] sorted by x-coordinate
    // postcondition: pointsByY[lo..hi] sorted by y-coordinate
  public double closest(Point[] pointsByX, Point[] pointsByY, Point[] temp, int lowBound, int highBound){
      if (highBound<=lowBound)
          return Double.POSITIVE_INFINITY;

          
      int mid = (lowBound + highBound)/2;
      Point median = pointsByX[mid];
      System.out.println("median: "+median.getX()+" "+median.getY());

      double d1 = closest(pointsByX,pointsByY,temp,lowBound,mid);
      double d2 = closest(pointsByX,pointsByY,temp,mid+1,highBound);
      double d = Math.min(d1,d2);


      //System.out.println("d: "+d);

      // merge back so that pointsByY[lo....hi] are sorted by y-coordinate
      // remember only from index lowBound to index highBound is sorted
      merge(pointsByX, pointsByY, lowBound, mid, highBound);

      // temp[0...k-1] = sequence of points closer than delta, sorted by y-coordinate
      int k = 0;
      int i ;
      for(i = lowBound; i<=highBound; i++)
          if(Math.abs(pointsByY[i].getY() - median.getY())<d){
              temp[k] = pointsByY[i];
              k++;
          }

      // compare each point to its neighbors with y-coordinate closer than d
      for(i = 0; i < k; i++){
          for(int j=i+1; (j<k)&&(temp[j].getY()-temp[i].getY()<d); j++){
              double distance = temp[i].distanceTo(temp[j]);
              if(distance<d)
                  d = distance;
                  if(distance<shortestDistance){
                      shortestDistance = d;
                      p1 = temp[i];
                      p2 = temp[j];
                  }
          }
      }

      return d;
  }

  // merge pointsByX(low...mid) and pointsByX(mid+1...high) back so that pointsByY[lo....hi] are sorted by y-coordinate
  private void merge(Point[] pointsByX, Point[] pointsByY, int lowBound, int mid, int highBound){

      displayPoints(pointsByX);
      displayPoints(pointsByY);
      System.out.println("lb: "+lowBound+" hb: "+highBound);


      for(int i=lowBound; i<=highBound; i++){
          pointsByY[i] = pointsByX[i];
      }


      displayPoints(pointsByY);

      //Only sort pointsByY from lowBound to highBound
      //Cannot sort the whole array because the later calculation only uses part of the array
      Arrays.sort(pointsByY, lowBound, highBound, new Comparator<Point>(){
               public int compare(Point p, Point q) {
              if (p.getY() < q.getY()) return -1;
                  if (p.getY() > q.getY()) return +1;
              return 0;
            }
        });
      displayPoints(pointsByY);

        System.out.println("");
  }

  public void displayPoints(Point[] points){
      for(int i = 0; i < points.length; i++)
          System.out.print("["+points[i].getX()+","+points[i].getY()+"]  ");

      System.out.println("");
  }

  public void displayPoint(Point p){
      System.out.println("["+p.getX()+","+p.getY()+"]");
  }

  public void displayShortestDistance(){
      System.out.println("shortest distance: "+shortestDistance);
  }

  public void displayShortestPoints(){
      System.out.println("p1: ["+p1.getX()+","+p1.getY()+"]"+"  p2: ["+p2.getX()+","+p2.getY()+"]");
  }
}

class Point extends Point2D.Double{

  public Point(double x, double y){
      super(x,y);
  }

  public void display(){
      System.out.println("["+x+","+y+"]");
  }

  public boolean equals(Point p){
      return this.x==p.getX()&&this.y==p.getY();
  }

  public double distanceTo(Point p){
      return Math.hypot(  (this.x-p.getX()) ,  (this.y-p.getY()) );
  }
}