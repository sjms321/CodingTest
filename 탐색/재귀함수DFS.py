#DFS 깊이 우선 탐색이라고도 하며 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘
#스택 또는 재쉬함수를 이용하여 구현한다.



#DFS 메서드 정의
def dfs(graph, v, visited):
    #해당 노드 방문표시
    visited[v] = True
    print(v,end=' ')
    
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

#각 노드가 연결된 정보를 2차원 리스트로 표현 
graph = [
    [],
    [2,3,4],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7],
]

#각 노드가 방문된 정보를 1차원 리스트로 표현
visited = [False] * 9

# 정의된 DFS함수를 통해 1번 노드부터 DFS 탐색실시.
dfs(graph,2,visited)