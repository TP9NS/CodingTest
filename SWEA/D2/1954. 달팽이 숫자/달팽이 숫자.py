T = int(input())
d = [(0,1),(1,0),(0,-1),(-1,0)]
for test_case in range(1, T + 1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    d_idx = 0
    x,y=0,0
    num=1
    for i in range(N*N):
        if arr[y][x] == 0:
            arr[y][x] = num
        n_y,n_x = d[d_idx]
        if x+n_x == N or y+n_y == N or arr[y+n_y][x+n_x] !=0:
            d_idx +=1
            d_idx = d_idx%4
        n_y,n_x = d[d_idx]
        x+=n_x
        y+=n_y
        num+=1
    print(f"#{test_case}")
    for j in arr:
        for i in j:
            print(i,end=" ")
        print()
