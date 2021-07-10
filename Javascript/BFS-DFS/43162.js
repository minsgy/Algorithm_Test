function solution(n, computers) {
    let answer = 0;
    let visited = [];
    
    for (let i = 0; i < n; i++){
        visited.push(false);
    }
    
    var DFS = function(computers, i) {
        if(visited[i]) return; 
        visited[i] = true;

        for(var j = 0; j < computers.length; j++) {
            if(computers[i][j] === 1) {
                console.log(i + ', ' + j);
                console.log('connected');
                DFS(computers, j);
            }
        }
    }
    
    
    for(var i = 0; i < n; i++) {
        if(!visited[i]) {
            answer++;
            console.log(answer);
            DFS(computers, i);
        }
    }
    
    return answer;
}