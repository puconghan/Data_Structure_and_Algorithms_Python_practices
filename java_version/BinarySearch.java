import java.io.*;
import java.util.*;

class BinarySearch {
    
    private List<Integer> list;

    public BinarySearch(List<Integer> list){
            this.list = list;
    }

    public boolean search(Integer target){
        int low = 0;
        int high = list.size() - 1;
        while ( high >= low){
            int middle = (low + high) / 2;
            if(list.get(middle) == target){
                return true;
            }else if(list.get(middle) < target){
                low = middle + 1;
            }else{
                high = middle - 1;
            }
        }
        return false;
    }

    /*
    static public Boolean search(Integer target){
        if (list.size() == 0){
            return false;
        } else {
            Integer pivot = (int)Math.ceil((double)list.size() / (double)2);
            if(list.get(pivot) == target){
                return true;
            } else if(target < list.get(pivot)){
                return _search(target, 0, pivot - 1);
            } else {
                return _search(target, pivot + 1, list.size() - 1);
            }
        }
    }

    static public Boolean _search(Integer target, Integer first, Integer last){
        if(list.size() == 0 || first > last){
            return false;
        } else{
            Integer pivot = (int)Math.ceil((double)(first + last) / (double)2);
            if (target == list.get(pivot)){
                return true;
            } else if (target < list.get(pivot)){
                return _search(target, 0, pivot - 1);
            } else {
                return _search(target, pivot + 1, last);
            }
        }
    }
    */

    public static void main(String[] args){
        List<String> strList = new ArrayList<String>(Arrays.asList(args[0].split(",")));
        List<Integer> intList = new ArrayList<Integer>();
        for(String str : strList){
            intList.add(Integer.parseInt(str));
        }
        Integer target = Integer.parseInt(args[1]);
        BinarySearch binarySearch = new BinarySearch(intList);
        System.out.println(binarySearch.search(target));
    }
}
