#ifndef ALGOX_CONTAINERS_BINARY_TREE_H
#define ALGOX_CONTAINERS_BINARY_TREE_H

typedef struct Node {
  int *data;
  struct Node *root_node;
  struct Node *left_child_node;
  struct Node *right_child_node;
  size_t level;
}

typedef struct BinaryTree {
  size_t height;
  size_t degree;
  struct *Node;
  
}BinaryTree;

#endif