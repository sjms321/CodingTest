#BFS는 너비 우선 탐색이라 불리며, 그래프에서 가까운 노드부터 우선적으로 탐색하는 알고리즘이다.
# 큐 자료구조를 이용한다.
#각 간선의 비용인 동일한 상황에서 최단거리를 구하는데 좋다.


from collections import deque

def bfs(graph,start,visited):
    
    queue = deque([start])
    #시작 노드 방문처리
    visited[start] = True

    while queue:
        #큐에서 해당 원소를 뽑아 출력
        v= queue.popleft()
        print(v,end=' ')

        #아직 방문하지 않은 인접한 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
        


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
bfs(graph,2,visited)