# Library to deal with heaps
import heapq

data = [2, 19, 34, 56, 98, 1, 7]

# Apply heap rule to list
heapq.heapify(data)

# Remove first element from heap 
value = heapq.heappop(data)

# Add element to heap
heapq.heappush(data, 7)

print(value)
print(data)