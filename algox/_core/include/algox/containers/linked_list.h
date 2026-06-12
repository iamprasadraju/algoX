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

/* operations/interface */
void ll_append(LinkedList *list, void *data); // post-append (add to tail)
void ll_prepend(LinkedList *list, void *data); // pre-append (add to head)

#endif