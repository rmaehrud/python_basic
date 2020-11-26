# Section02-1
# 파이썬 기초 코딩
# print 구문의 이해

# 기본출력
print('Hello Python!')
print("Hello Python!")
print("""Hello Python!""")
print('''Heool PYSFA''')


print()

# Separator 옵션 사용

print('T','E','S','T', sep='')
print('2019','09','24', sep='-')
print('rmmaehrud','naver.com', sep='@')

# end 옵션 사용
print('Welcome To', end=' ')
print('the black parade', end=' ')
print('the black parade')
print('test')

# format 사용 [] <-대괄호, {}<-중괄호,()<-소괄호
print('{} and {}'.format('You','Me'))
print('{0} and {1} and {0}'.format('You','Me'))
print('{a} are {b}'.format(a='You',b='Me'))

#%s : 문자, %d : 정수, %f : 실수
print("%s's favorite number is %d" %('안녕하세요',5))

print('Test1: %5d, price : %4.2f' %(776,6534.123))
print('Test1: {0: 5d}, price : {1: 4.2f}'.format(776, 6534.123))
print('Test1: {a: 5d}, price : {b: 4.2f}'.format(a=776, b=6534.123))

