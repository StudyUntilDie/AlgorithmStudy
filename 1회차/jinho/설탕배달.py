'''
그리디 알고리즘
5kg 봉지에 최대한 담고
3kg 봉지로 해결

이때 설탕이 9kg일때와 같이 예외가 발생 가능
-> 전체 설탕에서 3씩 빼고(최대 4회) 5의 배수가 되는순간 나누기
'''

n = int(input())

# 몇봉지가 필요한지
bags = 0

while n>=0:
    # 5kg에 담을수있으면 담고 아니면 3kg씩 담기
    if n%5 != 0:
        n-=3
        bags += 1
    else:
        bags += n//5
        n=0
        break
        

if n == 0:
    print(bags)
else:
    print(-1)
