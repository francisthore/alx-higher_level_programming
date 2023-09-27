#include "lists.h"
#include <stddef.h>

/**
 * check_cycle - checks if a list has a cycle
 * @list: head ptr to list
 * Return: 1 if cycle found or 0 otherwise
 */

int check_cycle(listint_t *list)
{
	listint_t *slw_ptr = list;
	listint_t *fast_ptr = list;

	while (slw_ptr != NULL && fast_ptr->next != NULL)
	{
		slw_ptr = slw_ptr->next;
		fast_ptr = fast_ptr->next->next;

		if (slw_ptr == fast_ptr)
			return (1);
	}
	return (0);
}
