#include<stdio.h>
int randomNum(int l, int h){
	return rand()%(h-l+1)+l;
}
int main(){
	int i=0;
	for(;i<10;i++) printf("%d ", randomNum(10,25)); //Prints 10 random numbers between 5 and 25
	return 0;
}
