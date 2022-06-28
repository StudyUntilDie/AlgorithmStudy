n = int(input())
p = list(map(int, input().split()))
p.sort()

total_time = [p[0]]
result = p[0]

for i in range(1, n):
    total_time.append(p[i] + total_time[i - 1])
    result += total_time[i]

print(result)
