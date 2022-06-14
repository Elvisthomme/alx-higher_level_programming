#include "lists.h"

/**
  * add_node - add a new node at the beginning of a listint_t
  * @head: a poiter to the head pointer
  * @n: the value to add to list_p
  * Return: the pointer to the new element or NULL if it failed
  */
list_p *add_pointer(list_p **head, listint_t *n)
{
	list_p *node;

	if (!head)
		return (NULL);
	node = malloc(sizeof(node));
	if (!node)
		return (NULL);
	node->n = n;
	node->next = *head;
	*head = node;
	return (node);
}

/**
 * free_list_p - frees a list_p list
 * @head: pointer to list to be freed
 * Return: void
 */

void free_list_p(list_p *head)

{
	list_p *current;
    
	while (head != NULL)
	{
		current = head;
		head = head->next;
		free(current);
	}
}

/**
  * check_cycle - check if a singly linked list has cycle in it
  * @h: the head of the listint_t
  * Return: 0 if there is no cycle, 1 if there is a cycle
  */
int check_cycle(listint_t *h)
{
	list_p *pointer_list, *head;

	head = NULL;
	pointer_list = NULL;
	if (!h)
		return (1);
	while (h)
	{
		add_pointer(&head, h);
		*pointer_list = *head;
		while (pointer_list)
		{

			if ((void*) (pointer_list->n) == (void*) (h->next))
			{
				free_list_p(head);
				free_list_p(pointer_list);
				return (0);
			}
			pointer_list = pointer_list->next;
		}
		pointer_list = head;
		h = h->next;
	}
	free_list_p(head);
	free_list_p(pointer_list);
	return (1);
}
