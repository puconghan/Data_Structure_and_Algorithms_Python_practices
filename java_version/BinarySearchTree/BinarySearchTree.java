import java.io.*;
import java.util.*;

class BinarySearchTree{

    private Node root;

    public BinarySearchTree(){
        this.root = null;
    }

    public BinarySearchTree(int value){
        this.root = new Node(value);
    }
    
    public boolean search(int value){
        if(this.root == null){
            return false;
        }else{
            return _search(value, this.root);
        }
    }

    public boolean _search(int value, Node leaf){
        if(leaf == null){
            return false;
        }else if(leaf.getValue() == value){
            return true;
        }else if(value < leaf.getValue()){
            return _search(value, leaf.getLeft());
        }else if(value > leaf.getValue()){
            return _search(value, leaf.getRight());
        }else{
            return false;
        }
    }

    public void insert(int value){
        if(this.root == null){
            this.root = new Node(value);
        }else{
            _insert(value, this.root);
        }
    }

    private void _insert(int value, Node leaf){
        if(value < leaf.getValue()){
            if(leaf.getLeft() == null){
                leaf.setLeft(new Node(value));
            }else{
                _insert(value, leaf.getLeft());
            }
        }else{
            if(leaf.getRight() == null){
                leaf.setRight(new Node(value));
            }else{
                _insert(value, leaf.getRight());
            }
        }
    }

    public void delete(int value){
        this.root = _delete(value, this.root);
    }

    private Node _delete(int value, Node leaf){
        if(leaf == null){
            return null;
        }else{
            if(leaf.getValue() == value){
                if(leaf.getLeft() == null && leaf.getRight() == null){
                    leaf = null;
                }else if(leaf.getLeft() != null && leaf.getRight() == null){
                    leaf = leaf.getLeft();
                }else if(leaf.getLeft() == null && leaf.getRight() != null){
                    leaf = leaf.getRight();
                }else{
                    Node successor = leaf.getLeft();
                    Node parent = null;
                    while(successor != null && successor.getRight() != null){
                        parent = successor;
                        successor = successor.getRight();
                    }
                    leaf.setValue(successor.getValue());
                    if(parent != null){
                        parent.setRight(null);
                    }else{
                        leaf.setLeft(null);
                    }
                }
            }else if(value < leaf.getValue()){
                leaf.setLeft(_delete(value, leaf.getLeft()));
            }else{
                leaf.setRight(_delete(value, leaf.getRight()));
            }
            return leaf;
        }
    }

    public int treeSize(){
        return _treeSize(this.root);
    }

    private int _treeSize(Node leaf){
        if(leaf == null){
            return 0;
        }else{
            return _treeSize(leaf.getLeft()) + 1 + _treeSize(leaf.getRight());
        }
    }

    public int treeDepth(){
        return _treeDepth(this.root);
    }

    private int _treeDepth(Node leaf){
        if(leaf == null){
            return 0;
        }else{
            return Math.max(_treeDepth(leaf.getLeft()), _treeDepth(leaf.getRight())) + 1;
        }
    }

    public int getMax(){
        if(this.root == null){
            return 0;
        }
        Node temp = this.root;
        while(temp.getRight() != null){
            temp = temp.getRight();
        }
        return temp.getValue();
    }

    public int getMin(){
        return _getMin(this.root);
    }

    public int _getMin(Node leaf){
        if(leaf == null){
            return 0;
        }else{
            if(leaf.getLeft() != null){
                return _getMin(leaf.getLeft());
            }else{
                return leaf.getValue();
            }
        }
    }

    public void BreadFirstTraversal(){
        if(this.root != null){
            List<Node> queue = new ArrayList<Node> ();
            queue.add(this.root);
            List<Node> output = new ArrayList<Node> ();
            while(queue.size() > 0){
                Node curr = queue.remove(0);
                output.add(curr);
                if(curr.getLeft() != null)
                    queue.add(curr.getLeft());
                if(curr.getRight() != null)
                    queue.add(curr.getRight());
            }
            System.out.print("BFS Traversal Result: ");
            for(int i=0; i<output.size(); i++){
                System.out.print(String.valueOf(output.get(i).getValue()) + " ");
            }
            System.out.println();
        }
    }

    public void DepthFirstTraversal(){
        if(this.root != null){
            List<Node> stack = new ArrayList<Node> ();
            stack.add(this.root);
            List<Node> output = new ArrayList<Node> ();
            while(stack.size() > 0){
                Node curr = stack.remove(stack.size()-1);
                output.add(curr);
                if(curr.getLeft() != null)
                    stack.add(curr.getLeft());
                if(curr.getRight() != null)
                    stack.add(curr.getRight());
            }
            System.out.print("DFS Traversal Result: ");
            for(int i=0; i<output.size(); i++){
                System.out.print(String.valueOf(output.get(i).getValue()) + " ");
            }
            System.out.println();
        }
    }

    public void printlevel(Node leaf, int level){
        if(level == 0){
            System.out.println(leaf.getValue());
        }else{
            if(leaf.getLeft() != null){
                printlevel(leaf.getLeft(), level-1);
            }
            if(leaf.getRight() != null){
                printlevel(leaf.getRight(), level-1);
            }
        }
    }

    public void printDeepestLevel(Node leaf){
        List<Node> queueone = new ArrayList<Node> ();
        List<Node> queuetwo = new ArrayList<Node> ();
        List<Integer> printlist = new ArrayList<Integer> ();
        queueone.add(leaf);
        while(queueone.size() > 0){
            Node curr = queueone.remove(0);
            if(curr.getLeft() != null){
                queuetwo.add(curr.getLeft());
            }
            if(curr.getRight() != null){
                queuetwo.add(curr.getRight());
            }
            if(queueone.size() == 0){
                if(queuetwo.size() != 0){
                    printlist = new ArrayList<Integer> ();
                    for(Node node : queuetwo){
                        queueone.add(node);
                        printlist.add(node.getValue());
                    }
                    queuetwo = new ArrayList<Node> ();
                }else{
                    System.out.print("Deepest level: ");
                    for(Integer i : printlist){
                        System.out.print(String.valueOf(i) + " ");
                    }
                    System.out.println();
                }
            }
        }
    }

    public static void main(String[] args){
        List<String> strList = new ArrayList<String>(Arrays.asList(args[0].split(",")));
        List<Integer> intList = new ArrayList<Integer>();
        for(String str : strList){
            intList.add(Integer.parseInt(str));
        }
        BinarySearchTree tree = new BinarySearchTree();
        for(Integer i : intList){
            tree.insert(i);
        }
        System.out.println("Tree size: " + String.valueOf(tree.treeSize()));
        System.out.println("Tree depth: " + String.valueOf(tree.treeDepth()));
        tree.printDeepestLevel(tree.root);
        tree.BreadFirstTraversal();
        tree.DepthFirstTraversal();
        if(args.length == 2){
            System.out.println("Searching: " + args[1]);
            Integer target = Integer.parseInt(args[1]);
            System.out.println(tree.search(target));
        }
        if(args.length == 3){
            System.out.println("Deleting: " + args[1]);
            tree.delete(Integer.parseInt(args[1]));
            System.out.println("Tree size: " + String.valueOf(tree.treeSize()));
            System.out.println("Searching: " + args[2]);
            System.out.println(tree.search(Integer.parseInt(args[2])));
        }
    }
}
