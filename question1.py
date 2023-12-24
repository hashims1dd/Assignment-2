'''
Write a Python program to insert a given string at the beginning of all items in a list.
Sample list : [1,2,3,4], string : emp
Expected output : ['emp1', 'emp2', 'emp3', 'emp4']
'''

list1 = [1,2,3,4,6]
string = "emp"
list2 = []


def func(list1, string):
    for i in range(0, len(list1)):
        z = string + str(list1[i])
        list2.append(z)

    return list2
    print(list2)


print(func(list1, string))
