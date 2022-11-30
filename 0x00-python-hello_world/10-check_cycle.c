#include "lists.h"
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

int check_cycle(listint_t *list)
{
	listint_t *cc;
	cc = list;
	while(cc)
	{
		cc = cc->next;
		if (cc == list)
		{
			return (1);
		}
	}
	return (0);
}
