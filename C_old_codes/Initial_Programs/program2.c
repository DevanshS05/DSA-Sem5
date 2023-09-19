/*
This program reverses the given number
*/
#include <stdio.h>
int main(){
//Program to reverse an 'n' digits number using a loop
	int num = 0;
	printf("Please enter the number: ");
	scanf("%d",&num);
	int temp = num;
	int revnum = 0;
	while(num>0){
		int rem = num%10;
		revnum = revnum*10 + rem;
		num=num/10;
	}
	printf("\nThe reversed number is: %d",revnum);
	return 0;
}
