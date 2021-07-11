function solution(n, wires) {
    let maps = [];
    let count = []; // 간선 갯수 세기
    let visited = []
    let count_dfs = 0;
    let maxs_count_dfs = []

    //  방문 기록 체크하기
    for (let i=0;i<=n;i++){
        visited[i] = false;
    }
        
    //  맵 만들기
    for (let i=0;i<=n;i++){
        maps[i] = [];
        for (let j=0;j<=n;j++){
            maps[i][j] = 0;
        }
    }
    
    for (let [x, y] of wires){
        maps[x][y] = 1;
        maps[y][x] = 1; 
    }
    
    // 간선 갯수 저장하기   
    for (let i in maps){
        count.push({ 'length' : maps[i].filter(element => 1 == element).length, 'index' : parseInt(i)});
    }
    
    // 간선 갯수 최대 값 뽑기
    let max_edge = count.reduce( function (previous, current) { 
        return previous.length > current.length ? previous:current;
    });
    
    // 깊이 우선 탐색 
    function DFS(v){
        visited[v] = true;
        // 가장 많은 쪽 노드 카운트 세기
        maxs_count_dfs.push({ 'node': v, 'count': count_dfs });
        count_dfs+=1;
        for (let i=1;i<=n;i++){
            if (visited[i] == false && maps[v][i] == 1){
                DFS(i);
            }
        }
        count_dfs = 1;
    }
    
    // 가장 많은 간선을 가진 노드 부터 시작     
    DFS(max_edge.index);
    // 가장 많은 탐색 횟수 노드   
    let maxsis = maxs_count_dfs.reduce( function (pre, cur) {
        return pre.count > cur.count ? pre : cur;
    });
    
    // 전체 노드 개수 - 나눠지는 쪽 노드 개수 = 나머지 한쪽 노드 개수
    // 한쪽 노드 개수 - 나눠지는 쪽 노드 개수 = abs() 절대 값 처리 
    return Math.abs((n-maxsis.count)-maxsis.count);
}