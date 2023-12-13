#Program to implement quickSort algorithm
import random

def ran(num):
    return random.randint(0,num)

def test(testCaseSize, testCaseCount):
    count=0
    for count in range(0,testCaseCount):
        lst=[]
        for i in range(0,ran(testCaseSize)):
            lst.append(ran(25))
        compList = list(lst)
        if len(lst)>0:
            compList.sort()
            lst=sort(lst,0,len(lst)-1)
        if lst==compList:
            print("Test #{}Passed!".format(count+1))
            count+=1
        else:
            print("Test #{} Failed!".format(count+1))
        print("Expected",compList)
        print("Actual",lst,"\n")
    return count




def sort(lst,start,end):
    if start>=end: return
    
    middle = int((start + end)/2)
    left,right = start,end
    while(left<=right):
        #print(lst,"left={},right={}".format(left,right))
        while(lst[left]<lst[middle]):
            left+=1
        while(lst[right]>lst[middle]):
            right-=1
        if left<=right:
            temp = lst[left]
            lst[left] = lst[right]
            lst[right]=temp
            left+=1
            right-=1

    sort(lst,start,middle-1)
    sort(lst,middle+1,end)
    return lst

lst = [15,22,20]
print(sort(lst,0,len(lst)-1))

testCaseSize, testCaseCount = 10,100
#sprint("{} out of {} testcases were successful.".format(test(testCaseSize,testCaseCount),testCaseCount))


