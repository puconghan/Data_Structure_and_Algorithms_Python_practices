import java.io.*;
import java.util.*;

class Stack{

    private List<String> stack;
    private int count;

    public Stack(){
        this.stack = new ArrayList<String>();
        this.count = 0;
    }

    public void push(String value){
        this.stack.add(value);
        this.count++;
    }

    public String pop(){
        if(this.count > 0){
            this.count--;
            return this.stack.remove(0);
        }else{
            return null;
        }
    }

    public String peel(){
        if(this.count == 0){
            return null;
        }else{
            return this.stack.get(0);
        }
    }

    public int getSize(){
        return this.count;
    }

    public static void main(String[] args){
        List<String> strList = new ArrayList<String>(Arrays.asList(args[0].split(",")));
        Stack stack = new Stack();
        for(String str : strList){
            stack.push(str);
        }
        while(stack.getSize() != 0){
            System.out.println(stack.peel());
            System.out.println(stack.pop());
        }
    }
}
