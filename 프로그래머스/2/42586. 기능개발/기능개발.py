from collections import deque
import math

def solution(progresses, speeds):
    answer = []
    dq = deque()
    for i in range(len(progresses)):
        dq.append(math.ceil((100-progresses[i])/speeds[i]))
    
    while dq:
        now = dq.popleft()
        temp= 1
        while dq and dq[0] <= now:
            dq.popleft()
            temp+=1
        answer.append(temp)
    
    
    return answer