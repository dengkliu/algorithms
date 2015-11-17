import java.util.*;

class graph2 {
    private int MAX_VERTS;
    private int MAX_EDGES;
    private vertex2 vertexList[]; // list of vertices
    private int adjMat[][];      // adjacency matrix
    private int nVerts;          // current number of vertices
    private queue thequeue;
    private stack theStack;
    private int[] parent;
    private static boolean printLabel;

    private int alpha []; // for finding the articulation point
    private int beta []; // for finding the articulation point
    private int predfn[]; // store the order of the vertices vistied
    private int rootdegree; 


    public graph2()  {                         // constructor
    	this(20, 40);
    }

    public graph2(int V, int E)  {             // constructor
    	
      MAX_VERTS = V;
    	MAX_EDGES = E;

    	vertexList = new vertex2[MAX_VERTS];
    	parent = new int[MAX_VERTS];
                                          // adjacency matrix
    	adjMat = new int[MAX_VERTS][MAX_VERTS];

      alpha = new int[MAX_VERTS];
      beta = new int[MAX_VERTS];
      predfn = new int[MAX_VERTS];

    	nVerts = 0;

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

    } // end constructor

    public void addvertex(String lab){
      vertexList[nVerts++] = new vertex2(lab);
    }

    public void addEdge(int start, int end) {
      adjMat[start][end] = 1;
      adjMat[end][start] = 1;   // undirected graph only
    }

   
   public void displayvertex(int v) {
      if (printLabel) System.out.print(vertexList[v].label + " ");
   }
   
  public void dfs() { // depth-first search

      System.out.println("The visiting order of vertices in dfs traversal: ");

    	theStack = new stack();                             
    	vertexList[0].wasVisited = true;  // begin at vertex 0 and mark it
    	displayvertex(0);                 // display it
    	parent[0] = -1;                   // vertex 0 has no parent
    	theStack.push(0);                 // push it
    	printLabel = true;

      int p = 1;
      predfn[0]=1; // the vertexList[0] is the first one to be visted

    	while( !theStack.isEmpty() )  {    // until stack empty,
    	   // get an unvisited vertex adjacent to stack top
    		int v = getAdjUnvisitedVertex( theStack.peek() );

        if(v == -1){
          theStack.pop();
        }                    // if no such vertex,
    		else {                          // if it exists,
    		  vertexList[v].wasVisited = true;  // mark it
    		  displayvertex(v);                 // display it
    		  parent[v] = theStack.peek();
    		  theStack.push(v);                 // push it
          p=p+1;
          predfn[v]=p;
    	  }
	    }  // end while

      System.out.println();

	    // stack is empty, so we're done
	    for(int j=0; j<nVerts; j++)          // reset flags
	        vertexList[j].reset();
  }  // end dfs
   
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


  // find the articulation points
  public void findArtPoints(){

      // initialize beta[] and alpha
      for(int i=0; i<MAX_VERTS; i++){
        alpha[i]=predfn[i];
        beta[i]=predfn[i];
      }

      int count=0;

      dfs(0);

      System.out.println("The articulation points include: ");

      for (int i=0; i<MAX_VERTS; i++){
        if (vertexList[i].isArtpoint==true){
          System.out.print(vertexList[i].label + " ");
        }
      }

      System.out.println();
  }

  public void dfs(int v){
      vertexList[v].wasVisited=true;
      vertexList[v].isArtpoint=false;
      for (int j=0; j<nVerts; j++){
        if (parent[j]==v) {
          dfs(j);
          if (v==0) {
            rootdegree=rootdegree+1;
            if (rootdegree==2) vertexList[v].isArtpoint=true;
          }else{
            beta[v]=(beta[v]>beta[j])? beta[j]:beta[v];
            if (beta[j]>=alpha[v]) vertexList[v].isArtpoint=true;
          }
        }else{
          if (adjMat[v][j]==1) beta[v]=(beta[v]>alpha[j])? beta[v]:alpha[j];
        }
      }
  }  


  public static void main(String[] args){

    graph2 g1 = new graph2(20, 80);

    g1.dfs();

    g1.findArtPoints();

    System.out.println();

    graph2 g2 = new graph2(40, 80);

    g2.dfs();

    g2.findArtPoints();

    System.out.println();

    graph2 g3 = new graph2(40, 100);

    g3.dfs();

    g3.findArtPoints();

    System.out.println();

    graph2 g4 = new graph2(40, 200);

    g4.dfs();

    g4.findArtPoints();

    System.out.println();

    graph2 g5 = new graph2(40, 400);

    g5.dfs();

    g5.findArtPoints();
  }

}  // end class graph

