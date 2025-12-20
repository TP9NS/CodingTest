from collections import deque

def solution(n, vertex):
    graph = dict()
    for i,j in vertex:
        if i in graph:
            graph[i].append(j)
        else:
            graph[i]= [j]
        if j in graph:
            graph[j].append(i)
        else:
            graph[j] = [i]
            
    visited = set([1])
    dq =deque()
    dq.append(1)
    dis = {1:0}
    
    while dq:
        node = dq.popleft()
        nodes = graph[node]
        for i in nodes:
            if i in visited:
                continue
            else:
                visited.add(i)
                dq.append(i)
                dis[i]=dis[node]+1
    max_dis = max(dis.items(),key= lambda x:x[1])[1]
    count=0
    for i in dis.values():
        if i == max_dis:
            count +=1
    return count
