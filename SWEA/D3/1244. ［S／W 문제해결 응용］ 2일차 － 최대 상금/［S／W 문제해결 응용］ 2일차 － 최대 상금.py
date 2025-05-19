T = int(input())

def solve(arr, depth):
    global max_val
    if depth == n:
        max_val = max(max_val, int(''.join(arr)))
        return

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            arr[i], arr[j] = arr[j], arr[i]
            key = (''.join(arr), depth + 1)
            if key not in visited:
                visited.add(key)
                solve(arr, depth + 1)
            arr[i], arr[j] = arr[j], arr[i]  # 원상복구

for test_case in range(1, T + 1):
    s, n = input().split()
    n = int(n)
    arr = list(s)
    visited = set()
    max_val = 0
    solve(arr, 0)
    print(f"#{test_case} {max_val}")
