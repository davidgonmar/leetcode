class Solution {
    public int climbStairs(int n) {
        return(climbStairsHelper(n, new HashMap<>()));
    }
    public int climbStairsHelper(int n, Map<Integer, Integer> memory){
        if (n == 1) return 1;
        if (n==2) return 2;
        Integer diffSol = 0;
        if (memory.containsKey(n)) return memory.get(n);
        diffSol+=climbStairsHelper(n-1, memory);
        diffSol+=climbStairsHelper(n-2, memory);
        memory.put(n, diffSol);
        return diffSol;
    }
}