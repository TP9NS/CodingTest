T = 10

for test_case in range(1, T + 1):
    trash = input()
    find = input()
    s =input()
    
    c = s.count(find)
    print(f"#{test_case} {c}")