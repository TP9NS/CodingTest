def dfs(index, sum_score, sum_kal):
    global answer
    if sum_kal > max_kal:
        return
    if index == N:
        if answer < sum_score:
            answer = sum_score
        return
    dfs(index + 1, sum_score + arr[index][0], sum_kal + arr[index][1])
    dfs(index + 1, sum_score, sum_kal)

T = int(input())

for test_case in range(1, T + 1):
    N, max_kal = map(int, input().split())
    arr = []
    for i in range(N):
        score, kal = map(int, input().split())
        arr.append((score, kal))
    answer = 0
    dfs(0, 0, 0)
    print(f"#{test_case} {answer}")
