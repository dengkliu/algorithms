
import java.util.*;


public class MergeSort {

	public static void main(String args[]){

		ArrayList<Integer> inputArr= new ArrayList<Integer>();

		inputArr.add(43);
		inputArr.add(32);
		inputArr.add(4);
		inputArr.add(523);
		inputArr.add(67);
		inputArr.add(45);
		inputArr.add(66);

		MergeSort mms = new MergeSort();

		ArrayList<Integer> outputArr = new ArrayList<Integer>();
		outputArr = mms.sorting(inputArr);

		for (int i=0; i<outputArr.size(); i++){
			System.out.print(outputArr.get(i));
			System.out.print(" ");
		}
	}

	public  ArrayList<Integer> sorting(ArrayList<Integer> L){

		if (L.size()==0) {return L;}
		else{
			int NumEelement = L.size()/2 + L.size()%2;

			ArrayList<Integer> A = new ArrayList<Integer>();
			ArrayList<Integer> B = new ArrayList<Integer>();

			for (int i=0; i < NumEelement; i++){A.add(L.get(i));}
			for (int i=NumEelement; i < L.size()-NumEelement; i++){B.add(L.get(i));}

			A = sorting(A);
		    B = sorting(B);

			return merge(A,B);
		}
	}

	public ArrayList<Integer> merge(List<Integer> A, List<Integer> B){
		int i=0;
		int j=0;

		ArrayList<Integer> newL = new ArrayList<Integer> ();

		for(int k=0;k<(A.size()+ B.size());k++){
			if (A.get(i)< B.get(j)){
				newL.add(A.get(i));
				i++;
			}else{
				newL.add(B.get(i));
				j++;
			}
		}
		return newL;
	}
}