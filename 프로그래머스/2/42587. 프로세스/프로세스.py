from collections import deque

def solution(priorities, location):
    answer = 0
    dq= deque()
    for i,j in enumerate(priorities):
        dq.append((i,j))
    
    max_pri = max(dq, key= lambda x : x[1])[1]
    
    while True:
        idx,pri = dq.popleft()
        if max_pri == pri:
            answer+=1
            if idx == location:
                break
            else:
                max_pri = max(dq, key= lambda x : x[1])[1]
        else :
            dq.append((idx,pri))
    return answer