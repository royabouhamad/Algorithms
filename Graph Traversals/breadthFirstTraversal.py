graph = {
                "A": {"colour": "White", "neighbours": ["B", "D", "E"]},
                "B": {"colour": "White", "neighbours": ["A", "C", "D"]},
                "C": {"colour": "White", "neighbours": ["B", "G"]},
                "D": {"colour": "White", "neighbours": ["A", "B", "E", "F"]},
                "E": {"colour": "White", "neighbours": ["A", "D"]},
                "F": {"colour": "White", "neighbours": ["D"]},
                "G": {"colour": "White", "neighbours": ["C"]}
                }

def bfs(graph, vertex):
    queue = []
    visited = []
    queue.append(vertex)
    while len(queue) != 0:
        currentNode = queue.pop(0)
        graph[vertex]["colour"] = "Black"
        visited.append(currentNode)
        for neighbour in graph[currentNode]["neighbours"]:
            if graph[neighbour]["colour"] == "White":
                queue.append(neighbour)
                graph[neighbour]["colour"] = "Grey"
    return visited

visited = bfs(graph, "A")
print(visited)
