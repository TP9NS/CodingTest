from collections import deque  # itertools가 아니라 collections입니다!

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = []
    for i in range(2):
        arr.append(list(map(int, input().split())))
    a = deque(arr[0])
    b = deque(arr[1])
    player =[]
    for i in range(N+1):
        player.append(i)
    for i in range(N//2+1):
        flag = True
        while flag:
            if a:
            	a_idx = a.popleft()
            else:
                break
            if player[a_idx]==a_idx:
                player[a_idx] = 'A'
                flag=False
        flag =True
        while flag:
            if b:
            	b_idx = b.popleft()
            else:
                break
            if player[b_idx]==b_idx:
                player[b_idx] = 'B'
                flag=False
    for i in range(1,len(player)):
        print(player[i],end="")
    print()
        
