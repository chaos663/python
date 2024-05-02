# Chapter02-1
# 파이썬 완전 기초
# Print 사용법
# 참조 : https://www.python-course.eu/python3_formatted_output.php


# """ 
# 참고 : Escapse 코드
# \n  : 개행
# \t : 탭
# \\ : 문자
# \' : 문자
# \" : 문자
# \000 : 널 문자
# ...
# """


# 기본 출력
print('Python Start!')
print("Python Start!")
print('''Python Start!''')
print("""Python Start!""")



print()


# seperator 옵션(출력시 구분자)
print('P','Y','T','H','O','N',sep='|')
print('010','7777','1234',sep='-')
print('python','google.com',sep='@')


print()


# end  옵션
  
print("Welcome to",end=' ')
print("IT News", end='')
print("Web Site")

# file 옵션
# import -> 파이썬에서 예약어
import sys

print("Learn Python", file=sys.stdout)
print()

# format 사용(d == digit , s == string , f == float) 
# %s는 % 뒤의 인자는 s니까 string이 와야하는데, 뒤 인자를 순차적으로 대체해서 출력
# 많이 사용하는 문법
print('%s %s' % ('one','two'))   # one two 출력
print('{} {}'.format('one','two')) # one two 출력, 위와 같은 출력 값
print('{1} {0}'.format('one','two')) # two one 출력, 괄호안에 index를 명시

# 10은 자릿수를 의미, s는 String(문자열)을 의미
print('%10s' % ('nice')) # 출력 :      nice(공백포함)
print('{:>10}'.format('nice')) # 출력 :      nice(공백포함)
# - 를 붙이면 왼쪽부터 채우고 나머지 공백으로 채움, 등호를 빼도 같음 
print('%-10s' % ('nice')) # 출력 :nice      (공백포함)
print('{:10}'.format('nice')) # 출력 :nice      (공백포함)

print('{:_>10}'.format('nice')) # 등호 옆에 있는 문자로 채워진다. 출력 : ______nice
print('{:^10}'.format('nice')) # ^를 붙이면 중앙정렬 , 출력 :    nice    

print('%.5s' % ('nice'))
# .를 붙이면 5글자(slicing)을 해서 출력
print('%.5s' % ('pythonStudy')) # 공간이 5개

print('{:10.5}'.format('PythonStudy')) # 공간이 10개, 5개만 슬라이싱

# %d 정수부 출력
print('%d %d' % (1,2))
print('{} {}'.format(1,2))

print('%4d' % (42))
print('{:4d}'.format(42)) # 정수는 d를 붙여줘야한다. 문자는 안붙여도 됨

print()

# %f 실수부 출력
print('%1.8f' % (3.123123213232131))  # f앞에 붙는 1의 의미는 정수부 자릿수, 8은 소수부 자릿수
print('{:1.8f}'.format(3.123123123213))


print('%06.2f' % (3.141592653589793)) # 06은 정수부 6자리에 나머지는 0으로 채움, 소수부는 2자리만 표현
print('{:06.2f}'.format(3.141592653589793))