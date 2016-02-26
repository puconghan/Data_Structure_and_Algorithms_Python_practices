import java.io.*;
import java.util.*;

class Queue{

    private String[] queue;
    private int count;

    public Queue(){
        this.count = 0;
    }

    public void enqueue(String value){
       if(this.count == 0){
            this.queue = new String[1];
            this.queue[0] = value;
            this.count++;
        }else{
            String[] temp = new String[count];
            for(int i=0; i<count; i++){
                temp[i] = this.queue[i];    
            }
            this.queue = new String[count+1];
            for(int i=0; i<count; i++){
                this.queue[i] = temp[i];
            }
            this.count++;
            this.queue[count-1] = value;
        }
    }

    public String dequeue(){
        if(count > 0){
            String[] temp = new String[count];
            for(int i=0; i<count; i++){
                temp[i] = this.queue[i];    
            }
            this.queue = new String[count-1];
            for(int i=1; i<count; i++){
                this.queue[i-1] = temp[i];
            }
            this.count--;
            return temp[0];
        }else{
            return null;
        }
    }

    public int getSize(){
        return this.count;
    }

    public static void main(String[] args){
        List<String> strList = new ArrayList<String>(Arrays.asList(args[0].split(",")));
        Queue queue = new Queue();
        for(String str : strList){
            queue.enqueue(str);
        }
        while(queue.getSize() != 0){
            System.out.println(queue.dequeue());
        }
    }
}
