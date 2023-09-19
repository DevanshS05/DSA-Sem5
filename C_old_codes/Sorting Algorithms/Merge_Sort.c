/*Implementation of merge-sort algorithm*/
#include<stdio.h>

void printArray(int arr[], int l, int r){
	int i=l;
	for(;i<=r;i++) printf("%d ", arr[i]);
}

void merge(int arr[], int left, int ptr, int right){
	int n1 = ptr-left+1;
	int n2 = right-ptr;
	
	int leftArr[n1], rightArr[n2];
	int p=0,q=0,r=0;
	for(p=0;p<n1;p++) leftArr[p] = arr[left+p];
	for(q=0;q<n2;q++) rightArr[q] = arr[ptr+1+q];
	
	//Printing the sub-arrays for debugging
//	printf("\nLeft SubArray: ");
//	printArray(arr, left, ptr);
//	printf("\nRight SubArray: ");
//	printArray(arr, ptr+1, right);
	
	p=0,q=0,r=left;
	while(p<n1 && q<n2){
		if(leftArr[p]<=rightArr[q]){
			arr[r++] = leftArr[p++];
		}
		else{
			arr[r++] = rightArr[q++];
		}
	}
	
	//If the left sub-array is not empty
	while(p<n1){
		arr[r++] = leftArr[p++]; 
	}
	//If the right sub-array is not empty
	while(q<n2){
		arr[r++] = rightArr[q++];
	}
}

void mergeSort(int arr[], int l, int r) {
  if (l < r) {

    // m is the point where the array is divided into two subarrays
    int m = l + (r - l) / 2;

    mergeSort(arr, l, m);
    mergeSort(arr, m + 1, r);

    // Merge the sorted subarrays
    merge(arr, l, m, r);
  }
}

int main(){
	int size=0,i=0;
	printf("Please enter the size of the array: ");
	scanf("%d", &size);
	int arr[size];
	for(i=0;i<size;i++){
		printf("\nPlease enter element no %d: ", i+1);
		scanf("%d", &arr[i]);
	}

	mergeSort(arr, 0, size-1);
	
	printf("\nThe array after sorting is: ");
	for(i=0;i<size;i++){
		printf("%d ",arr[i]);
	}
	return 0;
}
