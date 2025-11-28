from collections import deque
import math
def solution(players, m, k):
    answer = 0
    server= deque()
    for i in range(len(players)):
        while server:
            if server[0]<i:
                server.popleft()
            else:
                break
        need = players[i]//m
        new_server = need-len(server)
        print(players[i],"-",len(server),"-",new_server)
        if need<=0:
            continue
        for _ in range(new_server):
            server.append(i+k-1)
            answer+=1
        
    
    return answer