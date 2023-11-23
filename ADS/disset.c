#include<stdio.h>
#include<stdlib.h>
struct node {
struct node*rep;
struct node*next;
int data;
}*head[50],*tails[50];
static int countroot=0;
void makeset(int x) {
struct node*new=(struct node*)malloc(sizeof(structnode));
new_>rep=new;
new_>next=NULL;
new_>data=x;
heads[countroot]=new;
tails[countroot++]=new;
}
struct node*find(int a){
int i;
struct node*tmp=(struct node*)malloc(sizeof(struct node));
for(i=0;i<countroot;i++) {
		tmp=heads[i];
		while(tmp!=NULL) {
				if(tmp_>data==a)
						return tmp_>next;
				tmp=tmp_>next;
			}
}
return NULL;
}
void unionsets(int a,int b) {
int i,pos,flag=0,j;
struct node*tail2=(struct node*)malloc(sizeof(struct node));
struct node*rep1=find(a);
struct node*rep2=find(b);
if(rep1==NULL||rep2==NULL) {
			printf("\nNot Present");
			return;
}
if(rep1!=rep2) {
			for(j=0;j<countroot;j++) {
						if(heads[j]==rep2) {
										pos=j;
										flag=1;
										countroot_=1;
										tail2=tails[j];
										for(i=pos;i<countroot;i++){
													heads[i]=heads[i+1];
													tails[i]=tails[i+1];
										}
									}
									if(flag==1)
												break;
							}
							for(j=0;j<countroot;j++){
										if(heads[j]==rep1){
														tails[j]_>next=rep2;
														tails[j]=tail2;
														break;
										}
							}
							while(rep2!=NULL){
										rep_>rep=rep1;
										rep2=rep2_>next;
							}
			}
		}
		int search(int x){
		int i;
		struct node*tmp=(struct node*)malloc(sizeof(struct node));
		for(i=0;i<countroot;i++){
					tmp=heads[i];
					if(heads[i],i<countroot)
