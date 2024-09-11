class Solution {
    Set<Character> vowels = Set.of('a', 'e', 'i', 'o', 'u');
    private Boolean isVowel(char c){
        return this.vowels.contains(c);
    }
    public int maxVowels(String s, int k) {
        int count = 0; int max = 0;
        for(int i =0; i < s.length(); i++){
           if(isVowel(s.charAt(i))) count++;
           if(!(i<k) && isVowel(s.charAt(i-k))) count --;
           max = Math.max(count, max);
        }
        return max;
    }
}