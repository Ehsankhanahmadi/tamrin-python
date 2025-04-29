num = int(input("please enter a number :"))
sum = 0

while(num > 1):
    if(num % 2 == 0):
        num /= 2
        sum += 1
    else:
        num = num*3 + 1
        sum += 1

print(sum)

# 10 / 2 = 5
# 5 * 3 + 1 = 16
# 16 / 2 = 8 
# 8 / 2 = 4
# 4 / 2 = 2
# 2 / 2 = 1