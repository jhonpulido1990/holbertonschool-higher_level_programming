#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * check_cycle - check likend list
 * @list: likend list
 * Return: 0 or 1
 */
int check_cycle(listint_t *list)
{
	listint_t *temp = list;
	listint_t *temp2 = list;

	while (temp->next != NULL)
	{

		temp = temp->next;
		temp2 = temp2->next;
		temp2 = temp2->next;
		if(temp == list && temp2 == list)
		{
			return (1);
		}
	}
	return (0);
}
