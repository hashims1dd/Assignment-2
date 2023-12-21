'''
Write a Python program to extract specified size of strings from a give list of string values.
Original list:
['Python', 'list', 'exercises', 'practice', 'solution']
length of the string to extract:
8
After extracting strings of specified length from the said list:
['practice', 'solution']
'''

list1 =  ['Python', 'list', 'exercises', 'practice', 'solution']
list2 = []

for i in list1:
    if len(i) == 8:
        list2.append(i)

print(list2)
