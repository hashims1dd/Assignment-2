'''
Write a Python program to pack consecutive duplicates of a given list of elements into sublists.
Original list:
[0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
After packing consecutive duplicates of the said list elements into sublists:
[[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]
'''

list1 =  [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
list2 = []


def fun(list1):

    for i in list1:
        for j in list1:
            if i == j:
                list2.append(i)



# I didnt have time to finsih this one, and I need help on it; Sorry Muzafar
