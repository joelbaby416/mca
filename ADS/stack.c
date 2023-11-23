#include<stdio.h>
#include<stdlib.h>
int stack[100],choice,n,top,x,i;
void push();
void pop();
void display();
int main()
{
top=-1;
printf("Enter the size of the stack");
scanf("%d",&n);
printf("1.Push\n2.Pop\n3.Display\n4.Exit");
do
{
printf("Enter the choice");
scanf("%d",&choice);
switch(choice)
{
case 1:push();
       break;
case 2:pop();
       break;
case 3:disply();
       break;
case 4:exit(0);
       break;
defaut:
printf("Enter a valid choice");
}
}
}
while(choice!=4)
return0;
}
void push()
{
if(top>=n-1)
{
printf("stack is overflow");
}
else
{
printf("Enter value to be pushed");
scanf("%d",&x);
top++;
stack[top]=x;
}
}
void pop()
{
if(top<=-1)
{
printf("stack under flow");
}
else
{
printf("The poped element is %d",stack[top]);
top--;
}
}
void display()
{
if(top>=0)
{
printf("The element in stack");
for(i=top;i>=0;i--)
printf("%d",stack[i]);
}
else
{
printf("stack is empty");
}
}
