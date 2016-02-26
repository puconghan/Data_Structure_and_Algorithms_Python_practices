import java.io.*;
import java.util.*;

class Node{
    
    private int value;
    private Node left;
    private Node right;

    public Node(int value){
        this.value = value;
        this.left = null;
        this.right = null;
    }

    public void setValue(int value){
        this.value = value;
    }

    public int getValue(){
        return this.value;
    }

    public void setLeft(Node left){
        this.left = left;
    }

    public Node getLeft(){
        return this.left;
    }

    public void setRight(Node right){
        this.right = right;
    }

    public Node getRight(){
        return this.right;
    }
}
