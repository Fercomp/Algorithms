# leetcode.com/problems/course-schedule-ii
from collections import defaultdict

def findOrder(numCourses, prerequisites):
    graph = defaultdict(list)
    for pre in prerequisites:
        u, v = pre[0], pre[1]
        graph[v].append(u)
        
    visited = [0] * numCourses
    result = []
    
    def dfs(root, result):
        visited[root] = 1
        for v in graph[root]:
            if visited[v] == 0:
                if not dfs(v, result):
                    return False
            elif visited[v] == 1:
                return False
        visited[root] = 2
        result.append(root)
        return True
    
    for i in range(numCourses):
        if visited[i] == 0:
            if not dfs(i, result):
                return []
    
    result.reverse()
    return result