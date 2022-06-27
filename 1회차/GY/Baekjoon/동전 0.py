n, k = map(int, input().split())
temp = []
answer = 0

# 배열에 동전의 종류를 담는다
for i in range(n):
    temp.append(int(input()))
# 배열에 담긴 동전들을 내림차순으로 정렬 해준다
temp.sort(reverse=True)

# 동전의 갯수만큼 확인한다.
# 배열에 담긴 동전 중 큰 순서대로 최종금액을 나누고 
# 1. 나눈 금액의 몫을 정답에 추가해 나간다.
# 2. 나눈 금액의 나머지를 k로 만들어준다
# 위 1번 2번을 반복해서 실행 시켜주면서 
# 총 금액이 0이되면 탈출한다.
for i in range(n):
    if k >= 0:
        answer += k // temp[i]
        k %= temp[i]
        if k <= 0:
            break
print(answer)
