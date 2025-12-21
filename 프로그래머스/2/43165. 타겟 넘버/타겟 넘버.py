from collections import deque

def solution(numbers,target):
    count= 0
    
    queue = deque([(0,0)])
    
    while queue:
        idx,value = queue.popleft()
        if idx < len(numbers):
            queue.append((idx+1,value+numbers[idx]))
            queue.append((idx+1,value-numbers[idx]))
        if idx == len(numbers):
            if value == target:
                count+=1
    return count