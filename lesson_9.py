def WriteHelloWorld(n):
    if n > 0:
        print(" Hello World")
        n-=1
        WriteHelloWorld(n)
def FactorialRecursion(n):
    if n == 0:
        return 1
    return n * FactorialRecursion(n - 1)
def FactorialCycle(n):
    number = 1
    for i in range(1, n+1):
        number*=i
    return number
def fibonacci(n):
    if n == 2 or n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
 
def reversearray(array):
    if not array:
        return []
    return [array.pop()] + reversearray(array)
def gcd(x , y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)
    
print(gcd(20,12))         
        
array = [1,3,5,8]
print(reversearray(array))
print(FactorialCycle(5))