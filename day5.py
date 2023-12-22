'''
*Write a Python program to find the maximum and minimum values in a given heterogeneous list.
Original list:
['Python', 3, 2, 4, 5, 'version']
Maximum and Minimum values in the said list:
(5, 2)*
'''

list1 = ['Python', 3, 2, 4, 5, 'version']
count = 0

for item in range(0, len(list1)):
    if len(str(list1[item])) < 2 or len(str(list1[item])) > 5:
        count +=1

print(f"{count} have more or less than the minimum")

