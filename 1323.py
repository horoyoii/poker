"""
# class 이해
num = []
print(type(num ))
num2 = list(range(10))
print(num2)
print(type(num2))
cha = list("aaa")
print(cha)
print(type(cha))
# num, num2, cha 는 list의 인스턴스이다.
# 클래스 : 인간 / 인스턴스 : 나, 너 등등

##### 클래스만들기 #####
class Human():
    '''사람'''

## 클래스로 인스턴스 만드는 방법
person1 = Human()
person2 = Human()

print(type(person1))
## person1의 클래스는 Human이다. 

person1.language = "한국어"
person2.language = "English"
print(person1.language)
print(person2.language)

person1.name = "한국인"
person2.name = "미국인"

## 클래스를 정의하면 language나 name 혹은 행동도 클래스 안에 정의해서 쓸 수가 있다.

def speak(person):
    print("{}이 {}로 말을 합니다.".format(person.name, person.language))

speak(person1)  

# 클래스에 함수 담아주기
Human.speak = speak
person1.speak() # 이렇게 바로 쓸 수 있다.


class Human() :
    '''인간'''

person = Human()
person.name = "철수"
person.weight = 60.5
# 이렇게 매번 하면 귀찬ㄷㅎ다.abs

def create_human(name, weight) :
    person = Human()
    person.name = name
    person.weight= weight
    return person
Human.create = create_human # 위의 만든 함수를 클래스에 넣어준다.
person1 = Human.create("영희", 45.5)

def eat(person):
    person.weight += 0.1
    print("{}가 먹어서 {}kg가 되었습니다.".format(person.name, person.weight))
def walk(person):
    person.weight -= 0.1
    print("{}가 걸어서 {}kg가 되었습니다.".format(person.name, person.weight))

Human.eat = eat
Human.walk = walk

person1.eat()
person1.walk()
person1.eat()


#### 클래스에 바로 함수를 넣어준다. 메소드~
class Human() :
    '''인간'''
    def __init__(self,name,weight) : # 인잇을 통해 create함수를 대체할 수 있다. + 인스턴스 선언과 동시에 실행되는 함수이므로
        ''' 초기화 함수'''
        #print("__init__ 실행")
        self.name = name
        self.weight= weight


    def __str__(self) :
        '''문자열화 함수'''
    
    def eat(self):
        self.weight += 0.1
        print("{}가 먹어서 {}kg가 되었습니다.".format(self.name, self.weight))
    def walk(self):
        self.weight -= 0.1
        print("{}가 걸어서 {}kg가 되었습니다.".format(self.name, self.weight))
    def speak(self, message) :
        print(message)

## 메서드의 첫번째 인자는 self로 둔다.
#person1 = Human.create_human("영희", 45.5)

#person1.eat() # eat함수에 매개변수를 넣어주지 않아도 인스턴스를 인자로 받아간다. 그래서 아무것도 적지 않아도 된다.
#person1.walk()
#person1.eat()
#person1.speak("배부르다") # 그래서 메서드에는 인자 두개가 있지만 적을 때는 self를 생략하고 적어주면 된다.

### 클래스에서 사용가능한 특수한 메서드 : __inti__
person3 = Human("철수", 60) # 인스턴스를 만드는 순간에 자동으로 호출이 되는 함수 __init__
print(person3.name)
"""
## 클래스 상속의 개념
class Animal():
    def __init__(self, name) :
        self.name = name # 속성

    def walk(self) :
        print("걷는다.")
    def eat(self):
        print("먹는다.")
    def greet(self):  # 이 메서드를 다른 클래스에 오버라이드한다.
        print("{} 이/가 인사한다.".format(self.name)) 


class Cow(Animal):
    ''''소'''
    

class Human(Animal) : # 클래스의 괄호안에 다른 클래스를 넣는 것 상속
                        # 상속하게되면 부모클래스의 메서드를 그대로 사용할 수 있다.
    def __init__(self,name,hand):
        super().__init__(name) # name이라는 매개변수는 부모클래스가 처리하도록하고
        self.hand =hand         # hand만 처리한다.
    ## 오버라이드된 메서드를 부모 클래스의 메서드로 쓰고 싶을 때 super().을 쓴다.
    
    def wave(self):
        print("{}을 흔들면서".format(self.hand), end=" ")
    def greet(self):  # 이 메서드를 부모클래스와 다르게 정의했다. 자식클래스의 greet메서드가 부모의 메서드를 오버라이드했다.(덮어쓰다)
        self.wave()
        super().greet()

class Dog(Animal): 
    
    def wag(self):
        print("꼬리를 흔들면서", end=(' ')) 
    def greet(self):
        self.wag()
        super().greet() # 자식클래스에서 오버라이드된 메서드를 부모메서드로서 쓰고 싶을 떄 super().메서드로 입력
## Dog class에 낭비되는 코드가 있다.
## animal class에서 받아온다.
person1 = Human("철수", "오른손")
person1.walk()
person1.eat()
person1.greet()

dog1 = Dog("발발이")
dog1.walk()
dog1.eat()

dog1.greet()

cow = Cow("소소")
cow.greet()


print(__name__)
