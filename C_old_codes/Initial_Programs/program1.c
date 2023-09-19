/*
This program swaps two variables without using a third variable
x = x+y
y = x-y
x = x-y
*/
#include <stdio.h>
int main(){
	int num1=0, num2=0;
	printf("Enter the first number: ");
	scanf("%d",&num1);
	printf("\nEnter the second number: ");
	scanf("%d",&num2);
	//Standardised process for swapping of two numbers
	num1 = num1 + num2;
	num2 = num1 - num2;
	num1 = num1 - num2;
	printf("\nThe numbers after swapping are: %d and %d",num1,num2);
	return 0;
}
