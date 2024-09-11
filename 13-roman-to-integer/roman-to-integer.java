class Solution {
    public int romanToInt(String s) {
        Map<Character, Integer> symbolsMap = new HashMap<>();
        
        symbolsMap.put('I', 1);
        symbolsMap.put('V', 5);
        symbolsMap.put('X', 10);
        symbolsMap.put('L', 50);
        symbolsMap.put('C', 100);
        symbolsMap.put('D', 500);
        symbolsMap.put('M', 1000);

        
        int res = 0;
        for (int i = s.length() -1; i>=0; i--){
           Integer last = symbolsMap.get(s.charAt(i));
           if (i> 0 && last>symbolsMap.get(s.charAt(i-1))) {res+=last-symbolsMap.get(s.charAt(i-1));i--; continue;}
           res+=last;

        }
        return res;
    }
}