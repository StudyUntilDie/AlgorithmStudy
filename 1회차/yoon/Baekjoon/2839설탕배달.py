n = int(input())

result = 0
# 처음 몫
value = n // 5
# 처음 나머지
other = n % 5

# 가능한 5로 많이 나누는 게 중요. 5로 나눌만큼 나누고 3으로 나누면 최소값이 된다.
while True:
    # 5로 최대한 나눈 나머지가 3으로 나눠떨어질 때 종료
    if other % 3 == 0:
        result = value + (other // 3)
        break
    # 끝까지 안 나눠질 경우
    elif value < 1:
        result = -1
        break
    # 몫에서 하나씩 빼가면서 체크
    value -= 1
    # 나머지 업데이트
    other = n - value * 5

print(result)
