#include "search_algos.h"

// Function prototype declaration
int advanced_binary_recursive(int *array, size_t left, size_t right, int value);

/**
 * advanced_binary - Searches for a value in a sorted array of integers using
 *                   advanced binary search.
 * @array: Pointer to the first element of the array to search in.
 * @size: Number of elements in array.
 * @value: Value to search for.
 *
 * Return: Index where value is located, or -1 if not found or array is NULL.
 */
int advanced_binary(int *array, size_t size, int value)
{
    if (array == NULL || size == 0)
        return -1;

    return advanced_binary_recursive(array, 0, size - 1, value);
}

/**
 * advanced_binary_recursive - Recursive helper function for advanced binary search.
 * @array: Pointer to the first element of the array to search in.
 * @left: The left index of the current subarray.
 * @right: The right index of the current subarray.
 * @value: Value to search for.
 *
 * Return: Index where value is located, or -1 if not found.
 */
int advanced_binary_recursive(int *array, size_t left, size_t right, int value)
{
    if (left > right)
        return -1;

    printf("Searching in array: ");
    print_array(array, left, right);

    size_t mid = left + (right - left) / 2;

    if (array[mid] < value)
        return advanced_binary_recursive(array, mid + 1, right, value);
    else if (array[mid] > value)
        return advanced_binary_recursive(array, left, mid - 1, value);
    else
    {
        // Check if there is a smaller index with the same value
        if (mid > 0 && array[mid - 1] == value)
            return advanced_binary_recursive(array, left, mid - 1, value);
        return mid;
    }
}

/**
 * print_array - Prints the elements of an array within a specified range.
 * @array: Pointer to the first element of the array to print.
 * @left: The left index of the range to print.
 * @right: The right index of the range to print.
 */
void print_array(int *array, size_t left, size_t right)
{
    size_t i;
    for (i = left; i <= right; i++)
    {
        printf("%d", array[i]);
        if (i < right)
            printf(", ");
    }
    printf("\n");
}
