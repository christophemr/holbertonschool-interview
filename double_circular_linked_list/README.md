# double_circular_linked_list
This interview algorithm project works with a doubly linked list and circularly linked list. This project creates two functions: one to insert new nodes at the beginning of the circular list and one to insert at the end of the circular list.

[Add Nodes](/double_circular_linked_list/0-add_node.c)
* Write a function in C `List *add_node_end(List **list, char *str)` that adds a new node to the end of a double circular linked list:
  * `List` is the list to modify
  * `str` is the string to copy into the new node
  * returns the address of the new node, or NULL on failure
* Write a function in C `List *add_node_begin(List **list, char *str)` that adds a new node to the beginning of a double circular linked list:
  * `List` is the list to modify
  * `str` is the string to copy into the new node
  * returns the address of the new node, or NULL on failure
