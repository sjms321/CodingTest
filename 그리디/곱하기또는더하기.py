data = input()

result = int(data[0])

for i in range(1,len(data)):
    if result<=1 or int(data[i]) <=1 :
        result =  result + int(data[i])
    else :
        result = result * int(data[i])

print(result)
