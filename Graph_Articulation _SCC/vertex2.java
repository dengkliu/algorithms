
public class vertex2 {
	   public String label;        // label (e.g. "A")
	   public boolean wasVisited;
	   public int nextNeighbor;
	   public boolean isArtpoint;
	   
	   public vertex2(String lab) {  // constructor
	      label = lab;
	      wasVisited = false;
	      nextNeighbor = 0;
	   }
	   
	   public void reset() {
		  wasVisited = false;
		  nextNeighbor = 0;
	   }

}
