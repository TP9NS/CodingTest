T = int(input())
color = ["red","orange","yellow","green","blue","purple"]
for test_case in range(1, T + 1):
    c1,c2 = input().split()
    c1_idx = color.index(c1)
    c2_idx = color.index(c2)
    
    if c1_idx == c2_idx:
        print("E")
    elif abs(c1_idx-c2_idx) == 3:
        print("C")
    elif abs(c1_idx-c2_idx) == 1 or abs(c1_idx-c2_idx) == 5:
        print("A")
    else:
        print("X")
    