#include <stdio.h>
int main(){
	int arr[] = {1,2,3,4,5,6,7,8,9,10};
	printf("Please enter the element you want to search for: ");
	int num = 0;
	scanf("%d",&num);
	int idx=-1, i=0;
	for(;i<10;i++){
		if(arr[i]==num) idx=i;
	}
	idx==-1?printf("\nElement not found!"):printf("\nElement found at index position: %d",idx);
	return 0;
}
