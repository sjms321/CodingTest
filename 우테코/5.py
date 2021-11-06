def solution(rows, columns):
    answer=[ [0] * columns for _ in range(rows) ]
    nowR=0
    nowC=0
    answer[nowR][nowC]=1
    lastNum=1
    
    while(1):
        if lastNum%2==0:
            if nowR==rows-1:
                nowR=0
            else:
                nowR+=1
        if lastNum%2==1:
            if nowC==columns-1:
                nowC=0
            else:
                nowC+=1
        lastNum+=1
        flag=False
        for i in answer:
            if not all(i):
                flag=True
                break
        if flag==False:
            break
        if answer[nowR][nowC]==0:
            pass
        elif (answer[nowR][nowC]%2==lastNum%2) or (answer[nowR][nowC]%2==lastNum%2):
            break
        answer[nowR][nowC]=lastNum
        
    return(answer)