#include "lists.h"
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
/**
 * @brief
 *
 */
int is_palindrome(listint_t **head)
{
	int i = 0, a = 0;
	listint_t *h = NULL;
	char args[1024];

	h = *head;
	for (i = 0; h; i++)
	{
		args[i] = h->n;
		h = h->next;
	}
	a = i;
	for (i = 0; i <= a/2; i++)
	{
		if (args[i] != args[a - (i + 1)])
		{
			return (0);
		}
	}
	return (1);
}
