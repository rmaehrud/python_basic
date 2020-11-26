# section07-1
# 파이썬 클래스 상세 이해
# self, 클래스, 인스턴스 변수

# 클래스, 인스턴스 차이 중요 
# 네임스페이스 : 객체를 인스턴스화 할 때 저장된 공간
# 클래스 변수 : 직접 사용, 객체 보다 먼저 생성
# 인스턴스 변수 : 객체마다 별도로 존재, 인스턴스 생성 후 사용한다.

#선언1
# class 클래스명:
#     함수
#     함수
#     함수


# 예제 1
#속성, 메소드
class UserInfo:
    def __init__(self, name):#초기화 코드
        self.name = name
    def user_info_p(self):
        print("Name : ", self.name)


user1 = UserInfo("Kim")
print(user1.name)
user1.user_info_p()
user2 = UserInfo("park")
user2.user_info_p()
    
print(id(user1))
print(id(user2))
print(user1.__dict__)
print(user2.__dict__)

#예제2
# self의 이해
class SelfTest():
    def function1():# 클래스의 직접 호출
        print("function1 called!")
    def function2(self):# 인스턴스 함수
        print(id(self))
        print("function2 called")


self_test = SelfTest()
SelfTest.function1()
self_test.function2()

#예제 3
# 클래스 변수, 인스턴스 변수

class WareHouse:
    #클래스 변수 
    stock_num=0
    def __init__(self, name):
        self.name=name
        WareHouse.stock_num += 1
    def __del__(self):
        WareHouse.stock_num -= 1
user1 = WareHouse('KIM')
user2 = WareHouse('park')
user3 = WareHouse('lEE')
print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)
print(WareHouse.__dict__) # 클래스 네임스페이스, 클래스 변수(공유)





print(user1.stock_num) # 클래스 변수에 까지 접근 가능








