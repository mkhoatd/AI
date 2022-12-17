from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def addMultipleEdge(self, u, v):
        for node in v:
            self.graph[u].append(node)
            self.graph[node].append(u)

    def BFS(self, start, goal):
        visited = list()

        # Create a queue for BFS
        # Mark the source node as
        # visited and enqueue it

        frontier = [start]

        while frontier:

            # Dequeue a vertex from
            # queue and print it
            state = frontier.pop(0)
            visited.append(state)
            if state == goal:
                return visited

            # Get all adjacent vertices of the
            # dequeued vertex s. If a adjacent
            # has not been visited, then mark it
            # visited and enqueue it
            for i in self.graph[state]:
                if i not in visited and i not in frontier:
                    frontier.append(i)


if __name__ == "__main__":
    # Driver code

    # Create a graph given in
    # the above diagram
    g = Graph()
    g.addMultipleEdge("S", ["A", "B", "C"])
    g.addMultipleEdge('A', ['D'])
    g.addMultipleEdge('B', ['D', 'G', 'E'])
    g.addMultipleEdge('C', ['E'])
    g.addMultipleEdge('D', ['F'])
    g.addMultipleEdge('E', ['F', 'H'])
    g.addMultipleEdge('F', ['G'])
    g.addMultipleEdge('H', ['G'])

    print("Following is Breadth First Traversal"
          " (starting from vertex 2)")
    res = g.BFS('S', 'G')
    print(res)
