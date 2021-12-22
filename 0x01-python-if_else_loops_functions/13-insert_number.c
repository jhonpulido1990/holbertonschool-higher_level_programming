#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
/**
 * insert_node - insert node list
 * @head: lista
 * @number: data
 * Return: new node list
 */
listint_t *insert_node(listint_t **head, int number)
{
	int i = 0;
	listint_t *current = *head;
	listint_t *insert;

	insert = malloc(sizeof(listint_t));
	if (insert == NULL)
		return (NULL);
	insert->n = number;
	for (; current->next != NULL; i++)
	{
		current = current->next;
		if (current->n >= insert->n)
			break;
	}
	current = *head;
	for (; i > 0; i--)
	{
		current = current->next;
	}
	insert->next = current->next;
	current->next = insert;
	return (insert);
}