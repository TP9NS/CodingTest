def inorder(idx):  # idx: 현재 노드 번호
    global cnt
    if idx <= N:
        inorder(idx * 2)         # 왼쪽 자식 방문
        tree[idx] = cnt          # 현재 노드에 cnt값 저장
        cnt += 1
        inorder(idx * 2 + 1)     # 오른쪽 자식 방문

T = int(input())
for tc in range(1, T + 1):
    N = int(input())             # 트리의 총 노드 수
    tree = [0] * (N + 1)         # 1번부터 쓰기 위해 N+1 크기 배열
    cnt = 1                      # 1부터 시작해서 순서대로 채움
    inorder(1)                   # 루트(1번 노드)부터 순회 시작
    print(f"#{tc} {tree[1]} {tree[N // 2]}")
