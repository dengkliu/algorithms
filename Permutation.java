import java.util.ArrayList;

public class Permutation{

	public static void  main(String agrs[]) {

		int[] list= new int[15];

		for(int i=0; i<15; i++){
			list[i]=0;
		}

		perm(15, list);

	}

	public static void perm(Integer n, int[] list){
		if (n==0) print(list);
		else{
			for(int i=0; i<15; i++){
				if(list[i]==0){
					list[i]=n;
					perm(n-1, list);
					list[i]=0; 
				}
			}
		}			
	}

	public static void print(int[] list){
		for(int i=0; i<15; i++){
			System.out.print(list[i]);
		}
		System.out.println(' ');

	}
}