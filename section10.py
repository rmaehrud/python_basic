#section10
# 파이썬 예외처리의 이해

# 예외 종류
# 문법적으로 에러가 없지만, 코드 실행 (런타임)프로세스에서 발생하는 예외처리 중요


# StntaxError: 잘못된 문법

# print('Test)
# if True
# x => t

#NameError : 참조변수 없음

a= 10
b= 15

# print(c)
# ZeroDivsionError : 0 나누기 에러
# print(10/0)

# IndexError : 인덱스 범위 오버
x=[10,20,30]
print(x[0])
# print(x[3]) # 예외 발생

# KeyError
dic= {'name':'kim','Age':33,'City':'seoul'}

print(dic.get('hobby'))

#AttributeError : 모듈, 클래스에 있는 잘못된 속성 사용시에 에러
import time
print(time.time())
# print(time.sss())

#valueErrir : 참조 값이 없을 때 발생
x=[1,5,6]

# x.remove(10)


#FileNotFoundError

# f= open('test.txt','r') 파일이 없을 때

# TypeError

# x= [1,2]
# y = [1,2]
# z= 'test'
# print(x+list(z))

# 항상 예외가 발생하지 않을 것으로 가정하고 먼저 코딩
# 런타임 예외가 발생시 예외 처리 코딩 권장

# 예외 처리 기본 
# try : 에러가 발생할 가능성이 있는 코드 실행
# except : 에러명 1
# except : 에러명 2
# else : 에러가 발생하지 않았을 경우 실행
# finally : 항상 실행

# 예제 1
name = ['Kim', 'Lee', 'Park']

try:
    z = 'Kim'
    x = name.index(z)
    print('{} Found it! in name'.format(z,x+1))
except ValueError:
    print('Not found it! - Occurred ValueError!')
else:
    print('Ok! else!')


# 예제 2 
try:
    z = 'Kim'
    x = name.index(z)
    print('{} Found it! in name'.format(z,x+1))
except:
    print('Not found it! - Occurred Error!')
else:
    print('Ok! else!')


# 예제 2 
try:
    z = 'Kims'
    x = name.index(z)
    print('{} Found it! in name'.format(z,x+1))
except:
    print('Not found it! - Occurred Error!')
else:
    print('Ok! else!')
finally:
    print('finally')




# 예제 4
# 예외 처리는 하지 않지만, 무조건 수행되는 코딩 패턴
try:
    print('Try')
finally:
    print('ok Finally!!')



# 예제 5
try:
    z = 'Kim'
    x = name.index(z)
    print('{} Found it! in name'.format(z,x+1))
except ValueError :
    print('Not found it! - Occurred valueError!')
except IndexError:
    print('Not found it! - Occurred indexError!')
except Exception:
    print('Not found it! - Occurred exceoption!')
else:
    print('Ok! else!')
finally:
    print('finally')

# 예제6
# 예외 발생 : raise
# raise 키워드로 예외 직접 발생

try:
     a= '333'
     if a=='Kim':
         print(['허가'])
     else:
         raise ValueError
except ValueError:
    print('문제 발생!')
except Exception as f:
    print(f)
else:
    print('ok!')