end = 0

# enumrate the end
for start in range(n):
	while end < n and !self.isValid(start, end):
		end = end + 1

	if self.isValid(start, end):
		# deal with the start and end pair