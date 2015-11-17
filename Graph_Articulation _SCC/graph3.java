import java.util.*;

class graph3 {

    private int MAX_VERTS;
    private int MAX_EDGES;
    private vertex2 vertexList[]; // list of vertices
    private int adjMat[][];       // adjacency matrix
    private int nVerts;           // current number of vertices
    private queue thequeue;
    private stack theStack;
    private int[] parent;
    private static boolean printLabel;

    private int postfn[]; 
   

    public graph3()  {                         // constructor
	this(20, 40);
    }

    public graph3(int V, int E)  {             // constructor
	MAX_VERTS = V;
	MAX_EDGES = E;

	vertexList = new vertex2[MAX_VERTS];
	parent = new int[MAX_VERTS];
                                          // adjacency matrix
	adjMat = new int[MAX_VERTS][MAX_VERTS];
	nVerts = 0;
	postfn = new int[MAX_VERTS];


	for(int j=0; j<MAX_VERTS; j++)      // set adjacency
	    for(int k=0; k<MAX_VERTS; k++)   //    matrix to 0
		adjMat[j][k] = 0;
      
	for(int j=1; j<=MAX_VERTS; j++) {     // fill VertexList
	    vertexList[nVerts++] = new vertex2("v"+j);
	}

        Random randomGenerator = new Random();
        for (int i = 0; i < MAX_EDGES; i++) {
            int v = randomGenerator.nextInt(V);
            int w = randomGenerator.nextInt(V);
            if (v != w) addEdge(v, w);
        }

    }  // end constructor

    public void addvertex(String lab){
	vertexList[nVerts++] = new vertex2(lab);
    }

    public void addEdge(int start, int end) {
	adjMat[start][end] = 1; // directed graph
    }
   
    public void displayvertex(int v) {
      if (printLabel) System.out.print(vertexList[v].label + " ");
    }
   
    public void dfs() { // depth-first search


	  System.out.println("The order of vertices in dfs traversal is: ");

	  theStack = new stack();                             
	  vertexList[0].wasVisited = true;  // begin at vertex 0 and mark it
	  displayvertex(0);                 // display it
	  parent[0] = -1;                   // vertex 0 has no parent
	  theStack.push(0);                 // push it
	  printLabel = true;
	
	  int p=1;

	  while( !theStack.isEmpty() )  {    // until stack empty,
	    	  
	    // get an unvisited vertex adjacent to stack top
	    int v = getAdjUnvisitedVertex(theStack.peek());

	    if(v == -1){
		  postfn[theStack.pop()]=p; // store the postfn of vertex v
		  p=p+1;
	    }                    // if no such vertex,
	    else {                          // if it exists,
		  vertexList[v].wasVisited = true;  // mark it
		  displayvertex(v);                 // display it
		  parent[v] = theStack.peek();
		  theStack.push(v);                 // push it
	    }
	  }  // end while

	  // stack is empty, so we're done
	  for(int j=0; j<nVerts; j++)          // reset flags
	    vertexList[j].reset();

	  System.out.println();
    }  // end dfs


    public void findSCC(){

    	System.out.println("The strongest connected component(s) is(are): ");


    	while(true){

    		int max=0;
    	    int maxV=0;
    	    boolean stop = true; // to check if all vertices are visited


    	    //for (int k=0; k<MAX_VERTS; k++){
    	   	//   System.out.print(vertexList[k].wasVisited+ " ");
    		//   System.out.println(postfn[k]);
    	    //}

    		for(int i=0; i<MAX_VERTS; i++){
    		    if (vertexList[i].wasVisited==false){
    		    	stop = false;
    		    	if (postfn[i]>=max){
    				    max=postfn[i];
    				    maxV = i;
    		        } // find the vertex with maximum postfn in remaining unvistied vertices
    		    }
    	    }

    	    //System.out.println(stop);

    	    if (stop==true) break;


    	    //System.out.print(maxV);

    	    dfs(maxV);

    	    System.out.println();
    	}
    }

    public void dfs(int s){

    	System.out.print("SCC --- ");    

    	vertexList[s].wasVisited=true;
        theStack = new stack();                    
	    displayvertex(s);                 // display it
	    theStack.push(s);                 // push it
	    printLabel = true;

	    while(!theStack.isEmpty())  {    // until stack empty

	      // get an unvisited vertex adjacent to stack top
	      int v = getAdjUnvisitedVertex_2(theStack.peek());

	      if(v == -1)                    // if no such vertex,
		    theStack.pop();
	      else {                          // if it exists,
		    vertexList[v].wasVisited = true;  // mark it
		    displayvertex(v);                 // display it
		    theStack.push(v);                 // push it
	      }
	  }  // end while
    }

    // returns an unvisited vertex adj to v
    public int getAdjUnvisitedVertex(int v) {
    	
	    for(int j=vertexList[v].nextNeighbor; j<nVerts; j++)
	      if(adjMat[v][j]==1 && vertexList[j].wasVisited==false) {
		  vertexList[v].nextNeighbor = j+1;
		  return j;
	    }
	    vertexList[v].nextNeighbor = nVerts;
	    return -1;
    }  // end getAdjUnvisitedvertex()

    public int getAdjUnvisitedVertex_2(int v){

    	for(int j=vertexList[v].nextNeighbor; j<nVerts; j++)
	      if(adjMat[j][v]==1 && vertexList[j].wasVisited==false) { // modify the adjMat[v][j] to adjMat[j][v]
		    vertexList[v].nextNeighbor = j+1;
		    return j;
	    }
	    vertexList[v].nextNeighbor = nVerts;
	    return -1;
    }

    public static void main(String[] args){

    	graph3 g1 = new graph3(20, 80);

    	g1.dfs();

    	g1.findSCC();

    	System.out.println();

    	graph3 g2 = new graph3(40, 80);

    	g2.dfs();

    	g2.findSCC();

    	System.out.println();

    	graph3 g3 = new graph3(40, 100);

    	g3.dfs();

    	g3.findSCC();

    	System.out.println();

    	graph3 g4 = new graph3(40, 200);

    	g4.dfs();

    	g4.findSCC();

    	System.out.println();

    	graph3 g5 = new graph3(40, 400);

    	g5.dfs();

    	g5.findSCC();

    	System.out.println();

    }

}  // end class graph

