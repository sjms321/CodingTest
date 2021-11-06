def solution(s):
    answer=[]
    lastChar=None
    
    for ss in s:
        if lastChar is None:
            lastChar=ss
            answer.append(1)
        else:
            if lastChar==ss:
                answer[-1]+=1
            else:
                lastChar=ss
                answer.append(1)
                
    if s[0]==s[-1]:
        answer[0]+=answer[-1]
        del answer[-1]
        
    answer.sort()
    
    return answer