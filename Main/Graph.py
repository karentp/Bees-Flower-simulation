def add_vertex(v):
  global graph
  global vertices_no
  if v in graph:
    print("Arco ", v, " ya existe.")
  else:
    vertices_no = vertices_no + 1
    graph[v] = []


def add_edge(v1, v2, e):
  global graph
  if v1 not in graph:
    print("Arco ", v1, " no existe.")
  elif v2 not in graph:
    print("Arco ", v2, " no existe.")
  else:
    temp = [v2, e]
    graph[v1].append(temp)

def print_graph():
  global graph
  for vertex in graph:
    for edges in graph[vertex]:
      print(vertex, " -> ", edges[0], "peso: ", edges[1])


graph = {}

vertices_no = 0
add_vertex(1)
add_vertex(2)
add_vertex(3)
add_vertex(4)

add_edge(1, 2, 1)
add_edge(1, 3, 1)
add_edge(2, 3, 3)
add_edge(3, 4, 4)
add_edge(4, 1, 5)
print_graph()

print ("Grafo: ", graph)


def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if not graph.has_key(start):
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

def BFS():
    pass

def DFS():
    pass
