class UnionFind {

    // Use a hashmap to store the father for each node
    Map<Integer, Integer> father;
    // Use a hashmap to track the size of a set
    Map<Inetger, Integer> sizeOfSet;
    int numOfSets;
    // Use a hashmap to record all elements in the set
    Map<Integer, Set<Integer>> setElements;


    public UnionFind() {
        father = new HashMap<>();
        sizeOfSet = new HashMap<>();
        setElements = new HashMap<>();
        numOfSets = 0;
    }

    void add(int num) {

        if (father.containsKey(num)) {
            return;
        }

        father.put(num, null);
        sizeOfSet.put(num, 1);
        setElements.put(num, new HashSet<>().add(num));
        numOfSets++;
    }

    // find the set that this number belongs to
    // A set is identified by the root
    int find(int num) {
        
        int root = num;

        // move upward to the root
        while(father.get(root) != null) {
            root = father.get(root);
        }

        // Path compression! Make it real O(1)
        while (num != root) {
            int originalFather = father.get(num);
            father.put(num, root);
            num = originalFather;
        }

        return root;
    }

    boolean isConnected(int num1, int num2) {

        return find(num1) == find(num2);
    }

    void merge(int num1, int num2) {

        int root1 = find(num1);
        int root2 = find(num2);

        if (root1 != root2) {
            father.put(root1, root2);
        }

        sizeOfSet.put(root2, sizeOfSet.get(root1) + sizeOfSet.get(root2));

        setElements.get(root2).addAll(setElements.get(root1));
        numOfSets--;
    }
}
