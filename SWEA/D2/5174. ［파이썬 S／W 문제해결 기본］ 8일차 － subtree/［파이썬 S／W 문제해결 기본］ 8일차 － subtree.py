T = int(input())
def dfs(node):
    global count_num
    count_num+=1
    if node in graph:
        for i in graph[node]:
            dfs(i)
    else:
        return
for test_case in range(1, T + 1):
    n,node = map(int,input().split())
    arr = list(map(int,input().split()))
    
    graph = dict()
    #그래프 생성
    for i in range(0,len(arr),2):
        if arr[i] in graph:
            graph[arr[i]].append(arr[i+1])
        else:
            graph[arr[i]] = [arr[i+1]]
    flag=True
    count_num = 0

    dfs(node)
    print(f"#{test_case} {count_num}")