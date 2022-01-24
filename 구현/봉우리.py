
count = 0
n=int(input())
array=[list(map(int, input().split())) for _ in range(n)]
array.insert(0, [0]*n)
array.append([0]*n)
for x in array:
    x.insert(0, 0)
    x.append(0)


def check(i,j):
    if(array[i-1][j]<array[i][j] and array[i+1][j]<array[i][j] and array[i][j-1]<array[i][j] and array[i][j+1]<array[i][j]):
        return True
    else : return False

for i in range(n):
    for j in range(n):
        if check(i+1,j+1) == True:
            count += 1

print(count)
