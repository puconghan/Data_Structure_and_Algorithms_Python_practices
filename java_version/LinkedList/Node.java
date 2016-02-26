import java.io.*;
import java.util.*;

class Node{

    private String value;
    private Node next;
    private Node previous;
    
    public Node(){
        this.value = null;
        this.next = null;
        this.previous = null;
    }
    
    public Node(String value){
        this.value = value;
        this.next = null;
        this.previous = null;
    }

    public Node getNext(){
        return this.next;
    }

    public Node getPrevious(){
        return this.previous;
    }

    public String getValue(){
        return this.value;
    }

    public void setValue(String value){
        this.value = value;
    }

    public void setNext(Node next){
        this.next = next;
    }

    public void setPrevious(Node previous){
        this.previous = previous;
    }
}
