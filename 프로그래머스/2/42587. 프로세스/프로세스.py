from collections import deque

def solution(priorities, location):
    dq = deque()
    answer= 0
    
    for i,j in enumerate(priorities):
        dq.append((i,j))
        
    while dq:
        max_dq = max(dq,key=lambda x : x[1])[1]
        temp = dq.popleft()
        if temp[1] == max_dq:
            answer+=1
            if temp[0] == location:
                return answer
            else:
                max_dq = max(dq,key=lambda x: x[1])[1]
        else:
            dq.append(temp)
                
    return answer