#program to implement binary search in a given array
import sys

size = int(input("Please enter the size of the list: "))
myList = list()
for i in range(0,size):
    myList.append(int(input("Please enter the element no {}: ".format(i+1))))

num = int(input("Please enter the number you want to search for: "))
for i in range(0,size):
    if myList[i]==num:
        print("Element exists in list at index {}".format(i))
        sys.exit() #Since the number has been found, no point of executing further
print("Element does not exist in list")
                
