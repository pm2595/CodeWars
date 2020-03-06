def to_graph(maze):
    vec = maze.split()
    n = len(vec)
    graph = {}
    for i in range(n):
        for j in range(n):
            s = str(i) + "," + str(j)
            graph[s] = []
            if vec[i][j] != 'W':
                if i > 0 and vec[i-1][j] == '.':
                    graph[s].append(str(i - 1) + "," + str(j))
                if i < n-1 and vec[i+1][j] == '.':
                    graph[s].append(str(i + 1) + "," + str(j))
                if j > 0 and vec[i][j-1] == '.':
                    graph[s].append(str(i) + "," + str(j - 1))
                if j < n-1 and vec[i][j+1] == '.':
                    graph[s].append(str(i) + "," + str(j + 1))
    return graph


def path_finder(maze):
    graph = to_graph(maze)
    start = list(graph.keys())[0]
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(-1)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(list(set(graph[vertex]) - set(visited)))
            if list(graph.keys())[-1] in visited:
                return True
    return False



a = "\n".join([
  ".W.",
  ".W.",
  "..."
])

b = "\n".join([
  ".W.",
  ".W.",
  "W.."
])

c = "\n".join([
  "......",
  "......",
  "......",
  "......",
  "......",
  "......"
])

d = "\n".join([
  "......",
  "......",
  "......",
  "......",
  ".....W",
  "....W."
])

print(path_finder(a) is True)
print(path_finder(b) is False)
print(path_finder(c) is True)
print(path_finder(d) is False)