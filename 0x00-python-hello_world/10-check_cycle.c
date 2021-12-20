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
	int i = 0, a = 0;
	listint_t *current = list;
	listint_t *temp = list;

	while (a < 4)
	{
		temp = temp->next;
		a++;
	}
	while (i < 4)
	{
		if (current->n == temp->n)
		{
			return (1);
		}
		temp = temp->next;
		i++;
	}
	return (0);
}
