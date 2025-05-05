# class MyClass :
#     # test = 0
#     def __init__(self,name,lname):
#         # print("hello")
        # self.a = 2 # public
        # self._a = 2 # protect => use in child and parend
        # self.__a = 2 # private => use just in parent
        # self.name = name
        # self.lname = lname
#         # MyClass.test += 1

#     def test(self,t):
#         print(self.name)
#         print(self.lname)
#         print(t)

# class child(MyClass):
#     def __init__(self, name, lname, age):
#         super().__init__(name, lname)
#         self.age = age

#     def agef(self):
#         print(f"this is age {self.age} and name {self.name}")

# test = MyClass()
# test2 = MyClass()
# print(test.x)
# print(test2.x)
# test = MyClass("ehsan","khan")
# print(test.name+' '+test.lname)
# myclass = MyClass("ehsan","khan")
# myclass.test("this is s test text")
# myclass.name = "reza"
# # del myclass.lname
# myclass.test("hi reza")
# vch = child("ehsan","khanahmadi",19)
# print(vch.name+" "+vch.lname)
# print(vch.age)
# vch.test("vch")
# vch.agef()


# oop iterator
# class myIterator:
#     def __iter__(self):
#         self.a = 1
#         return self
    
#     def __next__(self):
#         if self.a < 10:
#             x = self.a
#             self.a += 1
#             return x
    
# test = myIterator()
# iterOne = iter(test)
# print(next(iterOne))
# print(next(iterOne))
# print(next(iterOne))
# print(next(iterOne))
# print(next(iterOne))
# print(next(iterOne))


# seter and geter and deleter
class person :
    def __init__(self):
        self.__age = 19

    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self,value):
        self.__age = value

    @age.deleter
    def age(self):
        del self.__age

ehsna = person()

print(ehsna.age)
ehsna.age = 20
print(ehsna.age)
# del ehsna.age
# print(ehsna.age)
