'''
Graph is a data structure that consists of following two components:
    1. A finite set of vertices also called as nodes.
    2. A finite set of ordered pair of the form (u, v) called as edge. The pair is ordered because (u, v) is not same as (v, u) in case of directed graph(di-graph). The pair of form (u, v) indicates that there is an edge from vertex u to vertex v. The edges may contain weight/value/cost.

Graphs are used to represent many real life applications: Graphs are used to represent networks. The networks may include paths in a city or telephone network or circuit network. Graphs are also used in social networks like linkedIn, facebook. For example, in facebook, each person is represented with a vertex(or node). Each node is a structure and contains information like person id, name, gender and locale.

Following two are the most commonly used representations of graph.
1. Adjacency Matrix
2. Adjacency List

Adjacency Matrix is a 2D array of size V x V where V is the number of vertices in a graph. Let the 2D array be adj[][], a slot adj[i][j] = 1 indicates that there is an edge from vertex i to vertex j. Adjacency matrix for undirected graph is always symmetric. Adjacency Matrix is also used to represent weighted graphs. If adj[i][j] = w, then there is an edge from vertex i to vertex j with weight w.
Pros: Representation is easier to implement and follow. Removing an edge takes O(1) time. Queries like whether there is an edge from vertex 'u' to vertex 'v' are efficient and can be done O(1).
Cons: Consumes more space O(V^2). Even if the graph is sparse(contains less number of edges), it consumes the same space. Adding a vertex is O(V^2) time.

Adjacency List: An array of linked lists is used. Size of the array is equal to number of vertices. Let the array be array[]. An entry array[i] represents the linked list of vertices adjacent to the ith vertex. This representation can also be used to represent a weighted graph. The weights of edges can be stored in nodes of linked lists.

Cited and consulted from: http://www.geeksforgeeks.org/graph-and-its-representations/
'''

class Matrix:
    def __init__(self, size):
        self.size = size
        self.matrix = [[None for j in xrange(size)] for i in xrange(size)]
    def addedge(self, r, c, w):
        if r >= self.size or c >= self.size:
            return False, 'out of bound'
        else:
            self.matrix[r][c] = w
    def getweight(self, r, c):
        if r >= self.size or c >= self.size:
            return False, 'out of bound'
        else:
            return self.matrix[r][c]
    def djikstra(self, start, end):
        temp = [start]
        distance = {start: 0}
        predecessor = {}
        for vertex in temp:
            if vertex == end: break
            for edge in xrange(len(self.matrix[vertex])):
                if self.matrix[vertex][edge] != None:
                    weight = distance[vertex] + self.matrix[vertex][edge]
                    if edge not in distance or weight < distance[edge]:
                        distance[edge] = weight
                        temp.append(edge)
                        predecessor[edge] = vertex
        shortest = distance[end]
        path = [end]
        while path[0] != start:
            path = [predecessor[path[0]]] + path
        return shortest, path

#Test
'''
m = Matrix(10)
m.addedge(0,4,10)
m.addedge(4,3,20)
m.addedge(3,8,30)
m.addedge(8,5,40)
m.addedge(3,5,10)
print m.djikstra(0, 5)
'''

class AdjacencyList:
    def __init__(self):
        self.nodes = []
        self.edges = {}
        self.distance = {}
    def addnode(self, value):
        self.nodes.append(value)
        self.edges[value] = []
    def addedge(self, fromnode, tonode, distance):
        self.edges[fromnode].append(tonode)
        self.edges[tonode].append(fromnode)
        self.distance[(fromnode, tonode)] = distance
    def djikstra(self, start, end):
        temp = [start]
        visited = {start:0}
        predecessor = {}
        for vertex in temp:
            if vertex == end: break
            for edge in self.edges[vertex]:
                if (vertex, edge) in self.distance:
                    weight = visited[vertex] + self.distance[(vertex, edge)]
                    if edge not in visited or weight < visited[edge]:
                        visited[edge] = weight
                        temp.append(edge)
                        predecessor[edge] = vertex
        shortest = visited[end]
        path = [end]
        while path[0] != start:
            path = [predecessor[path[0]]] + path
        return shortest, path

#Test for AdjacencyList
'''
m = AdjacencyList()
m.addnode(0)
m.addnode(3)
m.addnode(4)
m.addnode(5)
m.addnode(8)
m.addedge(0,4,10)
m.addedge(4,3,20)
m.addedge(3,8,30)
m.addedge(8,5,40)
m.addedge(3,5,10)
print m.djikstra(0, 5)
'''
