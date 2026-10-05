from collections import deque
import time


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj = [[] for _ in range(vertices)]

    # Add edge (Undirected Graph)
    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    # DFS Utility
    def dfs_util(self, v, visited):
        visited[v] = True
        print(v, end=" ")

        for neighbor in self.adj[v]:
            if not visited[neighbor]:
                self.dfs_util(neighbor, visited)

    # DFS Traversal
    def dfs(self, start):
        visited = [False] * self.V
        self.dfs_util(start, visited)

    # BFS Traversal
    def bfs(self, start):
        visited = [False] * self.V
        queue = deque()

        visited[start] = True
        queue.append(start)

        while queue:
            node = queue.popleft()

            print(node, end=" ")

            for neighbor in self.adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)


# Main Program
V = int(input("Enter number of vertices: "))

g = Graph(V)

E = int(input("Enter number of edges: "))

print("Enter edges (u v):")

for i in range(E):
    u, v = map(int, input().split())
    g.add_edge(u, v)

start = int(input("Enter starting vertex: "))


# ---------------- DFS Time Analysis ----------------
start_dfs = time.perf_counter_ns()

print("\nDFS Traversal: ", end="")
g.dfs(start)

end_dfs = time.perf_counter_ns()

dfs_time = end_dfs - start_dfs


# ---------------- BFS Time Analysis ----------------
start_bfs = time.perf_counter_ns()

print("\n\nBFS Traversal: ", end="")
g.bfs(start)

end_bfs = time.perf_counter_ns()

bfs_time = end_bfs - start_bfs


# ---------------- Execution Time ----------------
print("\n\nExecution Time:")
print("DFS:", dfs_time, "ns")
print("BFS:", bfs_time, "ns")