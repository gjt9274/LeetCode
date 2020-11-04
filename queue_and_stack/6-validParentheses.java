class Solution {
    public boolean isValid(String s) {
        Deque<Character> stack = new LinkedList<>();
        char[] charArray = s.toCharArray();
        for (char c : charArray){
            if(c == '(' || c=='[' || c=='{'){
                stack.push(c);
            }else if(!stack.isEmpty()){
                char top = stack.peek();
                if(c==')' && top == '(' || c==']' && top=='[' || c=='}'&&top=='{'){
                    stack.pop();
                }else{
                    return false;
                }
            }else{
                return false;
            }
        }
        if(stack.isEmpty()){
            return true;
        }else{
            return false;
        }
    }
}