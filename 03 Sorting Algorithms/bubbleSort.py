#Program to implement bubble sort
import random

def ran(num):
    return random.randint(0,num)

def sort(lst):
    for i in range(0,len(lst)-1):
        swap=False
        for j in range(0,len(lst)-i-1):
            if lst[j]>lst[j+1]:
                swap=True
                temp = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = temp
        if swap==False:
            break
    return lst

def test(testCaseSize, testCaseCount):
    count=0
    for count in range(0,testCaseCount):
        lst=[]
        for i in range(0,ran(testCaseSize)):
            lst.append(ran(25))
        compList = list(lst)
        compList.sort()
        lst=sort(lst)
        if lst==compList:
            print("Test #{}Passed!".format(count+1))
            count+=1
        else:
            print("Test #{} Failed!".format(count+1))
        print("Expected",compList)
        print("Actual",lst,"\n")
    return count

testCaseSize, testCaseCount = 5,100
print("{} out of {} testcases were successful.".format(test(testCaseSize,testCaseCount),testCaseCount))

