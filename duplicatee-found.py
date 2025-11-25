def func(num):
    temp = {}
    for n in num:
        if n in temp:
            return True      
        else:
            temp[n] = 1
    return False     

count = int(input("Enter total num: "))

arr = []
for n in range(count):
    arr.append(int(input()))

print(func(arr))
