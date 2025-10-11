# Library for working with heaps in Python
import heapq

# Example data
data = [2, 19, 34, 56, 98, 1, 7]

# Transform the list into a heap in-place.
# In a binary heap, for a node at index i:
#   - The left child is at index 2*i + 1
#   - The right child is at index 2*i + 2
heapq.heapify(data)  
# Now 'data' is a valid min-heap (the smallest element is always at index 0).

# Remove and return the smallest element from the heap
value = heapq.heappop(data)

# Insert a new element into the heap while maintaining the heap property
heapq.heappush(data, 7)

# Heaps can also store tuples. In this case, the heap is ordered 
# by the first element of the tuple (using lexicographic order).
# This is useful when we want to associate keys with values.
data = [(24, "Fernando"), (30, "Maumau"), (23, "Lari"), (27, "Igor")]
heapq.heapify(data)  
# Result: [(23, 'Lari'), (24, 'Fernando'), (27, 'Igor'), (30, 'Maumau')]

# Extract elements in ascending order until the heap is empty
while data:
    d = heapq.heappop(data)