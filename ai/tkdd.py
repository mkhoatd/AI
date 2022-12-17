# from collections import namedtuple

# Edge = namedtuple('Edge', ['start', 'end', 'cost'])
# Vertex = namedtuple('Vertex')

# class Graph:
#     def __init__(self, directed=False):
#         self.vertices = {}  # Danh sách các đỉnh
#         self.edges = {}  # Danh sách các cạnh
#         self.directed = directed  # Biến đánh dấu xem đồ thị có hướng hay không

#     def add_vertex(self, vertex):
#         """Thêm một đỉnh mới vào đồ thị"""
#         self.vertices.append(vertex)

#     def add_edge(self, start, end, cost=0):
#         """Thêm một cạnh mới vào đồ thị, có thể là cạnh hướng hoặc cạnh vô hướng"""
#         edge = Edge(start, end, cost)
#         self.edges.append(edge)
#         if not self.directed:
#             self.edges.append((end, start, cost))
from collections import deque


def uniform_cost_search(graph, start, goal):
    # Create a queue to store the nodes to be explored
    queue = deque([start])
    # Create a dictionary to store the cost of each node
    cost = {start: 0}
    # Create a dictionary to store the parent of each node
    parent = {start: None}

    # Loop until the queue is empty
    while queue:
        # Get the node at the front of the queue
        current = queue.popleft()

        # If the current node is the goal, return the path
        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            return path[::-1]

        # Loop through the neighbors of the current node
        for  neighbor, cost_of_edge in enumerate(graph[current]):
            # Calculate the cost of reaching the neighbor
            new_cost = cost[current] + cost_of_edge
            # If the neighbor has not been visited or the new cost is lower than the previous cost
            if neighbor not in cost.keys() or new_cost < cost[neighbor]:
                # Update the cost and parent of the neighbor
                cost[neighbor] = new_cost
                parent[neighbor] = current
                # Add the neighbor to the queue
                queue.append(neighbor)


labels = ["Hà Nội", "Nam Định", "Thanh Hóa", "Ninh Bình", "Phú Lý"]
labels_dict = {"Hà Nội": 0, "Nam Định": 1, "Thanh Hóa": 2, "Ninh Bình": 3, "Phú Lý": 4}
labels_dict_reverse = {0: "Hà Nội", 1: "Nam Định", 2: "Thanh Hóa", 3: "Ninh Bình", 4: "Phú Lý"}
data = [
    [float("inf"), 95, float("inf"), 51, 60],
    [95, float("inf"), 95, float("inf"), float("inf")],
    [float("inf"), 95, float("inf"), 64, float("inf")],
    [51, float("inf"), 64, float("inf"), 40],
    [60, float("inf"), float("inf"), 40, float("inf")],
]

path = uniform_cost_search(data, labels_dict["Hà Nội"], labels_dict["Thanh Hóa"])
print([labels_dict_reverse[i] for i in path])
