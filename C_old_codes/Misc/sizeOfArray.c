#include<stdio.h>
int main(){
//	int arr[] = {1,2,3,4,5,6,7,8,9,10};
	char arr[] = "Its";
	int i=0;
	printf("The size of the array is: %d\n",sizeof(arr)/sizeof(arr[0]));
	for(;i<4;i++) printf("%d ",arr[i]);
	return 0;
}
