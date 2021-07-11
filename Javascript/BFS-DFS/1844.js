function solution(maps) {
    const q = [];
    const dx = [0, 1, 0, -1];
    const dy = [1, 0, -1, 0];

    q.push([0, 0, 1]);
    while(q.length > 0) {
        const [x, y, cnt] = q.shift();
        if(x == maps.length-1 && y == maps[0].length-1) {
            return cnt;
        }
        for(var t=0; t<4; t++) {
            const nx = x + dx[t];
            const ny = y + dy[t];
            if(nx >= 0 && nx < maps.length && ny >= 0 && ny < maps[0].length && maps[nx][ny] == 1) {
                maps[nx][ny] = 0;
                q.push([nx, ny, cnt+1]);
            } 
        }
    }
    return -1;
}