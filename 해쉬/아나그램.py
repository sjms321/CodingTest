first =input()
second =input()
dic = dict()

for i in first:
    dic[i]=dic.get(i,0)+1
for i in second:
    dic[i]=dic.get(i,0)-1

for i in first:
    if dic[i]>0:
        print("NO")
        break
else :
    print("YES")