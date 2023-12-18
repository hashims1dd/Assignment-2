'''
Write a Python program to count integers in a given mixed list.
Original list:
[1, 'abcd', 3, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
Number of integers in the said mixed list:
6
'''

list1 = [1, 'abcd', 3, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
count = 0

for i in range(0, len(list1)):
    if type(list1[i]) == int: # This line checks if the data type is integer
        count += 1

print(f"There are {count} integers in the list")
