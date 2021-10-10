al = ['a','b','c','d','e','f','g','h']


input_ = input()


for i in range(len(al)):
    if input_[0]==al[i]:
        y = i+1



x = input_[1]

steps=[(-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,-1),(2,1)]

count =0
for i in steps:
    
    next_x = int(x)+int(i[0])
    next_y = int(y)+int(i[1])
    if next_x>=1 and next_x<=8  and next_y<=8 and next_y>=1 :
        count += 1    
    

print(count)
