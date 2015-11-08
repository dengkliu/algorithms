public class PermutationofString{

  public static void permute1(String input){
    int inputLength = input.length();
    boolean[ ] used = new boolean[ inputLength ];
    StringBuffer outputString = new StringBuffer();
    Char[ ] in = input.toCharArray( );

    doPermute ( in, outputString, used, inputLength, 0 );
  }



  public static void doPermute(char[ ] in, StringBuffer outputString, boolean[ ] used, int inputlength, int level){
     if( level == inputLength) {
      System.out.println ( outputString.toString());  
      return;
     }

    for( int i = 0; i < inputLength; ++i ){
      if( used[i] ) continue;
      outputString.append( in[i] );      
      used[i] = true;       
      doPermute( in,   outputString, used, length, level + 1 );       
      used[i] = false;
      outputString.setLength(outputString.length() - 1 );   
    }
 }

  public static void permute2(String s){permute2("", s);}

  private static void permute2(String perfix, String s){
    int N=s.length();
    char[] a = new char[N];
    if (N==0) System.out.println(prefix)
    else {
      for(int i=0; i<N; i++) permute2(prefix+s.charAt(i), s.substring(0, i)+s.substring(i+1, N));
    }
  } 
  
}

