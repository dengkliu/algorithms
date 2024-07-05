class LogAndQueries:
	def __init__(self):
		# query to Id
		self.queries_dict = {}
		# Word to query Ids
		self.reverted_indexes = collections.defaultdict(list)
		# Monotonic incremnting Ids
		self.query_id = 1

	def generateHash(self, words):
		counter =collections.defaultdict(int)
		for word in words:
			counter[word] += 1
		keys = list(counter.keys())
		keys.sort()
		result = []
		for word in keys:
			result.append(word)
			result.append(str(counter[word]))
		
		return "".join(result)

	def process_input(self, entry):
		# Q: hello world
		# L: hello morning world 
		entry_type, entry_content = entry.split(":")
		words = entry_content.strip().split(" ")

		if entry_type == "Q":
			query_hash = self.generateHash(words)
			if query_hash not in self.queries_dict:
				# hello1word1 -> 1
				self.queries_dict[query_hash] = self.query_id
				# hello -> 1, word -> 1
				for word in words:
					self.reverted_indexes[word].append(self.query_id)
				self.query_id += 1
		else:
			result = []
			# query Id to the words that exist in this log
			queries = collections.defaultdict(list)
			# 1 -> [hello, word]
			for word in words:
				for q_id in self.reverted_indexes[word]:
					queries[q_id].append(word)
			# rebuild each query
			for q_id in queries:
				q_hash = self.generateHash(queries[q])
				if q_hash in self.queries_dict and self.queries_dict[q_hash] == q_id:
					result.append(q_id)
			return result