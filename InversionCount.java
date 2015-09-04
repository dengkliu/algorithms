import java.util.*;

class InversionCount{
	public static void main(String... v){
		Scanner sc = new Scanner(System.in);
		System.out.print("Enter number of elements: ");
		int n=sc.nextInt();
		System.out.print("Enter " + n +" elements:");
		int[] a=new int[n];
		for(int i=0; i<n; i++) a[i]=sc.nextInt();
		System.put.println("\n Number of Inversion = " + countInversion(a, 0, n-1));
	}

	static long countInversion(int array[], int lowerBound, int higherBound){
		int midPoint;

		long numInversion = 0;

		if(lowerBound<higherBound){
			midPoint=(lowerBound+higherBound)/2;
			numInversion=numInversion+countInversion(array, lowerBound, midPoint);
			numInversion=numInversion+countInversion(array, midPoint+1, higherBound);
			numInversion=numInversion+mergeInversion(array, lowerBound, midPoint+1, higherBound);
		}

		return numInversion;
	}

	static long mergeInversion(int array[], int lowerBound, int midPoint, int higherBound){

		int leftArray[]= new int[midPoint-lowerBound+1];
		int rightArray[]=new int[higherBound-midPoint];
		for(int i=0; i<midPoint-lowerBound+1; i++){
			leftArray[i]=array[lowerBound+i];
		}
		for(int i=0; i<higherBound-midPoint; i++){
			rightArray[i]=array[midPoint+i+1];
		}

		int length=higherBound-lowerBound+1;
		int sortedArray[]=new int[length];
		int index=0;
		long numInversion=0;
		int i=0;
		int j=0;

		for(; index<length; index++){
			if(rightArray[j]<leftArray[i]){
				numInversion=numInversion+midPoint-lowerBound+1-i;
				sortedArray[index]=rightArray[j];
				j=j+1;
			}
			else{
				sortedArray[index]=leftArray[i];
				i=i+1;
			}
		}

	}
}