class Solution {
    public String longestCommonPrefix(String[] strs) {
        String res = "";
        Arrays.sort(strs);
        for (int i = 0; i<strs[0].length(); i++){
            char ch = strs[0].charAt(i);
            for(String str:strs){
                if(ch!=str.charAt(i)) return res;

            }
            res+=ch;
        }
        return res;
       
    }

}