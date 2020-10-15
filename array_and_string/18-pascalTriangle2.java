class Solution {
    public List<Integer> getRow(int rowIndex) {
        int n = rowIndex + 1;
        List<Integer> res = new ArrayList<>(n);
        for (int i = 0; i < n; i++){
            if(i == 0){
                res.add(1);
            }else{
                long val = (long) res.get(i-1) * (long) (n - i) / i;
                res.add((int)val);
            }
        }
        return res;
    }
}