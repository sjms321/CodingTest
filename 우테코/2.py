#공부 시작 후 5분전 중지x
#송부 시작 후 1시간 45분 넘어서 중지하면 1시간 45분까지만 max가 1시간45분 즉,105분
def solution(log):
    answer = ''
    result = 0
    for i in range(0,len(log),2):
        tempStart = log[i].split(":")
        Start = (int(tempStart[0])*60)+int(tempStart[1])
        
        tempEnd = log[i+1].split(":")
        End = (int(tempEnd[0])*60)+int(tempEnd[1])
        
        studyTime = End-Start
        if studyTime<5:
            studyTime = 0
        elif studyTime>105:
            studyTime = 105
        
        result += studyTime
        
    hour = str(result//60)
    min =  str(result%60)
    if len(hour) == 1 :
        hour = "0"+hour
    answer = hour +":"+min
       
    print(answer)

        
    return answer