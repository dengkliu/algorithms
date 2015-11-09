public class PermutationofList {
    public ArrayList<ArrayList<Integer>> permute(int[] num) {
        ArrayList<ArrayList<Integer>> lists = new ArrayList<ArrayList<Integer>>();
        if(num.length<=0){
            return lists;
        }
        boolean []visited = new boolean[num.length];
        Arrays.fill(visited,false);
        ArrayList<Integer> temp = new ArrayList<Integer>();
        permuteHelp(lists,temp,num,visited);
        return lists;
    }
    public void permuteHelp(ArrayList<ArrayList<Integer>> lists, ArrayList<Integer> temp, int[]num,boolean[] visited){
        if(temp.size()==num.length){
            lists.add(new ArrayList<Integer>(temp));
            return;
        }else{
            for(int i = 0; i < num.length; i++){
                if(!visited[i])
                temp.add(num[i]);.
                visited[i] = true;
                permuteHelp(lists, temp, num,visited);
                visited[i]= false;
                temp.remove(temp.size()-1);
            }

            }
        }
    }
} 