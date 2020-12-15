class Solution {
    public String decodeString(String s) {
        Deque<String> stk = new LinkedList<>();
        int i = 0;
        int len = s.length();
        while(i < len){
            char ch = s.charAt(i);
            if (Character.isDigit(ch)){
                StringBuilder number = new StringBuilder();
                while(Character.isDigit(s.charAt(i))){
                    number.append(s.charAt(i));
                    i++;
                }
                stk.push(number.toString());
            }else if(Character.isLetter(ch) || ch == '['){
                stk.push(Character.toString(ch));
                i++;
            }else{
                i++;
                StringBuilder repeatSeg = new StringBuilder();
                while(!"[".equals(stk.peek())){
                    repeatSeg.insert(0,stk.pop());
                }
                stk.pop();//弹出'['
                int repeatNumber = Integer.parseInt(stk.pop());
                StringBuilder pushSeg = new StringBuilder();
                while(repeatNumber != 0){
                    repeatNumber--;
                    pushSeg.append(repeatSeg);
                }
                stk.push(pushSeg.toString());
            }
        }
        StringBuilder res = new StringBuilder();
        while(!stk.isEmpty()){
            res.insert(0,stk.pop());
        }
        return res.toString();
    }
}