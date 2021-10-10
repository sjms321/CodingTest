input = input()
list = []
count = 0
for i in range(len(input)):

    #해당 글자가 알파벳인지 확인하는 법
    if input[i].isalpha() :
        list.append(input[i])
    else :
        count += int(input[i])        

list.sort()
print(''.join(list)+str(count))
