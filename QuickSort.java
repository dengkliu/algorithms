public class Solution {

	public void sort(int[] A) {

		quickSort(A, 0, A.length -1);

		return;

	}

	void quickSort(int[] A, int start, int end) {

		if (start >= end) {
			return;
		}

		int mid = (start + end)/2;

		int pivot = A[mid];

		int left = start, right = end;

		while (left <= right) {

			while (left <=right && A[left] < pivot) {
				left ++;
			}

			while (left <= right && A[right] > pivot) {
				right --;
			}

			if (left <= right) {
				int temp = A[left];
				A[left] = A[right];
				A[right] = left;

				left ++;
				right --;
			}
		}

		quickSort(A, start, left);
		quickSort(A, right, end);
	}

}