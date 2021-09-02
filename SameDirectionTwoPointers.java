int start = 0, end = 0;

for (; start < A.length; start++) {

	while(end < A.length && !isValid(start, end)) {
		end ++;
	}

	if (isValid(start, end)) {
		// deal with start and end pair
	}
}