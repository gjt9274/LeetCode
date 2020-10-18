class Solution {
    public String reverseWords(String s) {
        int len = s.length();
        if (len < 1) {
            return "";
        }
        StringBuilder word = new StringBuilder();
        StringBuilder res = new StringBuilder();
        int i = 0;
        while (i < len) {
            char ch = s.charAt(i);
            if (ch == ' ') {
                res.append(word.reverse().toString());
                res.append(ch);
                word.setLength(0);
            } else {
                word.append(ch);
            }
            i++;
        }
        res.append(word.reverse().toString());
        return res.toString();
    }
}