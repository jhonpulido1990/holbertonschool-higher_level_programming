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
	listint_t *ref = list;
	listint_t *ref2 = list;

	if (list == NULL)
		return (0);

	while (ref2->next != NULL)
	{
		ref = ref->next;
		ref2 = ref2->next;
		if (ref2->next == NULL)
			break;
		ref2 = ref2->next;
		if (ref2 == ref)
			return (1);
	}

	return (0);
}
