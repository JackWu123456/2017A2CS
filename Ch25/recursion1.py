# option3 Jack Wu

def factorial(n):
    if n==1:
        return 1
    return n * factorial(n-1)

def bunnyEars(bunnies):
    if bunnies == 0:
        return 0
    return bunnies * 2

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)

def bunnyEars2(bunnies):
    if bunnies == 0:
        return 0
    if bunnies%2 ==0:
        return bunnyEars2(bunnies-1)+3
    if bunnies%2 ==1:
        return bunnyEars2(bunnies-1)+2

def triangle(rows):
    if rows==0:
        return 0
    return triangle(rows-1)+rows

def sumDigits(n):
    if n==0:
        return 0
    return n%10+sumDigits(n//10)

def count7(n):
    if n==7:
        return 1
    return n%10//7+count7(n//10)

def count8(n):
    if n==8:
        return 1
    return n%10//8+count8(n//10)
    print(count8(8585))
