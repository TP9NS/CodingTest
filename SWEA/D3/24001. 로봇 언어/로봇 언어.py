T = int(input())

for test_case in range(1, T + 1):
    s = input()
    L_case = 0
    R_case = 0
    max_val=0
    for direction in s:
        if direction == 'L':
            L_case -=1
            R_case -=1
        elif direction == '?':
            L_case -=1
            R_case +=1
        else:
            L_case+=1
            R_case+=1
        if max_val < max(abs(L_case),R_case):
            max_val = max(abs(L_case),R_case)
            
    print(max_val)
