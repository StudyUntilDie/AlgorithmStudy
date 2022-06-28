'''
항상 이전사람들까지 걸린 시간을 계속 누적해서 더해야한다.
5명 [p1, p2, p3, p4, p5]일때
p1 + (p1+p2)+(p1+p2+p3)+(p1+p2+p3+p4)+(p1+p2+p3+p4+p5)
-> p1*5 + p2*4 + p3*3 + p4*2 + p5*1

이때 p를 정렬해야 값이 최소가 된다.
'''

n = int(input())

p = list(map(int, input().split()))
p.sort()

time = 0
for i in range(1, n+1):
#     print('p[',(-i),']*',i)
    time += (p[-i]*i)

print(time)
