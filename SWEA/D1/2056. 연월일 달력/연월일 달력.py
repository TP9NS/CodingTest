T = int(input())

month_days = {
    1: 31, 2: 28, 3: 31, 4: 30,
    5: 31, 6: 30, 7: 31, 8: 31,
    9: 30, 10: 31, 11: 30, 12: 31
}

for test_case in range(1, T + 1):
    date = input().strip()
    year = int(date[:4])
    month = int(date[4:6])
    day = int(date[6:])

    if 1 <= month <= 12 and 1 <= day <= month_days[month]:
        print(f"#{test_case} {year:04d}/{month:02d}/{day:02d}")
    else:
        print(f"#{test_case} -1")
