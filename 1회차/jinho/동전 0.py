'''
최솟값을 만드려면 제일큰 동전으로 채울수록 최소
'''

n, k = map(int, input().split())

coins = [int(input()) for _ in range(n)]
# 가장 큰 코인부터 나누기위해 뒤집기
coins.reverse()
count = 0

# 가장 큰 코인부터
for i in coins:
    count += k//i
    k %= i
    # 채워야할 돈이 0이되면 종료
    if k==0:
        break
        
print(count)
