#include <stddef.h>
#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * insert_node - insert a node
 * @head: pointer to pointer of first node of listint_t list
 * @number: number stored at n
 *
 * Return: the address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;
	current = *head;
	while (current->next != NULL)
	{
		if (number < current->n || number < current->next->n)
		{
			break;
		}
		current = current->next;
	}
	new = malloc(sizeof(listint_t));
	if (new == NULL)
	{
		return (NULL);
	}
	new->n = number;
	new->next = current->next;
	current->next = new;
	return(new);
}
