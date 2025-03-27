import math
def factorial(x):
    if x==0 or x==1:
        return 1;
    return x * factorial(x-1)

def lambdaFunc(x,n):
    sonuc = (-1)**n
    sonuc*= x**((2*n) + 1)
    sonuc/=factorial((2*n) + 1)
    return sonuc

def sine_x(x,n):
    radians = x * (math.pi / 180)

    result = 0

    for i in range(n):
        result += lambdaFunc(radians, i)

    return result


x = int(input("Enter the x value : "))
n = int(input("Enter the n value : "))
print(sine_x(x,n))
print("*************************************")

value = 0

def func3(n):
    """
This function about summotion and obey the rules.
    """
    global value
    if n == 1:
        value += 1
        return
    value += 1 / n
    func3(n - 1)


func3(2)
print(value)


print(func3.__doc__)
