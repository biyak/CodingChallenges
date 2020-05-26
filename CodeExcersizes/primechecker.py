#prime number checker bruteforce

def isPrime(n):
    #takes n and checks if its prime, returns true or false

    #divides n from 2 to n-1

    if n == 1:
        return False
    if n == 2:
        return True

    divisor = 2
    
    while divisor != n:
        if (n%divisor) == 0:
            return False
        else:
            divisor = divisor + 1

    return True

def recIsPrime(n):
    if n == 1:
        return False
    if n == 2:
        return True

def divisor(n, div):
    
    
