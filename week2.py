'''
Write a Python program to replace the last element in a list with another list.
Sample data : [1, 3, 5, 7, 9, 10], [2, 4, 6, 8]
Expected Output: [1, 3, 5, 7, 9, 2, 4, 6, 8]
'''

list1 = [1, 3, 5, 7, 9, 10]
list2 = [2, 4, 6, 8]
list3 = []
for i in range(0, len(list1)):

    if (i != len(list1)-1):
        list3.append(list1[i])     
    if i == len(list1)-1:  
        for j in range(0,len(list2)):
            list3.append(list2[j])
            #print(list2[j])
            


print(len(list1))


# [1,3,5,7,9,2,4,6]
# [1,3,5]
# [1,3,5,7,9]

#if (5 != 5):
# [1,3,4,7,9,2,4]
# [1,3,5,7,9,2,4,6,8]
