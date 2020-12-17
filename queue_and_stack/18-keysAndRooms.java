class Solution {
    boolean[] vis;
    int num = 0;
    public boolean canVisitAllRooms(List<List<Integer>> rooms) {
        int n = rooms.size();
        vis = new boolean[n];
        dfs(rooms,0);
        return num==n;

    }
    public void dfs(List<List<Integer>> rooms, int index){
        vis[index] = true;
        num++;
        for (int next : rooms.get(index)){
            if(!vis[next]){
                dfs(rooms,next);
            }
        }
    }
}