#include "lists.h"
#include <string.h>
#include <stdio.h>
#include <stdlib.h>

/**
  * is_palindrome - function in C that checks
  * if a singly linked list is a palindrome.
  * @head: pointer.
  * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
  */
int is_palindrome(listint_t **head)
{
	listint_t *x = *head;
	int nd = 0, i = 0, *arr = NULL;

	if (*head == NULL || head == NULL || (*head)->next == NULL)
		return (1);
	while (x)
	{
		nd++;
		x = x->next;
	}
	arr = malloc(sizeof(int) * nd);
	x = *head;
	while (x)
	{
		arr[i++] = x->n;
		x = x->next;
	}
	for (i = 0; i < nd / 2; i++)
	{
		if (arr[i] != arr[nd - 1 - i])
		{
			free(arr);
			return (0);
		}
	}
	free(arr);
	return (1);
}
