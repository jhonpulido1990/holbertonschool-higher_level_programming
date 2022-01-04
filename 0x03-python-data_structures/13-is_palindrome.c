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
	char args[4024];

	if (head == NULL)
		return (1);
	h = *head;
	for (i = 0; h; i++,a++)
	{
		args[i] = h->n;
		h = h->next;
	}
	for (i = 0; i <= a/2; i++)
	{
		if (args[i] != args[a - (i + 1)])
		{
			return (0);
		}
	}
	return (1);
}
