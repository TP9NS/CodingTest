T = int(input())
def dfs(arr,depth):
    global max_val
    if depth==n:
        max_val = max(max_val,int("".join(arr)))
    else:
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                arr[i],arr[j]= arr[j],arr[i]
                if ("".join(arr),depth) not in visited:
                    dfs(arr,depth+1)
                    visited.add(("".join(arr),depth))
                arr[i],arr[j]= arr[j],arr[i]
for test_case in range(1, T + 1):
    s,n = input().split()
    n = int(n)
    arr = list(s)
    max_val =0
    visited=set()
    dfs(arr,0)
    print(f"#{test_case} {max_val}")
