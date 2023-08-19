/*
The given programs implements bubble sort.
Improvisation : If the array is already sorted, then there is no need to sort it.
*/
#include<stdio.h>
#include<stdbool.h>
int main(){
	int size=0,i,j,counter=0;
	printf("Please enter the size of the array: ");
	scanf("%d",&size);
	int arr[size]; //Declaring an array of the given size
	for(i=0;i<size;i++){
		printf("\nPlease enter the element at index %d: ",i+1);
		scanf("%d",&arr[i]);
	}
	
	//Checking if the array is already sorted
	if(size==0 || size==1){
		printf("\nThe array is already sorted!");
		return 0; // Exit from the program
	}
	bool flag=true; //Assumption is that array is already sorted
	for(i=0;i<size-1;i++){
		if(arr[i]>arr[i+1]) {flag=false;break;} //If the array is unsorted at any point
		}
	
	if(flag){
		printf("\nArray is already sorted!");
		return 0;
	}
	
	//Sorting the given array using bubble sort
	for(i=0;i<size-1;i++){
		for(j=0;j<size-i-1;j++){
			if(arr[j]>arr[j+1]){
				int temp = arr[j];
				arr[j] = arr[j+1];
				arr[j+1] = temp;
				counter++;
			}
		}
	}
	printf("\nThe value of i is %d",i);
	printf("\nThe value of counter is %d",counter);
	printf("\nThe given array after sorting is: \n");
	for(i=0;i<size;i++) printf("%d ",arr[i]);
	return 0;
}
