'''
Write a Python program to remove all elements from a given list that are present in another list.
Original lists:
list1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2: [2, 4, 6, 8]
Remove all elements from 'list1' present in 'list2:
[1, 3, 5, 7, 9, 10]
'''

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [2, 4, 6, 8]

for i in list1:
    for j in list2:
        if i == j: # checks if both elements are the same
            list1.remove(i) # removes the elements that are the same

print(f"The new list is {list1}")
