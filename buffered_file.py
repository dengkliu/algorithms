class BufferedFile:
	def __init__(self, maxBufferedSize):
		self.maxBufferedSize = maxBufferedSize
		self.diskStorage = []
		self.buffer = []

	def write(self, content):
		for ch in content:
			self.buffer.append(ch)

		if len(self.buffer) == self.maxBufferedSize:
			self.flush()

	def flush(self):
		self.diskStorage.extend(self.buffer)
		# reset to empty array
		self.buffer = []