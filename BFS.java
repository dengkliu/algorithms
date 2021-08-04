// Java 普通BSF模板

Queue<Integer> queue = new LinkedList<>();
HashSet<Integer> visited = new HashSet<>();

// 初始点入队
queue.offer(0);
// 在入队的同时加到visited
visited.add(0)；

while (!queue.isEmpty()) {

	// 弹出
	int now = queue.poll();

	for (int next : findNext(now)) {

		// 已经在visited里面
		// 在界外
		// 其他
		if !isValid(next) {
			continue;
		}

		queue.offer(next);

		// 一定在入队的时候就要加入visited
		// 否则会重复入队
		visited.offer(next);

	}
}