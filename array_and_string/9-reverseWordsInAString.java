class Solution {
    public String reverseWords(String s) {
        int left = 0, right = s.length() - 1;
        // 去掉左边空格
        while (left < right && s.charAt(left) == ' ') {
            left++;
        }
        // 去掉右边空格
        while (left < right && s.charAt(right) == ' ') {
            right--;
        }
        Deque<String> res = new LinkedList<>();
        StringBuilder word = new StringBuilder();
        while (left <= right) {
            if (word.length() != 0 && s.charAt(left) == ' ') {
                res.offerFirst(word.toString());
                word.setLength(0);
            } else if (s.charAt(left) != ' ') {
                word.append(s.charAt(left));
            }
            left++;
        }
        res.offerFirst(word.toString());
        return String.join(" ", res);
    }
}