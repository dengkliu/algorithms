public class Solution {

	public void sort(int[] A) {

		quickSort(A, 0, A.length -1);

		return;

	}

	void quickSort(int[] A, int start, int end) {

		if (start >= end) {
			return;
		}
		
		// 每次选择以中间这个数作为pivot
		// 目的是把所有小于这个pivot的放在左边
		// 所有大于这个pivot的放在右边
		int mid = (start + end)/2;
		int pivot = A[mid];
		
		// 这种交换可以通过双指针实现
		int left = start, right = end;

		while (left <= right) {
			
                        // 找到第一个大于等于pivot的数
			while (left <=right && A[left] < pivot) {
				left ++;
			}
                        // 找到第一个小于等于pivot的数
			while (left <= right && A[right] > pivot) {
				right --;
			}

			// swap
			if (left <= right) {
				int temp = A[left];
				A[left] = A[right];
				A[right] = left;

				left ++;
				right --;
			}
		}
		
		// 然后分别quick sort 左边和右边
		quickSort(A, start, left);
		quickSort(A, right, end);
	}

}
