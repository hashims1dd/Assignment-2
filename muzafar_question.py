'''
Write a Python program to replace the last element in a list with another list.
Sample data : 
Expected Output: [1, 3, 5, 7, 9, 2, 4, 6, 8]
'''

list1 = [1, 3, 5, 7, 9, 10]
list2 = [2, 4, 6, 8]
list3 = []

for i in range(0, len(list1)):
    
    if list1[i] == list1[-1]:
        for j in list2:
            list3.append(j)
        break
    list3.append(list1[i])
    
            
            
print(list3)
