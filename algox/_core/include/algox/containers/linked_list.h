#ifndef ALGOX_CONTAINERS_LINKED_LIST_H
#define ALGOX_CONTAINERS_LINKED_LIST_H

#include <stddef.h>

typedef struct Node {
  void *data;
  struct Node *next;
} Node;

typedef struct LinkedList {
  size_t len;
  Node *head;
  Node *tail;
} LinkedList;

/* Constructor / Destructor */
LinkedList *ll_new(void);
void ll_free(LinkedList *list);

// -----------------------
// operations/interface 
// -----------------------

// post-append (add element to tail)
void ll_append(LinkedList *list, void *data);
// pre-append (add element to head)
void ll_prepend(LinkedList *list, void *data);

// Remove and return the last element of the container.
// Returns:  The removed element.
void ll_pop_front(LinkedList *list); // Removes the first element and returns it

// Remove and return the last element of the container.
// The removed element.
void ll_pop_back(LinkedList *list);

void ll_peek_front(); // Return the first element without removing it.
void ll_peek_back();  // Return the last element without removing it.

void 

#endif