def DFS(graph, v, visited):
    visited[v] = True
    n = len(graph)
    
    for node in range(n):
        if graph[v][node] == 1 and visited[node] == False:
            DFS(graph, node, visited)
    

def solution(n, computers):
    answer = 0
    visited = n * [0]    
    for start in range(n):
        if visited[start] == 0:
            DFS(computers, start, visited)
            answer += 1
            
    return answer


solution(3, [[1,1,0], [1,1,0], [0,0,1]])