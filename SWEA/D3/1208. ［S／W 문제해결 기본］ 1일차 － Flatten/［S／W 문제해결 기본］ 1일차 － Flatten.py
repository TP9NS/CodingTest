for case in range(1, 11):
    dump = int(input())
    arr = list(map(int, input().split()))
    for i in range(dump):
        min_val = min(arr)
        max_val = max(arr)
        min_idx = arr.index(min_val)
        max_idx = arr.index(max_val)

        arr[min_idx] += 1
        arr[max_idx] -= 1
    print(f"#{case} {max(arr) - min(arr)}")