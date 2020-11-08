class Solution {
    public int evalRPN(String[] tokens) {
        Deque<Integer> stack = new LinkedList<>();
        for (int i = 0; i < tokens.length; i++) {
            String curToken = tokens[i];
            if (!curToken.equals("+") && !curToken.equals("-") && !curToken.equals("*") && !curToken.equals("/")) {
                stack.push(Integer.parseInt(curToken));
            } else {
                int b = stack.pop();
                int a = stack.pop();
                int c = 0;
                switch (curToken) {
                    case "+":
                        c = a + b;
                        break;
                    case "-":
                        c = a - b;
                        break;
                    case "*":
                        c = a * b;
                        break;
                    case "/":
                        c = a / b;
                        break;
                }
                stack.push(c);
            }
        }
        return stack.peek();
    }
}