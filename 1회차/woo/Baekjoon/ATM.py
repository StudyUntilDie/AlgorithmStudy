n = int(input())
p = list(map(int, input().split()))

p.sort()

result = 0
sum = 0

for i in range(len(p)):
    sum += p[i]
    result += sum
    
print(result)