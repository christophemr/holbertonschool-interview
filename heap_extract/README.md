# heap_extract
This interview algorithm problem utilizes a Max Binary Heap. A Max Binary Heap is a complete binary tree where the root node is the maximum of all children nodes for the entire tree and recursively through any sub-trees.

[Heap Extract](/heap_extract/0-heap_extract.c)
* Write a function in C `int heap_extract(heap_t **root)` that extracts the root node of a Max Binary Heap, returning the value extracted and rebuilding the max heap.
  * `root` is a double pointer to the root node of the heap
  * returns the value store in the extracted node
  * root node must be freed and replaced with the last level-order node of the heap
  * the heap must be rebuilt to preserve Max Binary Heap if necessary
