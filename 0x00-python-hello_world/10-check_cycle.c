#include "lists.h"

/**
 * check_cycle - function in C that checks if a singly linked
 * list has a cycle in it.
 * @list: linked list to check
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *cy = list, *cy2 = list;

	while (list && cy && cy2 && cy->next && cy2->next)
	{
		cy = cy->next;
		cy2 = cy2->next->next;
		if (!cy2 || !cy)
			return (0);
		if (cy2->next == cy)
			return (1); 
	}
	return (0);
}
