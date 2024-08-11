```markdown
1. Let’s break down each of the cases:

   a. Reading from an array always takes just one step.

   b. Searching for a nonexistent element within an array of size 100 will take 100 steps, as the computer needs to inspect each element of the array before determining the element cannot be found.

   c. The insertion will take 101 steps: 100 shifts of each element to the right, and one step to insert the new element at the front of the array.

   d. Insertion at the end of an array always takes one step.

   e. The deletion will take 100 steps: first, the computer deletes the first element and then shifts the remaining 99 elements to the left, one at a time.

   f. Deletion at the end of an array always takes one step.

2. Let’s break down each of the cases:

   a. Like the array, reading from the array-based set will take just one step.

   b. Like the array, searching the array-based set will take 100 steps, as we inspect each element before concluding that the element isn’t there.

   c. To insert into the set, we first need to conduct a full search to make sure the value doesn’t already exist within the set. This search will take 100 steps. Then, we need to shift all 100 elements to the right to make room for the new value. Finally, we drop the new value at the beginning of the set. This is a total of 201 steps.

   d. This insertion takes 101 steps. Again, we need to conduct a full search before inserting, which takes 100 steps. We then conclude with the final step of inserting the new value at the end of the set.

   e. The deletion will take 100 steps, just like a classic array.

   f. The deletion will take one step, just like a classic array.

3. If the array contains N elements, searching for all instances of the string “apple” in an array will take N steps. When searching for just one instance, we can cut our search short as soon as we find it. But if we need to find all instances, we have no choice but to inspect each element of the entire array.
```
