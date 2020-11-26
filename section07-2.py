# section2
# 파이썬 클래스 상세 이해
# 상속, 다중상속

#예제 1
# 상속 기본
# 슈퍼클래스(부모) 및 서브클래스(자식) -> 모든 속성 메소드 사용 가능 

# 라면 -> 속성(종류, 회사, 맛, 면 종류, 이름): 부모클래스
# 신라면,진라면, 너구리 : 자식클래스

class Car:
    """parent class"""
    def __init__(self, tp, color):
        self.type = tp
        self.color = color

    def show(self):
        return 'car class "Show Method!"'

class BmwCar(Car):
    """Sub Class"""
    def __init__(self, car_name, tp, color):
        super().__init__(tp,color)
        self.car_name=car_name

    def show_model(self) -> None:
        return "Your Car Name : %s" % self.car_name


class BenzCar(Car):
    """Sub Class"""
    def __init__(self, car_name, tp, color):
        super().__init__(tp,color)
        self.car_name=car_name

    def show_model(self) -> None:
        return "Your Car Name : %s" % self.car_name

    def show(self):
        print(super().show())
        return "car Info : %s %s %s" %(self.car_name, self.type, self.color)


# 일반 사용
model1 = BmwCar('520d', 'sedan', 'red')
print(model1.color) # Super
print(model1.type) # Super
print(model1.car_name) # Sub
print(model1.show()) # Super
print(model1.show_model()) # Sub
print(model1.__dict__)

# Method Overriding(오버라이딩)
model2 = BenzCar('220d','suv','black')
print(model2.show())

# Parent Method Call
model3 = BenzCar('350s','sedan','silver')
print(model3.show())

# Inheritance Info
print(BenzCar.mro()) # 상속정보를 리스트 형태로 알려줌

# 예제 2
# 다중 상속
class x():
    pass
class y():
    pass
class z():
    pass

class A(x,y):
    pass

class B(y,z):
    pass

class M(B,A,z):
    pass

print(M.mro())

# 너무나 복잡한 다중상속은 해석하기 어려움이 따름