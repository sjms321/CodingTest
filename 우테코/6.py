def solution(time, plans):
    answer = ''
    quittingTime = 18
    workingStratTime = 9.5
    departureTime = []
    arriveTime = []
    for i in plans :
        departureTime.append(i[1])
        arriveTime.append(i[2])
    

    for i in range(len(departureTime)):
        if departureTime[i][-2:] =="PM":
            departureTime[i] = int(departureTime[i][:-2])+12
        if arriveTime[i][-2:] =="PM":
            arriveTime[i] = int(arriveTime[i][:-2])+12
        else : 
            arriveTime[i] = int(arriveTime[i][:-2])
    
    for i in range(len(plans)):
        loss = 0
        if departureTime[i]<quittingTime:
            loss += quittingTime-departureTime[i]
        else : loss += 0
            
        if arriveTime[i]>workingStratTime:
            loss += arriveTime[i]-workingStratTime
        else : loss += 0
        
        if loss <= time:
            answer = plans[i][0]
    
    
    
    return answer