#include<stdio.h>
#include<stdlib.h>
struct node
{
int info;
struct node *link;
};
struct node*start=NULL;
void traverse()
{
struct node*temp;
if (start==NULL)
printf("\n List is empty");
else
{
temp=start;
printf("The lsit is \n");
while(temp!=NULL)
{
printf("%d-->",temp->info);
temp=temp->link;
}
}
}
void insertatfront()
{
int data;
struct node*temp;
temp=malloc(sizeof(struct node));
printf("\n Enter number to be inserted");
scanf("%d",&data);
temp->info=data;
temp->link=start;
start=temp;
}
void insertatend()
{
int data;
struct node*temp,*head;
temp=malloc(sizeof(struct node));
printf("\n Enter the number to be inserted:");
scanf("%d",&data);
temp->link=0;
temp->info=data;
head=start;
while(head->link!=NULL)
{
head=head->link;
}
head->link=temp;
}
void insertatposition()
{
struct node*temp,*newnode;
int pos,data,i=1;
newnode=malloc(sizeof(struct node));
printf("\n Enter position and data:");
scanf("%d%d",&pos,&data);
temp=start;
newnode->info=data;
newnode->link=0;
while(i<pos-1)
{
temp=temp->link;
i++;
}
newnode->link=temp->link;
temp->link=newnode;
}
void deleteatfirst()
{
struct node*temp;
if(start==NULL)
printf("\n List is empty");
else
{
temp=start;
start=start->link;
free(temp);
}
}
void deleteatend()
{
struct node*temp,*prenode;
if(start==NULL)
printf("\n list is empty");
else
{
temp=start;
while(temp->link!=0)
{
prenode=temp;
temp=temp->link;
}
free(temp);
prenode->link=0;
}
}
void deleteatposition()
{
struct node*temp,*position;
int i=1,pos;
if(start==NULL)
printf("\n list is empty");
else
{
printf("\n Enter position:");
scanf("%d",&pos);
position=malloc(sizeof(struct node));
temp=start;
while(i<pos-1)
{
temp=temp->link;
i++;
}
position=temp->link;
temp->link=position->link;
free(position);
}
}
int main()
{
int choice;
while(1)
{
printf("\n\t1. to see list\n");
printf("\t2. for insertion at starting\n");
printf("\t3. for insertion at end\n");
printf("\t4. for insertion at any position\n");
printf("\t5. for deletion of first element\n");
printf("\t6. for deletion of last element\n");
printf("\t7. for deletion of any element at any position\n");
printf("\t8. to exit\n");
printf("\n Enter choice:\n");
scanf("%d",&choice);
switch (choice){
case 1:traverse();
      break;
case 2:insertatfront();
      break;
case 3:insertatend();
      break;
case 4:insertatposition();
      break;
case 5:deleteatfirst();
      break;
case 6:deleteatend();
      break;      
case 7:deleteatposition();
      break;      
case 8:exit(1);
      break;
      default:
      printf("Incorrect choice\n");
      }
      }
      return 0;
      }
      
