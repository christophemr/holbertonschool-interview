#ifndef LISTS_H
#define LISTS_H


#include <stdio.h>
#include <stdlib.h>

/* STRUCTS AND DEFINITIONS */

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 */
typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;

// Function prototypes

listint_t *add_nodeint_end(listint_t **head, const int n);
size_t print_listint(const listint_t *h);
listint_t *insert_node(listint_t **head, int number);
void free_listint(listint_t *head);

#endif
