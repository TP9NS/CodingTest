T = 10

for test_case in range(1, T + 1):
    trash = input()
    arr = []
    for _ in range(100):
        temp = list(map(int, input().split()))
        arr.append(temp)

    daegak_1 = 0
    daegak_2 = 0
    row_max = 0
    col_max = 0

    for i in range(100):
        row_sum = sum(arr[i])
        row_max = max(row_max, row_sum)

        col_sum = 0
        for j in range(100):
            col_sum += arr[j][i]
        col_max = max(col_max, col_sum)

        daegak_1 += arr[i][i]
        daegak_2 += arr[i][99 - i]

    print(f"#{test_case} {max(daegak_1, daegak_2, row_max, col_max)}")
