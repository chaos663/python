# Chapter02-1-ex1
# 파이썬 완전 기초
# print 사용법
# 파이썬 3가지 print formatting
# 자주 나오는 질문 참고
# 참조 : https://www.python-course.eu/python3_formatted_output.php
"""
\n  : 개행
\t : 탭
\\ : 문자
\' : 문자
\" : 문자
\000 : 널 문자
...
"""

### 3가지 Format Practices

x = 50
y = 100
text = 308276567
n = 'Lee'

# 출력1, % mapping
ex1 = 'n = %s, s = %s, sum = %d' % (n, text, (x+y))
print(ex1)

# 출력 2, formatting
ex2 = 'n = {n}, s = {s}, sum = {sum}'.format(n=n,s=text,sum=x+y)
print(ex2)

# 출력 3, f String 방법
ex3 = f'n = {n}, s = {text}, sum = {x+y}'
print(ex3)

# 주로 많이 사용하는 방법은 2와 3번

# 구분 기호 사용
m = 1000000000
# 천 단위로 , 로 나누어져 나옴
print(f'm : {m:,}')

print()

# 정렬
# ^ : 가운데 정렬 , < : 왼쪽 정렬 , > : 오른쪽 정렬

t = 20
print(f't : {t:10}')
print(f't center : {t:^10}') # 가운데 정렬
print(f't center : {t:>10}') # 오른쪽 정렬
print(f't center : {t:<10}') # 왼쪽 정렬

print()
print()

print(f't center : {t:*^10}') # 10자리,가운데 정렬, ^앞에 있는 문자로 빈칸을  채운다는 의미 출력 : ****20****
print(f't center : {t:#<10}') # 출력 : 20########