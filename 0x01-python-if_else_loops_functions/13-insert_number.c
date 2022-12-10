#include <stddef.h>
#include "lists.h"
#include <stdio.h>
#include <stdlib.h>





listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;
	current = *head;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	if(*head == NULL)
	{
		*head = new;
		new->n = number;
		new->next = NULL;
	}
	while (current->next != NULL)
	{
		if (number < current->n || number < current->next->n)
		{
			break;
		}
		current = current->next;
	}
	if (current == *head && number < current->n)
	{
		*head = new;
		new->n = number;
		new->next = current;
	}
	else
	{
		new->n = number;
		new->next = current->next;
		current->next = new;
	}
	return(new);
}
