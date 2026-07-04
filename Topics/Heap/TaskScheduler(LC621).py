# leetcode.com/problems/task-scheduler

import heapq
from collections import Counter, deque

def leastInterval(tasks, n):
    frq_tasks = Counter(tasks)
    max_heap = [-value for value in frq_tasks.values()]
    heapq.heapify(max_heap)
    queue = deque()
    
    time = 0
    while max_heap or queue:
        time += 1
        
        if max_heap:
            task = heapq.heappop(max_heap) + 1
            if task:
                queue.append((task, time + n))
        
        if queue and queue[0][1] >= time:
            v = queue.popleft()[0]
            heapq.heappush(max_heap, v)
    
    return time