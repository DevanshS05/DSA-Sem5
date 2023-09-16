#include<stdio.h>
#include<string.h>

struct Person{
	int age[1];
	char name[20];
};

void birthday(struct Person *ptr){
	printf("Happy Birthday %s",ptr->name);
	ptr->age[0] = ptr->age[0]+1;
}

int main(){
	struct Person susan;
	susan.age[0] = 23;
	strcpy(susan.name,"Susan Mary");
	birthday(&susan);
	printf("Name:%s Age:%d",susan.name, susan.age[0]);
	return 0;
}
