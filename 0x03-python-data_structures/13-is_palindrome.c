#include "lists.h"
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
/**
 * is_palindrome - validator if likend list is palindrome
 * @head: likend list
 * Return: 0 or 1
 */
int is_palindrome(listint_t **head)
{
	int i = 0, a = 0, b = 0;
	listint_t *h = NULL;
	int args[4024];

	if (head == NULL)
		return (1);
	h = *head;
	for (i = 0; h; i++, a++)
	{
		args[i] = h->n;
		h = h->next;
	}
	a--;
	b = a / 2;
	for (i = 0; i <= b; i++, a--)
	{
		if (args[i] != args[a])
		{
			return (0);
		}
	}
	return (1);
}
