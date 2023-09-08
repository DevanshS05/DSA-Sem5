#include<stdio.h>

struct

struct complex{
	int real;
	int img;
};


int main(){
	struct complex num1;
	num1.real = 5;
	num1.img = 7;
	printf("The number is %d+%di",num1.real,num1.img);
	return 0;
}
