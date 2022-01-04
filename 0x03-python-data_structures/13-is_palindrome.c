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
	char *args;

	h = *head;
	for (i = 0; h; i++)
		h = h->next;
	a = i;
	args = malloc((i + 1) * sizeof(char *));
	if (args == NULL)
		return (0);
	h = *head;
	for (i = 0; h; i++)
	{
		args[i] = h->n;
		h = h->next;
	}
	for (i = 0; i <= a/2; i++)
	{
		if (args[i] != args[a - (i + 1)])
		{
			free(args);
			return (0);
		}
	}
	free(args);
	return (1);
}
