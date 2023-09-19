#Program to implement binary search
import sys
import math

size = int(input("Please enter the size of the list: "))
myList = list()
for i in range(0,size):
    myList.append(int(input("Please enter the element at pos {}: ".format(i+1))))

num = int(input("Please enter the number you want to search for: "))
low, high = 0, size-1

while(low<=high):
    mid = math.floor(low + (high-low)/2)
    #print("Current midIdx={} and midElement={}".format(mid,myList[mid]))
    if myList[mid]>num:
        high=mid-1
    elif myList[mid]<num:
        low=mid+1
    else:
        print("Element found at index {}".format(mid))
        sys.exit()
print("Given element does not exist in the list")
        
