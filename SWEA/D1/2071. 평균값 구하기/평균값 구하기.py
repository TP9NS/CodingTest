T = int(input())

for test_case in range(1, T + 1):
    arr = list(map(int,input().split()))
    avg = sum(arr)/10
    
    print(f"#{test_case}",round(avg))