from collections import deque
def solution(maps):
    x_d = [-1,1,0,0]
    y_d = [0,0,-1,1]
    
    queue = deque([(0,0)])
    d = [[0]*len(maps[0])for i in range(len(maps))]
    d[0][0] =1
    visited = set((0,0))
    while queue:
        y,x = queue.popleft()
        for i in range(4):
            if x+x_d[i] >= 0 and x+x_d[i]<len(maps[0]):
                if y+y_d[i] >=0 and y+y_d[i]<len(maps):
                    if maps[y+y_d[i]][x+x_d[i]] == 0:
                        continue
                    if (y+y_d[i],x+x_d[i]) not in visited:
                        d[y+y_d[i]][x+x_d[i]] = d[y][x]+1
                        queue.append((y+y_d[i],x+x_d[i]))
                        visited.add((y+y_d[i],x+x_d[i]))
    answer = d[len(maps)-1][len(maps[0])-1]
    if answer == 0:
        return -1
    return answer