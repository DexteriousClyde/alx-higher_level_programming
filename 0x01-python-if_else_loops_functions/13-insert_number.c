#include "lists.h"

/**
 * insert_node - main
 * head: pointer
 * number: int
 * Return: listint_t
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *a, *b;
	
	a = malloc(sizeof(listint_t));
	if (a != NULL)
	{
		a->n = number;
		if (*head == NULL || (*head)->n >= a->n)
		{
			a->next = *head;
			*head = a;
			return (a);
		}
		else
		{
			b = *head;
			while (b->next != NULL && b->next->n < a->n)
			{
				b = b->next;
			}
			a->next = b->next;
			b->next = a;
			return (a);
		}
	}
	return (NULL);
}
