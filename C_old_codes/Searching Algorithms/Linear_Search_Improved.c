/*
Improvistion of linear search by modification of the algorithm
*/
#include<stdio.h>
int main(){
	int size=0,num=0,i;
	printf("Please enter the size of the array: ");
	scanf("%d",&size);
	int arr[size+1]; //Extra space included
	//Reading the array
	for(i=0;i<size;i++){
		printf("\nPlease enter the element at index %d: ",i+1);
		scanf("%d",&arr[i]);
	}
	//Reading the number to be searched for
	printf("Please enter the number you want to search for: ");
	scanf("%d",&num);
	arr[size] = num;

	for(i=0;i<size+1;i++) if(arr[i]==num) break;
	i==size?printf("\nElement not found!"):printf("\nElement is present at index %d",i+1);
	return 0;
}
