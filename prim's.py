def prim(graph, vertices):
    selected = [False] * vertices
    selected[0] = True

    total_cost = 0

    print("\nEdges in Minimum Spanning Tree:")

    for _ in range(vertices - 1):
        minimum = float('inf')
        x = 0
        y = 0

        # Find the minimum weight edge
        for i in range(vertices):
            if selected[i]:
                for j in range(vertices):
                    if not selected[j] and graph[i][j] != 0:
                        if graph[i][j] < minimum:
                            minimum = graph[i][j]
                            x = i
                            y = j

        selected[y] = True
        total_cost += minimum

        print(f"{x} -- {y}  Weight = {minimum}")

    print("\nMinimum Spanning Tree Cost:", total_cost)


# Main Program
vertices = int(input("Enter number of vertices: "))

graph = []

print("\nEnter the adjacency matrix:")
print("Enter 0 if there is no edge.")

for i in range(vertices):
    row = list(map(int, input(f"Row {i}: ").split()))
    graph.append(row)

prim(graph, vertices)