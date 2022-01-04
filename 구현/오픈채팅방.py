def solution(record):
    answer = []
    userNameMatching = {}
    do = [] 
    
    for i in record:
        temp = []
        temp = i.split() 
        action, userid = temp[0], temp[1]
        if action in ("Enter", "Change"):
            name = temp[2]
            userNameMatching[userid] = name
        do.append((action, userid))
        
    for i in do:
        action, userid = i[0], i[1]
        if action == 'Enter':
            answer.append(f'{userNameMatching[userid]}님이 들어왔습니다.')
        elif action == 'Leave':
            answer.append(f'{userNameMatching[userid]}님이 나갔습니다.')
    
    return answer