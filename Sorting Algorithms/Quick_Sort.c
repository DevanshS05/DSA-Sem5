/*
Program for implementation of quick sort using recursion
Working :
- Selects a pivot from the array and arranges all elements all the pivot 
s.t. elements to left < pivot and
elements to right > pivot
- Recursively calls the function again to repeat the same for the given two sub-arrays
 (sub-arrays are obtained by splitting around the pivot)
- Ultimately, we will obtain the sorted array

#We are not using pointers because in C arrays are called by "reference"
*/
#include<stdio.h>
void sort(int arr[], int low, int high){
	//printf("\nThe current array is: ");
	//int v=low;
	//for(;v<=high;v++) printf("%d ",arr[v]);
	//printf("with low:%d and high:%d",low,high);
	if(low>=high) return;
	
	int start=low, end=high, mid=0,pivot=0,temp=0;
	mid = (start+end)/2;
	pivot = arr[mid];
	
	while(start<=end){
		while(arr[start]<pivot) start++;
		while(arr[end]>pivot) end--;
		if(start<=end){
			temp = arr[end];
			arr[end] = arr[start];
			arr[start] = temp;
			start++;
			end--;
		}
	}
	
	//Pivot at correct index, sort the two halves of the array
	sort(arr,low,end);
	sort(arr,start,high);
}

int main(){
	int size=0,i=0;
	printf("Please enter the size of the array: ");
	scanf("%d",&size);
	
	int arr[size];
	for(i=0;i<size;i++){
		printf("\nPlease enter the element no %d: ",i+1);
		scanf("%d",&arr[i]);
	}
	
	//Call the sorting function
	sort(arr,0,size-1);
	
	printf("\nThe array after sorting is: ");
	for(i=0;i<size;i++) printf("%d ",arr[i]);
	
	return 0;
}
