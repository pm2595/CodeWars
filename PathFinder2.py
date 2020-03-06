def to_graph(maze):
    vec = maze.split()
    n = len(vec)
    maze = {}
    for i in range(n):
        for j in range(n):
            s = str(i) + "," + str(j)
            maze[s] = []
            if vec[i][j] != 'W':
                if i > 0 and vec[i-1][j] == '.':
                    maze[s].append(str(i - 1) + "," + str(j))
                if i < n-1 and vec[i+1][j] == '.':
                    maze[s].append(str(i + 1) + "," + str(j))
                if j > 0 and vec[i][j-1] == '.':
                    maze[s].append(str(i) + "," + str(j - 1))
                if j < n-1 and vec[i][j+1] == '.':
                    maze[s].append(str(i) + "," + str(j + 1))
    return maze


def path_finder(maze):
    graph = to_graph(maze)
    start = list(graph.keys())[0]
    final = list(graph.keys())[-1]
    queue, visited = graph[start], [start]
    path_len = {}
    i = 0
    while queue:
        i += 1
        to_visit = queue.copy()
        queue = []

        while to_visit:
            visiting = to_visit[0]
            to_visit.pop(0)
            visited.append(visiting)
            path_len[visiting] = i
            booked = queue+to_visit+visited
            queue.extend(list(set(graph[visiting]) - set(booked)))

    if final not in visited:
        return False
    else:
        return path_len[final]
