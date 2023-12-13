#Program to implement selection sort
import random

def ran(num):
    return random.randint(0,num)

def sort(lst):
    for i in range(0,len(lst)-1):
        idx=i
        for j in range(i+1,len(lst)):
            if lst[j]<lst[idx]: idx=j
        if idx!=i: 
            temp = lst[i]
            lst[i] = lst[idx]
            lst[idx] = temp
    return lst

def test(testCaseSize, testCaseCount):
    for count in range(0,testCaseCount):
        lst=[]
        for i in range(0,ran(testCaseSize)):
            lst.append(ran(25))
        compList = list(lst)
        compList.sort()
        lst=sort(lst)
        if lst==compList:
            print("Test #{}Passed!".format(count+1))
            return true
        else:
            print("Test #{} Failed!".format(count+1))
            return false
        print("Expected",compList)
        print("Actual",lst,"\n")
      

print(test(10,5))
#lst = [10,9,0,-1,5,3,9,4]
#print(sort(lst))
        
