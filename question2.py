'''
Write a Python program to check if each number is prime in a given list of numbers. Return True if all numbers are prime otherwise False.
Sample Data:
([0, 3, 4, 7, 9]) -> False
([3, 5, 7, 13]) -> True
([1, 5, 3]) -> False
'''

tuple1 = (0,3,4,7,9)
tuple2 = (3,5,7,13)
tuple3 = (1,5,3)


def fun_x(tuple1):


    for i1 in range(0, len(tuple1)):
        x = tuple1[i1]%2
        if x == 5:
            return True
        else:
            return False


def fun_y(tuple2):


    for i2 in range(0, len(tuple2)):
        y = tuple2[i2]%2
        if y == 5:
            return True
        else:
            return False


def fun_z(tuple3):


    for i3 in range(0, len(tuple3)):
        z = tuple3[i3]%2
        if z == 5:
            return True
        else:
            return False
        
    # I know half of 1 is 0.5, but its still returning False

        
print(fun_x(tuple1))
print(fun_y(tuple2))
print(fun_z(tuple3))
