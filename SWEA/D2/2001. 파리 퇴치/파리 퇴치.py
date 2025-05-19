T = int(input())

for test_case in range(1, T + 1):
    N,M = map(int,input().split())
    arr=[]
    for i in range(N):
        temp = list(map(int,input().split()))
        arr.append(temp)
    plus = M -1
    answer=0
    for i in range(N-plus):
        for j in range(N-plus):
            hap=0
            for x in range(M):
                for y in range(M):
                    hap+=arr[i+x][j+y]
            if hap>answer:
                answer = hap
    print(f"#{test_case}",answer)
                