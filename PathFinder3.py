import math
import heapq

def adjacent(point, N):
    x = point[0]
    y = point[1]
    if x == 0:
        if y == 0:
            return [(0, 1), (1, 0)]
        elif y == N-1:
            return [(0, N-2), (1, N-1)]
        else:
            return [(0, y-1), (0, y+1), (1, y)]
    elif x == N-1:
        if y == 0:
            return [(N-2, 0), (N-1, 1)]
        elif y == N-1:
            return [(N-2, N-1), (N-1, N-2)]
        else:
            return [(N-2, y), (N-1, y-1), (N-1, y+1)]
    else:
        if y == 0:
            return [(x - 1, 0), (x, 1), (x+1, 0)]
        elif y == N-1:
            return [(x-1, N-1), (x, N-2), (x+1, N-1)]
        else:
            return [(x-1, y), (x, y-1), (x, y+1), (x+1, y)]


def compute_altitude(point1, point2, maze, N):
    x_1 = point1[0]
    x_2 = point2[0]
    y_1 = point1[1]
    y_2 = point2[1]
    return abs(int(maze[y_1*N+x_1+y_1])-int(maze[y_2*N+x_2+y_2]))

##USE HEAPS FOR QUEUED



def path_finder(maze):
    maze_len = len(maze)
    N = math.floor(maze_len ** 0.5)
    weights = [N * [float("inf")] for k in range(N)]
    weights[0][0] = 0
    priority = []
    for i in range(N):
        for j in range(N):
            if i == j and i == 0:
                priority.append((0, (i, j)))
            else:
                priority.append((float("inf"), (i, j)))
    final = (N-1, N-1)
    visiting = (0, 0)
    visited = set()
    while visiting != final:
        visited.add(visiting)
        x_visiting = visiting[0]
        y_visiting = visiting[-1]
        for node in adjacent(visiting, N):
            x_adjacent = node[0]
            y_adjacent = node[-1]
            if node not in visited:
                update_weight = weights[y_visiting][x_visiting] + compute_altitude(visiting, node, maze, N)
                if weights[y_adjacent][x_adjacent] > update_weight:
                    weights[y_adjacent][x_adjacent] = update_weight
                    heapq.heappush(priority, (update_weight, node))
        visiting = heapq.heappop(priority)[1]
        while visiting[1] in visited:
            visiting = heapq.heappop(priority)[1]
    return weights[N-1][N-1]



a = "\n".join([
  "000",
  "000",
  "000"
])

b = "\n".join([
  "010",
  "010",
  "010"
])

c = "\n".join([
  "010",
  "101",
  "010"
])

d = "\n".join([
  "0707",
  "7070",
  "0707",
  "7070"
])

e = "\n".join([
  "700000",
  "077770",
  "077770",
  "077770",
  "077770",
  "000007"
])

f = "\n".join([
  "777000",
  "007000",
  "007000",
  "007000",
  "007000",
  "007777"
])

g = "\n".join([
  "000000",
  "000000",
  "000000",
  "000010",
  "000109",
  "001010"
])

print(path_finder(a))
print(path_finder(b))
print(path_finder(c))
print(path_finder(d))
print(path_finder(e))
print(path_finder(f))
print(path_finder(g))


