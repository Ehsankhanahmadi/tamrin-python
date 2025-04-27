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
# 3 => sets = moratab {}
# 4 => dictionarys = customise ghabeleh taghir {object}
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