#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - function in C that inserts a number
 * into a sorted singly linked list.
 * @head: head of a list.
 * @number: input.
 * Return: the address of the new node,or NULL if it
 * failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *x;
	listint_t *hd;
	listint_t *hd_p;

	hd = *head;
	x = malloc(sizeof(listint_t));

	if (x == NULL)
		return (NULL);

	while (hd != NULL)
	{
		if (hd->n > number)
			break;
		hd_p = hd;
		hd = hd->next;
	}

	x->n = number;

	if (*head == NULL)
	{
		x->next = NULL;
		*head = x;
	}
	else
	{
		x->next = hd;
		if (hd == *head)
			*head = x;
		else
			hd_p->next = x;
	}

	return (x);
}
