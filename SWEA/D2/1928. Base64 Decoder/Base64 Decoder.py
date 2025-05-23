table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

T = int(input())
for t in range(1, T + 1):
    s = input().strip()
    binary = ""

    for ch in s:
        idx = table.index(ch)
        binary += format(idx, '06b')  # 6비트로 변환

    result = ""
    for i in range(0, len(binary), 8):
        byte = binary[i:i+8]
        if len(byte) < 8:
            continue
        result += chr(int(byte, 2))

    print(f"#{t} {result}")
