#include<stdio.h>
#include<stdlib.h>
#define SIZE 100
void enqueue();
void dequeue();
void show();
int inp_arr[SIZE];
int rear=-1;
int front=-1;
int main()
{
int ch;
while(1)
{
printf("1:enqueue operation\n");
printf("2:dequeue operation\n");
printf("3:display the queue\n");
printf("4:exit\n");
printf("Enter your choice of operation: ");
scanf("%d",&ch);
switch(ch)
{
case 1:enqueue();
       break;
case 2:dequeue();
       break;
case 3:show();
       break;
case 4:exit(0);              
default:
printf("\nincorrent choice");
}
}
return 0;
}
void enqueue()
{
int insert_item;
if(rear==SIZE-1)
printf("Overflow\n");
else
{
if(front==-1)
front=0;
printf("element to be inserted in the queue:");
scanf("%d",&insert_item);
rear=rear+1;
inp_arr[rear]=insert_item;
}
}
void dequeue()
{
if(front==-1||front>rear)
{
printf("underflow\n");
return;
}
else
{
printf("element deleted from the queue:%d\n",inp_arr[front]);
front=front+1;
}
}
void show()
{
if(front==1)
printf("empty queue\n");
else
{
printf("queue:\n");
for(int i=front;i<=rear;i++)
printf("%d",inp_arr[i]);
printf("\n");
}
}
