"""
7 9
A B
A C
A F
C E 
C F
C D
D E
D G
G F
"""

from collections import defaultdict


def dfs(graph, start, visited, path):
    path.append(start)
    visited[start] = True
    for neighbour in graph[start]:
        if visited[neighbour] == False:
            dfs(graph, neighbour, visited, path)
    return path


graph = defaultdict(list)
v, e = map(int, input().split())

for i in range(e):
    u, v = map(str, input().split())
    graph[u].append(v)
    graph[v].append(u)

path = []
start = 'A'
visited = defaultdict(bool)
traversedpath = dfs(graph, start, visited, path)
print(traversedpath)
