n, k = map(int, input().split())
a = []
result = 0

for i in range(n):
    a.append(int(input()))
for i in range(n - 1, -1, -1):
    # 나누려는 수보다는 커야 함.
    if a[i] <= k:
        result += k // a[i]
        k %= a[i]
    # 더 나눌 수 없을 때 탈출
    if k == 0:
        break
print(result)
