class Solution {
    private int rows;
    private int cols;

    public int numIslands(char[][] grid) {
        rows = grid.length;
        cols = grid[0].length;
        if (rows == 0) {
            return 0;
        }
        int[][] directions = { { -1, 0 }, { 0, -1 }, { 1, 0 }, { 0, 1 } };
        boolean[][] marked = new boolean[rows][cols];
        int count = 0;
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (!marked[i][j] && grid[i][j] == '1') {// 如果没被访问过，且当前节点为1，则以该结点为起点开始BFS
                    count++;
                    // 需要将坐标添加进队列，可以将队列转成数字 i*cols + j
                    Queue<Integer> queue = new LinkedList<>();
                    queue.offer(i * cols + j);
                    marked[i][j] = true;
                    while (!queue.isEmpty()) {
                        int cur = queue.poll();
                        int x = cur / cols;
                        int y = cur % cols;
                        // 得到其子节点(邻居结点)
                        for (int k = 0; k < 4; k++) {
                            int newX = x + directions[k][0];
                            int newY = y + directions[k][1];
                            // 没越界 && 未访问 && 是陆地
                            if (inArea(newX, newY) && !marked[newX][newY] && grid[newX][newY] == '1') {
                                queue.offer(newX * cols + newY);
                                marked[newX][newY] = true;
                            }
                        }
                    }
                }
            }
        }
        return count;

    }

    public boolean inArea(int x, int y) {
        return x >= 0 && x < rows && y >= 0 && y < cols;
    }
}