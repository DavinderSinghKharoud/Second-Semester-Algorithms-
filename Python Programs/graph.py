class Node:
   def __init__(node, value,graph_dict=None):
      node.value = value
      node.neighbors = []

   def __repr__(self):
       return str(self.value)



graph_adjacency_list={}

def Add_vertices(node):
    graph_adjacency_list[node]=[]


def connect(node, neighbor):
    graph_adjacency_list[node].append(neighbor)
    graph_adjacency_list[neighbor].append(node)
    node.neighbors.append(neighbor)
    neighbor.neighbors.append(node)


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

Add_vertices(a)
Add_vertices(b)
Add_vertices(c)
Add_vertices(d)

connect(a, b)
connect(b, c)
connect(c, a)
connect(d, a)

print(graph_adjacency_list)


