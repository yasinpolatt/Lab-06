import math
def factorial(x):
    if x==1:
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


def func3(n):
    """
     function  take “n” as a parameter and obey the formula.
    """
    toplam = 0
    while(n!=0):
        toplam += 1/n
        n-=1
    print("Total : " + str(toplam))



func3(5)
print(func3.__doc__)
