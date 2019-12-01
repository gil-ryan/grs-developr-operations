# Fibonnaci Implementations

Write a dynamic programming version of computing Fibonacci for n.

Python: How would you remove indices 6 to 11 in a list foo?

```
del foo[6:12]
```

Isolate the right-most bit in x.

```
x & ~(x - 1)
```

What is Prim's algorithm?

```
def prim(self):
    """
    Returns a dictionary of parents of vertices in a minimum spanning tree
    :rtype: dict
    """
    s = set()
    q = queue.PriorityQueue()
    parents = {}
    start_weight = float("inf")
    weights = {}  # since we can't peek into queue

    for i in self.get_vertex():
        weight = start_weight
        if i == 0:
            q.put(([0, i]))
        weights[i] = weight
        parents[i] = None

    while not q.empty():
        v_tuple = q.get()
        vertex = v_tuple[1]

        s.add(vertex)

        for u in self.get_neighbor(vertex):
            if u.vertex not in s:
                if u.weight < weights[u.vertex]:
                    parents[u.vertex] = vertex
                    weights[u.vertex] = u.weight
                    q.put(([u.weight, u.vertex]))

    return parents
```

Python: Write a class function to tell if the graph is bipartite. Start with vertex 0. You can access the adjacency list for a vertex v with: self.adjacency_list[v]

```
def is_bipartite(self):
        """
        Returns true if graph is bipartite
        :rtype: bool
        """
        colorings = {}
        to_visit = queue.Queue()
        to_visit.put(0)
        colorings[0] = 0

        while not to_visit.empty():
            v = to_visit.get()

            for u in self.adjacency_list[v]:
                if u not in colorings:
                    colorings[u] = 1 - colorings[v]
                    to_visit.put(u)
                elif colorings[u] == colorings[v]:
                    return False

        return True
```
