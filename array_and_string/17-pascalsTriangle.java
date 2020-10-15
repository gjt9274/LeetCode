class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> res = new ArrayList<>();
        for (int i = 0; i < numRows; i++) {
            List<Integer> tmp = new ArrayList<>();
            if (res.isEmpty()) {
                tmp.add(1);
            } else {
                List<Integer> prev = res.get(i - 1);
                tmp.add(1);
                for (int j = 1; j < prev.size(); j++) {
                    tmp.add(prev.get(j - 1) + prev.get(j));
                }
                tmp.add(1);
            }
            res.add(tmp);
        }
        return res;
    }
}