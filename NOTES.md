.c vs .h
--------

* .h -> declarations (what exists)
* .c -> implementations (how it works)


#### C backend - Python Wrapper

 * CPython C Extension (uses numpy) [fastest / efficient]

    Python User -> [global imports]
        ↓
    Python API (.py) -> [algox/.py]
        ↓
    Binding (.c)   ← only place with PyObject * -> [algox/_core/bindings]
        ↓
    Core (.c/.h)   ← no PyObject * -> [algox/_core/src & algox/_core/include]
 
    (Algox follows same architecture)

 ``` 90% - C; 10% - CPython ```

#### Things to learn in C

* malloc - 
* free - 
* typedef - Creates an alias (nickname) for a type.

without typedef 
---------------

```c
struct Vector {
    int size;
};

struct Vector v;
```
with typedef
------------

```c
typedef struct Vector {
    int size;
} Vector;

Vector V;
```

* struct - A struct groups multiple values into a single type.

Usage:
=====

```c
struct Vector {
    int size;
    int capacity;
};

Vector V;
V.size = 10;
V.capacity = 20;
```

* void * - 

