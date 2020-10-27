class Solution {
    public int openLock(String[] deadends, String target) {
        Set<String> deads = new HashSet();
        for (String d:deadends){deads.add(d);}

        Queue<String> queue = new LinkedList();
        queue.offer("0000");
        queue.offer(null); //用来分隔层
        
        Set<String> seen = new HashSet(); //访问记录
        seen.add("0000");

        int depth = 0;
        while (!queue.isEmpty()){
            String node = queue.poll();
            if(node == null){
                depth++;
                if(queue.peek() != null){
                    queue.offer(null);
                }
            }else if (node.equals(target)){
                return depth;
            } else if(!deads.contains(node)){
                for(int i = 0; i < 4;i++){
                    for (int d = -1; d <= 1; d += 2){ //每个位置有两个方向，增大或者减小
                        int y = ((node.charAt(i) - '0') + d + 10) % 10;
                        String neig = node.substring(0,i) + ("" + y) + node.substring(i+1);
                        if (!seen.contains(neig)){
                            seen.add(neig);
                            queue.offer(neig);
                        }
                    }
                }
            }
        }

    return -1;
    }
}