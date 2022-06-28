n, k = map(int, input().split())
a = []

for i in range(n):
    a.append(int(input()))
    
a.sort(reverse=True)
    
result = 0

for i in a:
    result += k // i
    k %= i

print(result)