def binary_search(P, find):
    start = 1
    end = P
    count = 0
    while start <= end:
        mid = (start + end) // 2
        count += 1
        if mid == find:
            return count
        elif mid < find:
            start = mid
        else:
            end = mid 
    return count  # 이 부분은 실행되지 않아야 합니다 (문제 조건에 따라)

T = int(input())
for test_case in range(1, T + 1):
    P, A, B = map(int, input().split())
    ans_A = binary_search(P, A)
    ans_B = binary_search(P, B)
    if ans_A < ans_B:
        print(f"#{test_case} A")
    elif ans_A > ans_B:
        print(f"#{test_case} B")
    else:
        print(f"#{test_case} 0")