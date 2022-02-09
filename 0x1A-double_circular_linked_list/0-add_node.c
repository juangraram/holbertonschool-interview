#include "list.h"
/**
 * add_node_begin - add node at start
 * @h: head
 * @str: string
 * Return: node - null
 */
List *add_node_begin(List **h, char *str)
{
	List *last, *n = NULL;

	n = malloc(sizeof(List));

	if (n == NULL)
		return (NULL);
	n->str = strdup(str);
	if (!n->str)
	{
		free(n);
		return (NULL);
	}
	if (*h == NULL)
	{
		n->next = n->prev = n;
		*h = n;
		return (n);
	}
	last = (*h)->prev;
	n->next = (*h);
	n->prev = last;
	(*h)->prev = last->next = n;
	*h = n;

	return (n);
}
/**
 * add_node_end - add node at end
 * @h: head
 * @str: string
 * Return: node null
 */
List *add_node_end(List **h, char *str)
{
	List *last, *n = NULL;

	n = malloc(sizeof(List));

	if (n == NULL || str == NULL)
		return (NULL);

	n->str = strdup(str);
	if (!n->str)
	{
		free(n);
		return (NULL);
	}
	if (*h == NULL)
	{
		n->next = n->prev = n;
		*h = n;
		return (n);
	}
	last = (*h)->prev;
	last->next = n;
	n->next = *h;
	n->prev = last;
	(*h)->prev = n;

	return (n);
}
