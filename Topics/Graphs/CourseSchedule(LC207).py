# leetcode.com/problems/course-schedule/

from collections import defaultdict

def create_graph(prerequisites):
    d = defaultdict(list)
    for edge in prerequisites:
        u, v = edge[0], edge[1]
        d[v].append(u)
    return d

def dfs(graph, v, visited):
    if visited[v] == 1:
        return False
    if visited[v] == 2:
        return True
    
    visited[v] = 1
    for u in graph[v]:
        if not dfs(graph, u, visited):
            return False
    visited[v] = 2
    
    return True
    
def canFinish(numCourses, prerequisites):
    visited = [0] * numCourses
    graph = create_graph(prerequisites)
    
    for i in range(numCourses):
        if not visited[i]:
            if not dfs(graph, i, visited):
                return False
    
    return True