def is_pal(arr):
    start = 0
    end = len(arr)-1
    flag = True
    while start < end:
        if arr[start] != arr[end]:
            flag = False
            break
        else:
            start += 1
            end -= 1
    return flag
            
T = 10

for test_case in range(1, T + 1):
    N = int(input())
    arr = []
    count = 0
    for i in range(8):
        temp = list(input().strip())  # 문자열로 처리 (문제에 따라 int로 할지 결정)
        arr.append(temp)
    
    for i in range(8):
        for j in range(9 - N):
            # 가로 방향 검사
            if is_pal(arr[i][j:j+N]):
                count += 1
            # 세로 방향 검사
            temp = [arr[j+k][i] for k in range(N)]
            if is_pal(temp):
                count += 1
    print(f"#{test_case} {count}")