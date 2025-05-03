# dar in file tamam nokat python fandamentl hast bahamin tor pishrafteh
# print("hi i am ehsan")

# data types
# string
# print(type("ehsan"))
# boolean
# print(type(True))
# number 
    # int
# print(type(180))
    # float
# print(type(180.8888))
    # complex
# print(type(180j))
# list
# print(type(["ehsan","reza",2,True,9.5]))

# operator
# +
# -
# *
# / => dar python ma taghsim hamoon beh shekleh float ast
# %
# ** => tavan
# // => haman taghsim ast vali int

# variable
# baraieh create iek variable dar python beh shekleh zir amal mikonim 
# baraieh sakhteh subet ham name on baiad ba horoofeh bozorg bashad
# nemitavan bein name ha faseleh gozasht va inkeh ba number va namad shoroonemishavad

# name = "ehsan"
# age = 19
# SUBET = "ehsan" # in sabet nemishavad valieh behtar ast name on insheklii bashad

# type casting in python

# float string ra nemitavan keh beh int tarig kard va inkeh esm ia character ra imitavan adad kard
# mored badi mesl js nist keh string ra dar kenar number bogzarad kolan error midahad

# x = int(3.2)
# x2 = int("83342")
# y = float(3)
# y2 = float("5")
# z = str(3.6)
# print(x , x2 , y , y2 , z)

# slicing in string
# x = "ehsan"
# print(x[1])
# print(x[0:2])
# print(x[:])
# print(x[:3])
# print(x[0:])

# format string 
# n = "ehsan"
# l = "khanahmadi"
# a = 19
# me = f"{n} {l} {a}"
# print(me)
# method string
# text = "hi my name is ehsan"
# text = "hi my name is ehsan my name"
# text = "hi my name is {} an my lastname {}"
# text = "سلام"
# print(text.capitalize())
# print(text.casefold())
# print(text.count("m"))
# print(text.count(" "))
# print(text.find("name"))
# print(text.index('my'))
# print(text.format("ehsan","khanahmadi"))
# print(text.title())
# print(text.upper())
# print(text.lower())
# print(len(text))

# boolean true and false
# print(bool(False))
# print(bool(None))
# print(bool(0))
# print(bool(""))
# print(bool(()))
# print(bool({}))
# print(bool([]))

# comparision 
# == != > < >= <=

# list or array
# ma baraieh zakhireh sazieh array ha dar python 4 ravesh darim
# 1 => lists = moratab ghableh tekrar va ghabeleh taghir []
# 2 => tuples = moratab ghableh tekrar ()
# 3 => sets = moratab nist {}
# 4 => dictionarys = customise ghableh tekrar va ghabeleh taghir {object}
# use list
# listone = ["ehsan","amir","reza","fatemeh","mobina"]
# print(listone[2])
# print(listone[2:4])
# print(listone[-3:-1])

# array = ["ehsan","bahram","reza","elia","Amin","Bahram"]
# arraynum = [1,2,3,4,5]
# array2 = [True,3,"khan"]
# tuple = (3 , "mina")
# print(array)
# print(type(array))
# array[1] = "mahdi"
# print(array)
# array[1:3] = ["mohammad","amin"]
# print(array)
# array[1:3] = ["mohammad"]
# print(array)
# array.insert(1,"amirhosein")
# print(array)
# array[0] = ["ehsan","milad"]
# print(array)
# print(array[0][1])
# array.append(True)
# print(array)
# array.extend(array2)
# print(array)
# array.extend(tuple)
# print(array)
# array.remove("ehsan")
# array.remove(array[1])
# array.pop()
# array.pop(1)
# del array[1]
# del array
# array.clear()
# print(array) 
# array3 = array + array2
# print(array3)
# array.sort()
# array.sort(reverse=True)
# arraynum.sort()
# arraynum.sort(reverse=True)
# print(arraynum)
# test = arraynum
# print(test)
# test2 = arraynum.copy()
# print(test2)
# test3 = list(arraynum)
# print(test3)

# tuples 
# tupleOne = ("ehsan")
# print(type(tupleOne))
# tupleOne = ("ehsan",)
# print(type(tupleOne))
# tupleOne = ("ehsan","reza",2,True,2)
# tupleTwo = ('amir',)
# print(tupleOne)
# print(type(tupleOne))
# tuplrThree = tupleOne + tupleTwo
# print(tuplrThree)
# print(type(tuplrThree))
# print(tupleOne.count(2))
# print(tupleOne.index(True))

# Sets
# x = {"ehsan","amir","reza"}
# x2 = {"amir","mina","reza"}
# y = {1, 2, 3}
# z = ["mehdi","mina","ehsan"]
# print(type(x))
# print("ehsan" in x)
# print("Ehsan" in x)
# print(x)
# x.add("mohammad")
# print(x)
# x.remove("amir")
# print(x)
# z = x.union(y)
# x.update(y)
# print(z)
# print(x)
# y.update(z)
# print(y)
# x.update(z)
# print(x)
# x.intersection_update(x2)
# print(x)
# z = x.intersection(x2)
# print(z)
# x.symmetric_difference_update(x2)
# print(x)
# z = x.symmetric_difference(x2)
# print(z)
# print(x | x2)
# print(x & x2)

