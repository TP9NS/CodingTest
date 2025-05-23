T = int(input())
for _ in range(T):
    L, R = map(int, input().split())
    print("yes" if 2 * L > R else "no")