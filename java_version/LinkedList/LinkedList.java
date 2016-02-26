import java.io.*;
import java.util.*;

class LinkedList{

    private Node head;
    private Node tail;

    public LinkedList(){
        this.head = null;
        this.tail = null;
    }

    public LinkedList(String value){
        this.head = new Node(value);
        this.tail = this.head;
    }

    public void insert(String value){
        if(this.head == null){
            this.head = new Node(value);
            this.tail = this.head;
        }else{
            Node newnode = new Node(value);
            this.tail.setNext(newnode);
            this.tail.getNext().setPrevious(this.tail);
            this.tail = this.tail.getNext();
        }
    }

    public boolean delete(String value){
        if(this.head == null){
            return false;
        }else{
            if(this.head.getValue().equals(value)){
                this.head = this.head.getNext();
                this.head.setPrevious(null);
                return true;
            }else if(this.tail.getValue().equals(value)){
                this.tail = this.tail.getPrevious();
                this.tail.setNext(null);
                return true;
            }else{
                Node temp = this.head;
                while(temp.getNext() != null){
                    if(temp.getValue().equals(value)){
                        temp.getPrevious().setNext(temp.getNext());
                        temp.getNext().setPrevious(temp.getPrevious());
                        return true;
                    }
                    temp = temp.getNext();
                }
                return false;
            }
        }
    }

    public void print(){
        Node temp = this.head;
        while(temp != null){
            System.out.println(temp.getValue());
            temp = temp.getNext();
        }
    }

    public static void main(String[] args){
        List<String> strList = new ArrayList<String>(Arrays.asList(args[0].split(",")));
        LinkedList list = new LinkedList();
        for(String str : strList){
            list.insert(str);
        }
        list.print();
        if(args.length == 2){
            System.out.println("Delete element: " + args[1]);
            list.delete(args[1]);
            list.print();
        }
    }
}
