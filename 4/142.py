class Edge:
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w
    
    def __gt__(self, other):
        return self.w > other.w
    
    def __repr__(self) -> str:
        return f"{self.u}-{self.w}->{self.v}"


def find(parents, node):
    """нахождение родителя для узла"""
    if parents[node] == node:
        return node
    
    parents[node] = find(parents, parents[node])
    return parents[node]



def kruskal(edges, nodes):
    edges = sorted(edges)
    parent = {s: s for s in nodes}
    result = []
    i, e = 0, 0
    while e < len(nodes) - 1:
        u, v = edges[i].u, edges[i].v

        i = i + 1
        x, y = find(parent, u), find(parent, v)

        if x != y:
            e = e + 1
            result.append(edges[i - 1])
            parent[x] = y
    return result



nodes, edges = map(int, input().split())
edge_list = []
nodes_set = set()
for i in range(edges):
    u, v, w = input().split()
    nodes_set.add(u)
    nodes_set.add(v)
    edge_list.append(Edge(u, v, int(w)))


result = kruskal(edge_list, nodes_set)
print(sum(n.w for n in result))
