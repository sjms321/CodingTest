N =int(input())
X = 1
Y= 1
move = input().split()

move_al = ['R','L','U','D']
dx = [0,0,-1,1]
dy = [1,-1,0,0]

for i in move:
    for z in range(len(move_al)):
        if i==move_al[z]:
            nx = X+dx[z]
            ny = Y+dy[z]
    if nx == 0 or nx > N or ny > N  or ny == 0:
        continue
    X = nx
    Y = ny

print(X,Y)