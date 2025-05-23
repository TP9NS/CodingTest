T = int(input())

for test_case in range(1, T + 1):
    arr= list(map(int,input().split()))
    arr.sort(reverse = True)
    hap = sum(arr)
    buha = arr[0]+1
    while (buha + hap)%7 !=0:
        buha+=1
    print(buha)
