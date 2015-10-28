// Project 2
// Dengke Liu
// CS:3330 Algorithm 

import java.util.*;
// This class build a tree node structure
// The tree node structure provides public interfaces to get and reset the parent and the rank of node 
// when we do union and path compression
class TreeNode{
    private int parent;
    private int rank;

    public TreeNode(int p){
        parent = p;
        rank=0;
    }

    public int parent(){return parent;}
    public int rank(){return rank;}
    public void setParent(int p){parent=p;}
    public void incrementRank(){rank=rank+1;}
}

// This class implements a Union-Find data structure using a disjoint set forest containing multiple treeNodes
class UnionFind {

    // The forest is an array of treenodes
    TreeNode[] forest;

    // constructor to initialize the forest
    // each tree has just one node as parent itself
    UnionFind(int size){
        forest = new TreeNode[size];
        for (int i=0; i<forest.length; i++){
            forest[i]=new TreeNode(i);
        }
    }

    // Union by rank
    public boolean Union_by_Rank(int x, int y){
        int x_Root = find_path_compression(x);
        int y_Root = find_path_compression(y);

        if(x_Root!=y_Root){
            link(x_Root, y_Root);
            return true;
        }else return false;
    }

    // find using path compression
    // recurisely do path compression
    public int find_path_compression(int x){
        if (forest[x].parent()!=x){
            forest[x].setParent(find_path_compression(forest[x].parent()));
        }
        return forest[x].parent();
    }
    
    // Link the root by rank
    public void link(int x_Root, int y_Root){
        TreeNode a=forest[x_Root];
        TreeNode b=forest[y_Root];

        if(a.rank()>b.rank()) b.setParent(x_Root);
        else if (a.rank()<b.rank()) a.setParent(y_Root);
        else { a.setParent(y_Root); b.incrementRank();}
    }
}

public class Maze {
    
    public static int Size; 
    public static int N;                                                                                                      
    public static int [] board; // a borad is a Size*Size array of integers
    public static Edge[] graph; // a graph is simply a set of edges
    public static HashMap<Integer, ArrayList<Integer>> connectedIntegers; // for each integer in the board, store the neighbor integers 
                                                                        // if they are in the same sets, which means the edge between them
                                                                        // has been deleted
    public static ArrayList<Integer> path; // a path holds the integers of path from 0 to Size*Szie-1
    
    public static class Edge { 
       // an Edge is a link between two Points: 
	   // For the grid graph, an edge can be defined by the integers that it seprates
	   int  left; // or top
       int  right; // or bottom
	   boolean used;     // for maze creation
	   boolean deleted;  // for maze creation

	    public Edge(int l, int r) {
           this.left=l;
           this.right=r;   
           this.used = false;
           this.deleted = false;
        }
    }

    // construct the maze with the input size
    public Maze(int size){

        Size=size;
        N=size*size;

        // initilizae the board
        board = new int[N];
        for (int i=0; i<N; i++){
            board[i]=i;
        }

        // initialize the graph
        graph = buildEdges();

        // mix up the edges thus we can randomly delete them later
        Collections.shuffle(Arrays.asList(graph));

        UnionFind mergeNodes = new UnionFind(N);

        for (Edge e : graph){
            if(mergeNodes.Union_by_Rank(e.left, e.right)){
                e.deleted=true;
            }
        }
    }

    public Edge[] buildEdges(){

        graph = new Edge[2*(N-Size)]; // there are 2*(N-Size) internal edges
        int index=0;

        // the edges that separate the boards vertically
        for (int i=0; i<N-Size; i++){
            graph[index]=new Edge(i, i+Size);
            index++;
        }

        // the edges that separate the boards horizontally
        for (int i=0; i<N-1; i++){
            if((i+1)%Size!=0){
                graph[index]=new Edge(i, i+1);
                index++;
            }
        }
        return graph;
    }

    // display the maze
    public static void displayInitBoard() {

       find_connected_Integers(); 

        System.out.println("\nInitial Configuration:");

        System.out.print("    -");

        for (int i = 0; i < Size; ++i) System.out.print("----");

        System.out.println();

        for (int i = 0; i < Size; ++i) {
            
            if (i == 0) System.out.print("Start");
            else System.out.print("    |");

            for (int j=0; j<Size; ++j) {
                if (connectedIntegers.get(i*Size+j).contains(i*Size+j+1)) System.out.print("    ");
                else {
                    if(i==Size-1 && j==Size-1) System.out.print("    End");
                    else System.out.print("   |");
                }
            }
            
            System.out.println();

            System.out.print("    -");
        
            for (int j = 0; j < Size; ++j){
                if (connectedIntegers.get(i*Size+j).contains((i+1)*Size+j)) System.out.print("    ");
                else System.out.print("----");
            }
            System.out.println();
        }
    }
    
    // this method identify for each integer if the right/left/up/bottom edges have been deleted, if they are deleted, then there is a 
    // a path from the integer to right/left/up/bottom integer, store the integer as a key and the surrounding accessible integer in an
    // array, which is the value of the key in hashmap

    public static void find_connected_Integers(){
        
        HashMap<Integer, ArrayList<Integer>> h = new HashMap<Integer,ArrayList<Integer>>();

        for (Edge e: graph){

            if (e.deleted==true){
                if (h.containsKey(e.left)) h.get(e.left).add(e.right);
                else{
                    ArrayList<Integer> values1 = new ArrayList<Integer>();
                    values1.add(e.right);
                    h.put(e.left, values1);
                }

                if (h.containsKey(e.right)) h.get(e.right).add(e.left);
                else{
                    ArrayList<Integer> values2 = new ArrayList<Integer>();
                    values2.add(e.left);
                    h.put(e.right, values2);
                }  
            }
        }
        connectedIntegers=h;
    }

    // display the maze path, if an integer is in the path array, then print a $ in the corresponding postion
    // This method is not complete since the build_path method did not function as expected
    
    //public static void displayPath(){

    //    path=build_path();

    //    }
    //}

    // the following two functions return an ArrayList of the intergers in the path
    // I think the main logic works well, but some trickly trival error somewhere

    //public static ArrayList<Integer> build_path(){

    //    ArrayList<Integer> p = new ArrayList<Integer>();
    //    find_path(p, 0);
    //    return p;
    //}

    //public static void find_path(ArrayList<Integer> p, int i){

    //    p.add(i);

    //    for(int j: connectedIntegers.get(path.get(-1))){
    //        if (path.contains(j)) continue;
    //        else {
    //            find_path(p, j);
    //            if (p.get(-1)==Size*Size-1) break;
    //            else{
    //                p.remove(-1);
    //                continue;
    //            }
    //        }
    //    }
    //}

        
    public static void main(String[] args) {

        Scanner scan = new Scanner(System.in);

        try {
            System.out.println("What's the size of your maze? ");
            Size = scan.nextInt();

            Maze maze = new Maze(Size);

            displayInitBoard();

            //System.out.println("Press any key to see the path");
            
            //try{

            //    System.in.read();

            //    displayPath(); 

            //}catch(Exception e){}         
	    }catch(Exception ex){
            ex.printStackTrace();
        }

        scan.close();
    }    
}
