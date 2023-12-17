numbers = [    
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527
    ]
'''
Write a Python program to print all even numbers from a given list
of numbers in the same order and stop printing any after 237 in the sequence.
loops
conditon
use while loops

for loopp with range functiion usage
'''

for i in numbers:
    if i == 237:
        break
    if i%2 == 0:
       print(i)


for i in range(0, len(numbers)):
    if numbers[i] == 237:
        break
    if numbers[i]%2 == 0:
        print(numbers[i])
    

count = 0

while count < len(numbers):
    if numbers[count] == 237:
        break
    if numbers[count]%2 == 0:
        print(numbers[count])
    count += 1        

# ------------------------------------------------------------
# Global variables
# ------------------------------------------------------------
count = 1
number = 1
# ------------------------------------------------------------
# Main program
# ------------------------------------------------------------
number = int(input ("Enter a number 1 to 12: "))

# =====> Complete the brackets
if number < 1:
    print("Number is too small")
# =====> Complete the brackets
elif number > 12:
    print("Number is too large")
else:
    # =====> Complete the brackets
    while count <= 12:
        #printiing tabel of given numbeer 
        print(str(number) + " x " + str(count) + " = " + str(count * number))
        # =====> Add a line to keep the loop going around
        count +=1

