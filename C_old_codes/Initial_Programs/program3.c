/*
This program checks whether the given number is palindrome or not
( A given number is said to be palindrome when it reads the same backwards and forwards )
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
	revnum==temp?printf("\nThe given number is palindrome"):printf("\nThe given number is not a palindrome");
	return 0;
}
