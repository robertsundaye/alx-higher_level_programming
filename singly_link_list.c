#include <stdio.h>
#include <stdlib.h>

struct node {
	int data;
	struct node *link;
};

int count_of_node(struct node *hold_head);
void print_data(struct node *hold_head2);

int main()
{
	int counter;
	struct node *head = NULL;
	head = (struct node *)malloc(sizeof(struct node));
	head->data = 45;
	head->link = NULL;

	struct node *mover = NULL;
	mover = (struct node *)malloc(sizeof(struct node));
	mover->data = 90;
	mover->link = NULL;
	head->link = mover;

	mover = malloc(sizeof(struct node));
	mover->data = 100;
	mover->link = NULL;
	head->link->link = mover;

	mover = malloc(sizeof(struct node));
	mover->data = 150;
	mover->link = NULL;
	head->link->link->link = mover;

	printf("%d\n", head->data);
	printf("%d\n", head->link->data);
	printf("%d\n", head->link->link->data);
	printf("%d\n", head->link->link->link->data);

	counter = count_of_node(head);
	printf("The total number of nodes is : %d\n", counter);
	print_data(head);

	return (0);
}

int count_of_node(struct node *hold_head)
{
	int counter = 0;

	if (hold_head == NULL)
	{
		printf("link list is not set up\n");
	}
	struct node *runner = NULL;
	runner = hold_head;
	while(runner != NULL)
	{
		counter++;
		runner = runner->link;
	}

	return (counter);
}

void print_data(struct node *hold_head2)
{
	if (hold_head2 == NULL)
	{
		printf("link list is not set up\n");
	}
	struct node *runner2 = NULL;
	runner2 = hold_head2;
	while(runner2 != NULL)
	{
		printf("%d\n", runner2->data);
		runner2 = runner2->link;
	}
}
