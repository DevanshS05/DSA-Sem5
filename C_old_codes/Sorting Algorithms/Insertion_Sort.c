/*
Divides the given array into a sorted and unsorted sub-array
Pass-by-pass inserts an element of the unsorted sub-array into its correct index position
*/
#include<stdio.h>
int main(){
	int size=0,temp=0,i=0,j=0;
	printf("Enter the size of the array: ");
	scanf("%d", &size);
	int arr[size];
	
	for(i=0;i<size;i++){
		printf("\nPlease enter the element no %d: ",i+1);
		scanf("%d",&arr[i]);
	}
	//To check the number of passes and comparisons
	int pass=0,comp=0,swap;
	
	//Implementation of insertion sort alogrithm
	for(i=1;i<size;i++){
		for(j=i;j>=0;j--){
			comp++;
			if(arr[j-1]>arr[j]){
				temp = arr[j-1];
				arr[j-1] = arr[j];
				arr[j] = temp;
				swap++;
			}
		}
		pass++;
	}
	printf("\nThe number of passes = %d and the number of swaps = %d and no. of comparsions = %d",pass,swap,comp);
	printf("\nThe sorted array is as follows: ");
	for(i=0;i<size;i++) printf("%d ",arr[i]);
	return 0;
}
