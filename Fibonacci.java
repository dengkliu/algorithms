 class Fibonacci{

 	public static long Fibonacci(int n){
 		int f1=1;
 		int f2=1;
 		int f3=1;
 		if(n==1||n==2) return 1;

	    for(int i=3; i<=n; i++){
	    	f3=f1+f2;
	    	f1=f2;
	    	f2=f3;
	    }
	    return f3;
    }

    public static void main(String[] args){
    	System.out.println(Fibonacci(39));
    } 
}



