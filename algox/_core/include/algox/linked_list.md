## Linked List
---

![linked list](https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Singly-linked-list.svg/1920px-Singly-linked-list.svg.png)

**FOR COMPILING (run at _core/)**

```bash
clang -Iinclude src/containers/linked_list.c -o linked_list
```

size of LinkedList; 

| Field        | Size    |
|--------------|---------:|
| `size_t len` | 8 bytes  |
| `Node *head` | 8 bytes  |
| `Node *tail` | 8 bytes  |
| **Total**    | **24 bytes** |

size of Node; 

| Field | Size |
|--------|------:|
| `void *data` | 8 bytes |
| `Node *next` | 8 bytes |
| **Total** | **16 bytes** |

## LinkedList Interface

* .append(LinkedList *list, void *data) - post-append (add element to tail) -> T complex: O(1) 
* .prepend(LinkedList *list, void *data) - pre-append (add element to head) -> T complex: O(1)
* .pop_front(LinkedList *list) - Remove and return the first element of the container. -> T complex: O(1)
* .pop_back(LinkedList *list) - Remove and return the last element of the container. -> T complex: O(1)
* .insert_at(LinkedList *list, int index) - Insert an element at position(index) -> T complex: O(n)
* .pop_at / remove_at (LinkedList *list, int index) - Remove an element at position -> T complex: O(n)
* .peek_first(LinkedList *list) - return first element in container -> T complex: O(1)
* .peek_back(LinkedList *list) - return last element in container -> T complex: O(1)

