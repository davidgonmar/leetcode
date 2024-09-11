class Solution {
    public boolean isValid(String s) {
        var closingPars = List.of(')', '}', ']');
        if (closingPars.contains(s.charAt(0))) return false;
        
        Stack<Character> openStack = new Stack<Character>();
        openStack.push(s.charAt(0));
        


        for(var p: s.substring(1).toCharArray()){
            if (closingPars.contains(p)){
                if (openStack.empty()) return false;
                Character head = (Character) openStack.peek();
                if (p==(')') && !head.equals('(') ) return false;
                if (p==('}') && !head.equals('{') ) return false;
                if (p==(']') && !head.equals('[') ) return false;
                if (p==(')') || p==('}') || p==(']') ) openStack.pop();
            }
            else openStack.push(p);
            

        }
    if (!openStack.empty()) return false; else return true;
    }
}