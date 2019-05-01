# class Person:
#     기능 = "숨쉬기"
#     name ="아이유"
    
#     def Print(self): 
#         print(self.기능)
    
#     def say_hello(self):
#         print(f"Hello, {self.name}")
        

# 사람 = Person()
# 남자 = Person()
# # iu.say_hello();

# 사람.기능 = "걷기"

# 사람.Print()
# 남자.Print()

# 사람.say_hello();


# iu.name = "홍길동"

# Person.say_hello(iu)

# print(isinstance(iu, Person))
# print(isinstance(iu, Student))


# class Person:   #class 정의
#     name = "Justin" # member 변수
    
#     def greeting(self): #member method
#         print(f"안녕하세요, {self.name}")
        
# justin = Person() # justin --> Person class의 instance
# justin.greeting()



# class Person:
#     name = "아이유"
#     age = "23"
    
#     def greeting(self):
#         print(f"안녕하세요 저는 {self.name}입니다. 제 나이는 {self.age}입니다.")
        

# iu = Person()
# iu.greeting



# word = "Not Class Member"

# class Something:
#     word = "Class Member"
    
#     def Set(self, msg):
#         self.word = msg
        
#     def Print(self):
#         print(word)
        
# g = Something()
# g.Set("First Message")
# g.Print()



# class Person:
#     name = "허승범"
    
#     def greeting(self):
        
        

class Student:
    
    
    def __init__(self, name, age,  Class):
        self.name = name
        self.age = age
        self.Class = Class

    def learning(self):
        print(f"저는 {self.age}살의 {self.name}이고, {self.Class}을(를) 배우고 있습니다.")

class Teacher:
    
     def __init__(self, name, age,  Class):
        self.name = name
        self.age = age
        self.Class = Class

    def teaching(self):
        print(f"저는 {self.age}살의 {self.name}이고, {self.Class}을(를) 가르치고 있습니다.")

