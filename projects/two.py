num = int(input("please enter a number two : "))
num1 = int(input("please enter a number one  : "))
num2 = num
num3 = num
sum = 1
array = []
if(num == 1):
    print(sum)
else:
    while(num2 > num1):
        num2 -= 1
        sum = 1
        while(num > 1):
            if(num % 2 == 0):
                num /= 2
                sum += 1
            else:
                num = num*3 + 1
                sum += 1
        num = num2
        array.append(sum)

array.sort(reverse=True)
print(num1 , num3 , array[0])

# 1 10 20
# 100 200 125
# 201 210 89
# 900 1000 174