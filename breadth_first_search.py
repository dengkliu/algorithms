# Python 普通BSF模板

# ArrayDeque is faster than linkedlist for adding elements
# Queue to store nodes while searching
queue = collections.deque()
# Set to store visited nodes
visited = set()

# 初始点入队
queue.append(0);
# 在入队的同时加到visited
visited.add(0)；

while queue:

    #弹出第一个，先入队先出队
	now = queue.popleft();

	for next in self.__findNext(now):

		# 已经在visited里面
		# 在界外
		# 其他不满足条件的，直接跳过
		if not self.__is_valid(now):
			continue

		queue.append(next);
		# 一定在入队的时候就要加入visited
		# 否则会重复入队
		visited.add(next);

# 分层遍历版本 记录到起点的distance

distance = 0;

while queue:

	# 先取这一层的size
	# queue.size()每次调用都会显示实时的size
	queueSize = len(queue)

	for i in range(queueSize):
		now = queue.popleft();

		for next in self.__find_next(now):
			# 已经在visited里面
			# 在界外
			# 其他
			if not self.__isvalid(next):
				continue

			queue.append(next)
			visited.add(next)		

	distance ++;

# 更推荐版本 记录distance到每个节点
# ArrayDeque is faster than linkedlist for adding elements
# Queue to store nodes while searching
queue = collections.deque()
# dictionary to store visited nodes to distance
visited = {} 

# 初始点入队
queue.append(0);
# 在入队的同时加到visited, 初始距离为0
visited[0] = 0

while queue:

	queueSize = len(queue)

	for i in range(queueSize):
		now = queue.poll()

		for next in self.__find_next(now):
			# 已经在visited里面
			# 在界外
			# 其他
			if not self.__isValid(next):
				continue

			queue.append(next)

			visited[next] = visited[now] + 1
