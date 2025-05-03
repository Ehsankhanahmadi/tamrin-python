# class MyClass :
#     # test = 0
#     def __init__(self,name,lname):
#         # print("hello")
#         self.name = name
#         self.lname = lname
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