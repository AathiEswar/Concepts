def greater(a,b):
    if a>b:
        return a
    else :
        return b

def smaller(a,b):
    if a<b:
        return a
    else:
        return b

def even_or_odd(a,b):
    if a % 2 == 0 and b % 2 == 0:
        return smaller(a,b)

    else:
        return greater(a,b)

a = int(input("Enter number1:"))
b = int(input("Enter number2:"))
result = even_or_odd(a,b)

print(result)