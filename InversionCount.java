import java.util.*;

class InversionCount{

	// read the input
	public static void main(String... v){
		Scanner sc = new Scanner(System.in);
		System.out.print("Enter number of elements: ");
		int n=sc.nextInt();
		System.out.print("Enter " + n +" elements:");
		int[] a=new int[n];
		for(int i=0; i<n; i++) a[i]=sc.nextInt();
		System.put.println("\n Number of Inversion = " + countInversion(a, 0, n-1));
	}

	// An auxiliary recursive function that sorts the input arrary and return the number of inversions in the array
	static long countInversion(int array[], int lowerBound, int higherBound){
		int midPoint=0;

		long numInversion = 0;

		if(lowerBound<higherBound){
			// Inversion count will be sum of inversions in left-part, right part, and number of inversions in merging
			midPoint=(lowerBound+higherBound)/2;
			numInversion=countInversion(array, lowerBound, midPoint);
			numInversion+=countInversion(array, midPoint+1, higherBound);

			// Merge two parts
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

		while(i<=leftArray.length && j<rightArray.length){
			if (leftArray[i]<=rightArray[j]) {
				sortedArray[index]=leftArray[i];
				i++;
				index++;
			}else{
				sortedArray[index]=rightArray[j];
				j++;
				index++;

				numInversion+=midPoint-i;
			}

		}

		while(i<leftArray.length) sortedArray[index++]=leftArray[index++];
		while(j<rightArray.length) sortedArray[index++]=rightArray[index++];

		return numInversion

	}
}