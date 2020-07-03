# -*- coding:utf-8 -*-
"""
@author: lijingxin
@contact: lijingxin666@gmail.com
@site: https://github.com/lijingxin666
@time: Created on 12:18 PM 5/15/20

Question: 

"""

import sys


class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}  # Dict
        # Set distance to infinity for all nodes
        self.distance = sys.maxsize
        # Mark all nodes unvisited
        self.visited = False
        # Predecessor
        self.previous = None

    def addNeighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    # returns a list
    def getConnections(self):  # neighbor keys
        return self.adjacent.keys()

    def getVertexID(self):
        return self.id

    def getWeight(self, neighbor):
        return self.adjacent[neighbor]

    def setDistance(self, dist):
        self.distance = dist

    def getDistance(self):
        return self.distance

    def setPrevious(self, prev):
        self.previous = prev

    def setVisited(self):
        self.visited = True

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

    def __lt__(self, other):
        return self.distance < other.distance and self.id < other.id


class Graph:
    def __init__(self, directed=False):
        # key is string, vertex id
        # value is Vertex
        self.vertDictionary = {}
        self.numVertices = 0
        self.directed = directed

    def __iter__(self):
        return iter(self.vertDictionary.values())

    def isDirected(self):
        return self.directed

    def vectexCount(self):
        return self.numVertices

    def addVertex(self, node):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(node)  # create一个对象,对象是一个顶点
        self.vertDictionary[node] = newVertex  # 把顶点放到Dict
        return newVertex

    def getVertex(self, n):
        if n in self.vertDictionary:
            return self.vertDictionary[n]  # 直接在Dict返回  没有的话返回None
        else:
            return None

    def addEdge(self, frm, to, cost=0):
        if frm not in self.vertDictionary:
            self.addVertex(frm)
        if to not in self.vertDictionary:
            self.addVertex(to)

        self.vertDictionary[frm].addNeighbor(self.vertDictionary[to], cost)  # from + neighbor:to   距离cost
        if not self.directed:
            # For directed graph do not add this
            self.vertDictionary[to].addNeighbor(self.vertDictionary[frm], cost)

    def getVertices(self):
        return self.vertDictionary.keys()

    def setPrevious(self, current):
        self.previous = current

    def getPrevious(self, current):
        return self.previous

    def getEdges(self):
        edges = []
        for key, currentVert in self.vertDictionary.items():  # 得到所有城市
            for nbr in currentVert.getConnections():  # 列出所有neighbor
                currentVertID = currentVert.getVertexID()
                nbrID = nbr.getVertexID()
                edges.append((currentVertID, nbrID, currentVert.getWeight(nbr)))  # tuple(from, to, weight)
        return edges

    def getNeighbors(self, v):
        vertex = self.vertDictionary[v]
        return vertex.getConnections()


def graphFromEdgelist(E, directed=False):
    """Make a graph instance based on a sequence of edge tuples.
    Edges can be either of from (origin,destination) or
    (origin,destination,element). Vertex set is presume to be those
    incident to at least one edge.
    vertex labels are assumed to be hashable.
    """
    g = Graph(directed)
    V = set()
    for e in E:  # E所有的顶点
        V.add(e[0])
        V.add(e[1])

    print("Vertex: ", V)

    verts = {}  # map from vertex label to Vertex instance    可以不用定义verts
    for v in V:
        verts[v] = g.addVertex(v)
    print(g.vectexCount())

    for e in E:
        src = e[0]  # from
        dest = e[1]  # to
        cost = e[2] if len(e) > 2 else None
        g.addEdge(src, dest, cost)
    return g

E2 = (
('A','B', 1), ('A','C', 1),
)
graph = graphFromEdgelist(E2, True)
for k in graph.getEdges():
    print(k)