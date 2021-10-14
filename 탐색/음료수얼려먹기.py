def dfs(x,y):
    #주어진 범위를 벗어나면 종료
    if x<=-1 or x>=n or y <= -1 or y>= m :
        return False
    #노드 방문안했으면 방문으로 바꿈   
    if graph[x][y] == 0:
        graph[x][y]==1
        #상하좌우 재귀로 호출
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False


N,M = map(int,input().split())


#맵만들기
graph=[]
for i in range(N):
    graph.append(list(map(int,input())))

print(graph)
#머든 노드에대하여 음료수 채우깅
result = 0
for i in range(N):
    for j in range(M):
        if dfs(i,j) == True:
            result +=1

print(result)