# Dictionaries
# dic = {
#     "name":"ehsan",
#     "age":19,
#     "frinds":["reza","amir"],
#     "man":True    
# }
# print(type(dic))
# print(dic)
# print(dic["name"])
# print(dic.get("name"))
# print(dic.keys())
# print(dic.values())
# print(dic.items())
# if "name" in dic :
#     print(dic["name"])
# dic["age"] = 18
# dic.update({"frinds":["reza","amir","mahdi"]})
# print(dic)
# dic["hir"] = "black"
# dic.update({"tall":185})
# print(dic)
# dic.pop("age")
# dic.popitem()
# print(dic)
# del dic["name"]
# del dic
# print(dic)
# dic.clear()
# print(dic)
# dic2 = dic
# dic2["name"] = "amir"
# print(dic)
# dic2 = dic.copy()
# dic2 = dict(dic)
# test = {
#     "name":"test",
#     "age":10
# }
# dic = {
#     "child1":{
#         "name":"ehsan",
#         "age":19
#     },
#     "child2":{
#         "name":'amir',
#         "age": 18
#     },
#     "child3": test
# }
# # print(dic["child1"]["name"])
# print(dic)

# if ... else 
# a = 10
# b = 20
# if (a < b) and (a == b):
#     print("test one")
# elif (b < a) or (a < b) and (b == 20) :
#     print("test two")
# else : 
#     print("else")
# print("a") if a < b else print("b")

# Loops
# i = 1
# while(i < 10):
#     # print(i)
#     i += 1 
#     if(i == 6):
#         continue
#         # break
#     print(i)
#     # i += 1
# # else:
# #     print("error")
# name = ["ehsan","amir","reza"]
# for x in name :
#     print("hi")
#     print(x)
# x = "ehsan"
# for i in x :
#     print(i)
# for i in range(6):
    # print(i)
# for i in range(2,6,2):
#     print(i)
# for i in range(10 , 3 , -1):
#     print(i)

# Functions
# def function(name,lastname):
# def function(name,lastname="khanahmadi"):
    # print(f"hi {name} {lastname}")

# function("ehsan","khanahmadi")
# function(name="amir",lastname="khanahmadi")
# function("ehsan")
# def function(*args):
# def function(fname,lname,*args):
# def function(fname,lname,*args,**kwargs):
    # print(args)
    # for name in args:
    #     print(name)
    # print(f"{fname} {lname}")
    # for frind in args:
    #     print(f"frinds = ({frind})")
    # print(fname)
    # print(lname)
    # print(args)
    # print(kwargs)

# function()
# function("ehsan","amir",2,True)
# function("ehsan","khanahmadi","amir","reza")
# function("ehsan","khan","test","test2",city="mino",tall=185)
# def function(name):
#     for n in name:
#         print(n)

# names = ["ehsna","amir","reza"]
# function(names)
# def function(a,b):
#     a += 1
#     b += 1
#     return a,b
# result = function(1,2)
# print(result)
# print(type(result))
# print(result[1])
# def test():
#     global x
#     x = 19
# test()
# print(x)

# Lambda
# x = lambda a ,b : a * b
# print(x(2,3))
# def function(a):
#     return lambda b : a + b
# x = function(10)
# print(x(2))
# listOne = [1,2,3,4,5]
# listTwo = [6,7,8,9,10]
# x = list(map(lambda a,b: a*b,listOne,listTwo))
# print(x)

# Modules
# def testOne(test):
#     print(f"this is test one {test}")

# dic = {
#     "name":"ehsan",
#     "lastname":"khan"
# }

# Math
# import math
# array = [2,3,1,53,13,12]
# x = min(array)
# y = max(array)
# print(x)
# print(y)
# print(abs(-10))
# print(pow(5,3))
# x = math.floor(1.8)
# y = math.ceil(1.2)
# print(x)
# print(y)

# JSON
# import json
# JSON = """[
#     {
#         "name":"ehsan",
#         "age":19,
#         "frinds":["reza","amir","mahdi"]
#     },
#     {
#         "name":"amir",
#         "age":19,
#         "frinds":["reza","ehsan","mahdi"]
#     }
# ]"""

# dic = {
#     "name":"ehsan",
#     "age":18,
#     "man":True,
# }

# x = json.loads(JSON)
# print(JSON)
# print(x[1]["name"])

# y = json.dumps(dic, indent=2, sort_keys=True)
# y = json.dumps(dic)
# print(dic)
# print(y)

# Error Handling
# try:
#     print(2)
#     print(x)
# except:
#     print("this is error")
# else:
#     print("this is else")
# finally:
#     print("this is finally")

# raise Exception("this is thorw error in python")
# raise NameError('this is name error')
# raise KeyError('this is key error')