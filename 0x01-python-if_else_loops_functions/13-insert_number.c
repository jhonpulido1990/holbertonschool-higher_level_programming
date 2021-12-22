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
	listint_t *current = *head;
	listint_t *insert;

	insert = malloc(sizeof(listint_t));
	if (insert == NULL)
		return (NULL);
	insert->n = number;
	insert->next = NULL;
    if (*head == NULL)
        *head = insert;
    else
    {
        if (current->n >= number)
        {
            *head = insert;
            insert->next = current;
        }
        else
        {
            while ((current->next != NULL) && (current->next->n <= number))
                current = current->next;

            insert->next = current->next;
            current->next = insert;
        }
    }
    return (insert);
}