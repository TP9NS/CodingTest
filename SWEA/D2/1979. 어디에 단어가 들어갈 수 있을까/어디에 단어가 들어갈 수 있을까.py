T = int(input())

for test_case in range(1, T + 1):
    N, num_len = map(int, input().split())
    arr = []
    answer = 0
    for i in range(N):
        temp = list(map(int, input().split()))
        arr.append(temp)
    
    # 가로 방향 검사
    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[i][j] == 1:
                cnt += 1
            else:
                if cnt == num_len:
                    answer += 1
                cnt = 0
        # 행의 끝에서 확인
        if cnt == num_len:
            answer += 1
    
    # 세로 방향 검사
    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[j][i] == 1:
                cnt += 1
            else:
                if cnt == num_len:
                    answer += 1
                cnt = 0
        # 열의 끝에서 확인
        if cnt == num_len:
            answer += 1
    
    print(f"#{test_case} {answer}")