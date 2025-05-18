def in_order_fill(node, N, tree, values, index):
    if node > N:
        return index
    index = in_order_fill(node * 2, N, tree, values, index)
    tree[node] = values[index]
    index += 1
    index = in_order_fill(node * 2 + 1, N, tree, values, index)
    return index

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    tree = [0] * (N + 1)  # 1번부터 N번까지 사용
    values = list(range(1, N + 1))  # 1부터 N까지 숫자
    
    in_order_fill(1, N, tree, values, 0)

    print(f"#{test_case} {tree[1]} {tree[N // 2]}")
