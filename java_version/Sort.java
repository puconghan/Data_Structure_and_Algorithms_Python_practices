import java.io.*;
import java.util.*;

class Sort{

    private int[] list;

    public Sort(int[] list){
        this.list = list;
    }

    public void sort(String type){
        if(type.equalsIgnoreCase("quicksort")){
            System.out.println("Using Quick Sort");
            quicksort(0, list.length - 1);
        } else if(type.equalsIgnoreCase("mergesort")){
            System.out.println("Using Merge Sort");
            mergesort(0, list.length - 1);
        } else if(type.equalsIgnoreCase("heapsort")){
            System.out.println("Using Heap Sort");
            heapsort();
        }
    }

    /**
     * Divide-and-Conquer algorithm
     * Average run time O(n*log(n))
     * Worst case run time O(n^2)
     * To avoid worst case run time, select middle element as the pivot
     **/
    public void quicksort(int low, int high){
        int i = low;
        int j = high;
        int pivot = list[low + (high - low) / 2];
        while (i <= j){
            while(list[i] < pivot){
                i++;
            }
            while(list[j] > pivot){
                j--;
            }
            if(i <= j){
                swap(i, j);
                i++;
                j--;
            }
        }
        if(low < j)
            quicksort(low, j);
        if(high > i)
            quicksort(i, high);
    }

    /**
     * Divide-and-Conquer algorithm
     * Stable sorting routine with guaranteed O(n*log(n)) efficiency
     **/
    public void mergesort(int low, int high){
        if(low < high){
            int middle = low + (high - low) / 2;
            mergesort(low, middle);
            mergesort(middle + 1, high);
            mergeparts(low, middle, high);
        }
    }

    private void mergeparts(int low, int middle, int high){
        int[] templist = new int[list.length];
        for(int i=low; i<=high; i++){
            templist[i] = list[i];
        }
        int i = low;
        int j = middle + 1;
        int k = low;
        while(i <= middle && j <= high){
            if(templist[i] <= templist[j]){
                list[k] = templist[i];
                i++;
            }else{
                list[k] = templist[j];
                j++;
            }
            k++;
        }
        while(i <= middle){
            list[k] = templist[i];
            k++;
            i++;
        }
        while(j <= high){
            list[k] = templist[j];
            k++;
            j++;
        }
    }

    /**
     * Comparison based sorting technique based on Binary Heap data structure.
     * Average run time O(n*log(n))
     **/
    public void heapsort(){
        int size = list.length - 1;
        int leastparent = size / 2;
        for(int i=leastparent; i >= 0; i--){
            movedown(i, list.length-1);
        }
        for(int i=list.length-1; i >= 0; i--){
            swap(0, i);
            movedown(0, i-1);
        }
    }

    private void movedown(int parent, int last){
        int child = parent * 2 + 1;
        while (child <= last){
            if(child < last && list[child] < list[child+1]){
                child+=1;
            }
            if(list[child] > list[parent]){
                swap(child, parent);
                parent = child;
                child = child * 2 + 1;
            }else{
                break;
            }
        }
    }

    private void swap(int i, int j){
        int temp = list[i];
        list[i] = list[j];
        list[j] = temp;
    }

    private void printList(){
        System.out.println("Printing list:");
        for(int i=0; i<list.length; i++){
            System.out.println(list[i]);
        }
    }
    
    public static void main(String[] args){
        String[] strList = args[0].split(",");
        int[] intList = new int[strList.length];
        for(int i=0; i<strList.length; i++){
            intList[i] = Integer.parseInt(strList[i]);
        }
        Sort sort = new Sort(intList);
        sort.printList();
        sort.sort(args[1]);
        sort.printList();
    }
}
