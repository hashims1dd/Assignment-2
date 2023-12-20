'''
Write a Python program to check if the elements of a given list are unique or not.
Original list:
[1, 2, 4, 6, 8, 2, 1, 4, 10, 12, 14, 12, 16, 17]
Is the said list contains all unique elements!
False
Original list:
[2, 4, 6, 8, 10, 12, 14]
Is the said list contains all unique elements!
True
'''

list1 = [1, 2, 4, 6, 8, 2, 1, 4, 10, 12, 14, 12, 16, 17]


if len(set(list1)) == len(list1):
    print("They are unique")
else:
    print("They aren't unique")
