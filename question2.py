'''
Write a Python program to check if each number is prime in a given list of numbers. Return True if all numbers are prime otherwise False.
Sample Data:
([0, 3, 4, 7, 9]) -> False
([3, 5, 7, 13]) -> True
([1, 5, 3]) -> False
'''
import math
tuple1 = (3, 5, 7, 13)


def fun_x(tuple1):
    is_prime=False
    for i in range(0, len(tuple1)):
        is_prime=check_prime_number(tuple1[i])
        print(tuple1[i],is_prime)
        
        if not is_prime:
            return False
        
    if is_prime:
            return True
            
            
def check_prime_number(num):
    if num < 2:
        return False
    
    for i in range(2, math.isqrt(num) + 1):
        if num % i == 0:
            return False
    return True
        
            
            

        
print(fun_x(tuple1))

