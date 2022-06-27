p = int(input())

# 돈을 인출하는데 걸리는 시간을 배열에 담는다
wait = list(map(int, input().split()))
# 배열에 담긴 시간을 오름차순으로 정렬시킨다
wait.sort()

temp = 0
answer = []

# 정렬된 돈 더해가면서 정답 배열에 담는다
for i in range(p):
    temp += wait[i]
    answer.append(temp)

# 정답 배열에 담긴 시간들을 더한다
print(sum(answer))
