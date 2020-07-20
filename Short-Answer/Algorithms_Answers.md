#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) The while loop should have a runtime complexity of O(n).

b) O ( n log n) because inside the while loop within the for loop, j is multiplied by 2. For loop is going to run n times, while while loop will run n\*2.

c) O(1) just because regardless of the input size, the function should take the same amount of time.

## Exercise II

I think the easiest way to approach this problem is using a binary search tree, because you can quickly get rid of n/2 of the values. if the egg were to break you can keep those values on the left side of the BST and the egg that doesn't break would stay on the right side. Since you know that any values that are less than f are floors where the eggs break, you can then assume that any floors that are greater than f are floors where the eggs aren't broken. This seems to be the simplest approach to the problem to help minimize the number of broken eggs. Average run time complexity of a binary search tree would be O(log n) with a worst case of O(n).
