# Thuật toán DFS
def DFS(G):
    visited = [0] * len(G)
    vertices = []
    DFS_visit(G, visited, 0, vertices)
    return unique_vertex(vertices)

def DFS_visit(G, visited, u, vertices):
    visited[u] = 1
    vertices.append(u)
    for v in G[u]:
        if visited[v] == 0:
            DFS_visit(G, visited, v, vertices)
            vertices.append(u)

# Loại bỏ các đỉnh bị lặp
def unique_vertex(vertices):
    TSP = []
    for v in vertices:
        if v not in TSP:
            TSP.append(v)
    return TSP + [vertices[0]]