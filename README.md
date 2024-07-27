# Bubble Sort Algorithm
**Introduction**

Bubble Sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted. The algorithm gets its name because smaller elements "bubble" to the top of the list.

**Time Complexity**
* Best Case: O(n) - The list is already sorted.
* Average Case: O(n^2) - The list is in random order.
* Worst Case: O(n^2) - The list is in reverse order.
Here, n is the number of elements in the list.

**Explanation**

**Function Definition:**

The bubbleSort function takes one parameter: arr (a list of integers to be sorted).

**Outer Loop:**

The outer loop runs from i = 0 to n-1 (where n is the length of the list). This loop ensures that the entire list is traversed multiple times.

**Inner Loop:**

The inner loop runs from j = 0 to n-i-2. This loop compares each pair of adjacent elements.
If the element at position j is greater than the element at position j+1, they are swapped. This step ensures that the largest unsorted element "bubbles" to its correct position.

**Return Sorted Array:**

After the loops complete, the sorted list arr is returned.

**User Input:**

The user is prompted to enter the elements of the array as a space-separated string. This input is converted to a list of integers using map and list.

**Print Before Sorting:**

The original array is printed before sorting.

**Function Call and Result:**
* The bubbleSort function is called with the user-provided array.
* The sorted array is printed to the console.
  
**Usage**
* Run the code.
* Enter the elements of the array when prompted. Separate each element with a space.
* The program will output the original array before sorting and the sorted array after applying bubble sort.
