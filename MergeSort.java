public class Solution {


	public void sortIntegers(int[] A) {
		if (A == null || A.length == 0) {
			return;
		}

		// 用一个数组去存放中间的结果
		// 一边merge一边把结果先写在这个数组里面
		// 最后再写回到A数组中
		int[] temp = new int[A.length];

		mergeSort(A, 0, A.length -1, temp);
	}

	private void mergeSort(int[] A, int start, int end, int[] temp) {

		if (start >= end) {
			return;
		}

		// 处理左半区间
		mergeSort(A, start, (start + end)/2, temp);
		// 处理右半区间
		mergeSort(A, (start + end)/2 + 1, end, temp);

		// 合并
		merge(A, start, end, temp);
	}

	private void merge(int[] A, int start, int end, int[] temp) {

		int middle = (start + end)/2;
		int left = start;
		int right = middle + 1;

		int index = 0;

		while (left <= middle && right <= end) {

			if (A[left] > A[right]) {
				temp[index] = A[right];
				index ++;
				right ++;
			} else {
				temp[index] = A[left];
				index ++;
				left ++;
			}
		}

		while (left <= middle) {
			temp[index] = A[left];
			index ++;
			left ++;
		}

		while (right <= end) {
			temp[index] = A[right];
			index++;
			right++;
		}

		for (int i = start; i <= end; i ++) {
			A[i] = temp[i];		}
	}
}
