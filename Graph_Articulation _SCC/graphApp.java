public class graphApp {
		
    public static void main(String[] args) {
	graph2 theGraph = new graph2(20, 50);
		      
	System.out.println(theGraph);
		      
	System.out.print("\nBFS Visits: ");
	theGraph.bfs();             // breadth-first search
	System.out.println("\n  "+theGraph.displayTree());
		      
	System.out.print("DFS Visits: ");
	theGraph.dfs();             // depth-first search
	System.out.println("\n  "+theGraph.displayTree());
		    
	//System.out.println("Using backtrackDFS to find longest paths.");
	//theGraph.longestPaths();             // backtrack depth-first search
		      
    }  // end main
		   
}  // end class GraphApp

