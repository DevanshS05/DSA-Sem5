#Program to implement insertion sort
import random

def ran(num):
    return random.randint(0,num)


def sort(lst):
    for i in range(1,len(lst)):
        idx=i
        while(idx>=1):
            if lst[idx]<lst[idx-1]:
                temp = lst[idx]
                lst[idx] = lst[idx-1]
                lst[idx-1] = temp
            idx-=1
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
