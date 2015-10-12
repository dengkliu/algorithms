public class BinaryTree{
	Node root;

	public void addNode(int key, String name){
		Node newNode = new Node(key, name);

		if(root==null) root=newNode;
		else{
			Node focusNode = root;
			Node parent;
			while(true){
				parent=focusNode;
				if(key<focusNode.key){
					focusNode=focusNode.leftChild;
					if(focusNode==null){
						parent.leftChild=newNode;
						return;
					}
				}else{
					focusNode=focusNode.rightChild;
					if(focusNode==null){
						parent.rightChild=newNode;
						return;
					}

				}
			}
		}
	}

	public void inOrderTraverseTree(Node focusNode){
		if(focusNode!=null){
		inOrderTraverseTree(focusNode.leftChild);
		System.out.println(focusNode);
		inOrderTraverseTree(focusNode.rightChild);
	    }
	}

	public void preOrderTraverseTree(Node focusNode){
		if(focusNode!=null){
		System.out.println(focusNode);
		preOrderTraverseTree(focusNode.leftChild);
		preOrderTraverseTree(focusNode.rightChild);
	    }
    }

    public void postOrderTraverseTree(Node focusNode){
    	if(focusNode!=null){
    		postOrderTraverseTree(focusNode.leftChild);
    		postOrderTraverseTree(focusNode.rightChild);
    		System.out.println(focusNode);
	    }
    }

    public Node findNode(int key){
    	Node focusNode=root;
    	while(focusNode.key!=key){
    		if(key<focusNode.key){
    			focusNode=focusNode.leftChild;
    		}else{
    			focusNode=focusNode.rightChild;
    		}
    		if(focusNode==null) return null;
    	}
    	return focusNode;
    }

    public int BinaryTreeHeight(){
    	return root.height();
    }
}

public class Node{
	int key;
	String name;

	Node leftChild;
	Node rightChild;

	Node(int key, String name){
		this.key=key;
		this.name=name;
	}

	public int height(){
    	int h1=0;
    	int h2=0;
    	if(this.leftChild!=null) h1=this.leftChild.height()+1;
    	if(this.rightChild!=null) h2=this.rightChild.height()+1;
    	return(h1<h2)?h2:h1;
    }
}









