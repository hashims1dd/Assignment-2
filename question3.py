'''
Write a Python program to count the number of sublists that contain a particular element.
Original list:
[[1, 3], [5, 7], [1, 11], [1, 15, 7]]
Count 1 in the said list:
3
Count 7 in the said list:
2
Original list:
[['A', 'B'], ['A', 'C'], ['A', 'D', 'E'], ['B', 'C', 'D']]
Count 'A' in the said list:
3
Count 'E' in the said list:
1
'''

list1 = [[1, 3], [5, 7], [1, 11], [1, 15, 7]]
list2 = [['A', 'B'], ['A', 'C'], ['A', 'D', 'E'], ['B', 'C', 'D']]



def fun_x(list1):


    c1 = 0
    c2 = 0

    for i in list1:
        if i[0] == 1:
            c1 +=1

            if i[-1] == 7:
                c2 +=1
                
    return c1, c2
    #return c2


def fun_y(list2):

    c3 = 0
    c4 = 0

    for j in list2:
        if j[0] == 'A':
            c3 +=1
            
            if all(j[-1]) == 'E':
                c4 +=1

    return c3, c4
    #return c4



x = fun_x(list1)
y = fun_y(list2)

print(x)
print(y)
