/*
Implementation of binary search algorithm
*/
#include<stdio.h>
#include<stdbool.h>
int main(){
	int arr[] = {1,2,3,4,5,6,7,8,9,10};
	int high=9,low=0,mid,num;
	bool flag = false;
	printf("Please enter the number you want to search for: ");
	scanf("%d",&num);
	while(high>low){
		mid = (high+low)/2;
		if(arr[mid]==num) {flag=true;break;}
		if(arr[mid]>num) high=mid-1;
		if(arr[mid]<num) low=mid+1;
	}
	flag?printf("\nElement is present at index position %d",mid+1):printf("\nElement is not present!");
	return 0;
}
