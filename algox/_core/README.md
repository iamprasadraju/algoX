#### Linked List

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
