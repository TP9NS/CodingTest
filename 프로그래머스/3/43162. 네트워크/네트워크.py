from collections import deque
def solution(n, computers):
    answer = 0
    graph = dict()
    for i in range(len(computers)):
        graph[i] = []
    for idx,com in enumerate(computers):
        for i,c in enumerate(com):
            if c == 1:
                graph[idx].append(i)
                
    visited = set()
    queue = deque()
    for i in graph.keys():
        if i in visited:
            continue
        else:
            queue.append(i)
            visited.add(i)
            
            while queue:
                node = queue.popleft()
                for nxt in graph[node]:
                    if nxt not in visited:
                        queue.append(nxt)
                        visited.add(nxt)
            answer+=1
            
    
                
    return answer