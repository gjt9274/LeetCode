class Solution {
    public int rows;
    public int cols;
    public int[][] floodFill(int[][] image, int sr, int sc, int newColor) {
        int oldColor = image[sr][sc];
        rows = image.length;
        cols = image[0].length;
        int[][] directions = { { -1, 0 }, { 0, -1 }, { 1, 0 }, { 0, 1 } };
        Set<Integer> visited = new HashSet<>();
        Deque<Integer> stk = new LinkedList<>();
        stk.push(sr*50+sc);
        while(!stk.isEmpty()){
            int cur = stk.pop();
            int x = cur / 50;
            int y = cur % 50;
            image[x][y] = newColor;
            for(int i = 0; i < 4; i++){
                int newX = x + directions[i][0];
                int newY = y + directions[i][1];
                int next = newX*50 + newY;
                if(inArea(newX,newY) && !visited.contains(next) && image[newX][newY] == oldColor){
                    stk.push(next);
                    visited.add(next);
                }
            }
        }
        return image;
    }
    public boolean inArea(int x,int y){
        return x >=0 && x < rows && y >=0 && y < cols;
    }
}