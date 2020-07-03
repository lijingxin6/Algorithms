# -*- coding:utf-8 -*-
"""
@author: lijingxin
@contact: lijingxin666@gmail.com
@site: https://github.com/lijingxin666
@time: Created on 10:56 AM 5/16/20

Question: 

"""


class Vertex:
    def __init__(self, node):
        self.id = node  # id 相当于名称 城市名字
        # Mark all nodes unvisited
        self.visited = False

    def addNeighbor(self, neighbor, G):  # 要把Graph传进来, 建立联系的neighbor
        G.addEdge(self.id, neighbor)

    def getConnections(self, G):
        return G.adjMatrix[self.id]

    def getVertexID(self):
        return self.id

    def setVertexID(self, id):
        self.id = id

    def setVisited(self):
        self.visited = True

    def __str__(self):
        return str(self.id)


class Graph:
    def __init__(self, numVertices=10, directed=False):  # 创建一个矩阵   无向图
        self.adjMatrix = [[None] * numVertices for _ in range(numVertices)]
        self.numVertices = numVertices
        self.vertices = []  # list ==> dict {id:vertex}
        self.directed = directed
        for i in range(0, numVertices):
            newVertex = Vertex(i)  # 面向对象 =>  node id 就是 i
            self.vertices.append(newVertex)

    def addVertex(self, vtx, id):  # 这个 没有扩展操作
        if 0 <= vtx < self.numVertices:
            self.vertices[vtx].setVertexID(id)

    def getVertex(self, n):  # 给一个名字n, 返回 顶点->数字表示
        for vertxin in range(0, self.numVertices):
            if n == self.vertices[vertxin].getVertexID():
                return vertxin
        return None

    def addEdge(self, frm, to, cost=0):
        # print("from",frm, self.getVertex(frm))
        # print("to",to, self.getVertex(to))
        if self.getVertex(frm) is not None and self.getVertex(to) is not None:
            self.adjMatrix[self.getVertex(frm)][self.getVertex(to)] = cost
            if not self.directed: # 若direct=False,说明是无向图, 才执行下面无向图的操作
                # For directed graph do not add this
                self.adjMatrix[self.getVertex(to)][self.getVertex(frm)] = cost

    def getVertices(self):
        # *** create a copy, and return a copy ***
        vertices = []
        for vertxin in range(0, self.numVertices):
            vertices.append(self.vertices[vertxin].getVertexID())
        return vertices
        # return self.vertices  不能直接写, 其他人调用的时候就可以操作内部的数据了

    def printMatrix(self):
        for u in range(0, self.numVertices):
            row = []
            for v in range(0, self.numVertices):
                row.append(str(self.adjMatrix[u][v]) if self.adjMatrix[u][v] is not None else '/')
            print(row)

    def getEdges(self):
        edges = []
        for v in range(0, self.numVertices):  # 先知道多少个顶点,矩阵里不是0的 说明有连线
            for u in range(0, self.numVertices):
                if self.adjMatrix[u][v] is not None:
                    vid = self.vertices[v].getVertexID()
                    wid = self.vertices[u].getVertexID()
                    edges.append((vid, wid, self.adjMatrix[u][v]))
        return edges

    def getNeighbors(self, n):
        neighbors = []
        for vertxin in range(0, self.numVertices):
            if n == self.vertices[vertxin].getVertexID():  # 查找到这个顶点
                for neighbor in range(0, self.numVertices):
                    if (self.adjMatrix[vertxin][neighbor] is not None):
                        neighbors.append(self.vertices[neighbor].getVertexID())

    def isConnected(self, u, v):
        uidx = self.getVertex(u)
        vidx = self.getVertex(v)
        return self.adjMatrix[uidx][vidx] is not None

    def get2Hops(self, u):
        neighbors = self.getNeighbors(u)  # 先找到所有邻居
        print(neighbors)
        hopset = set()
        for v in neighbors:  # 再在邻居的所有的点 看看它们的邻居, 放进 set里  不会有重复
            hops = self.getNeighbors(v)
            hopset |= set(hops)
        return list(hopset)

graph = Graph(6,True)
graph.addVertex(0, 'a')
graph.addVertex(1, 'b')
graph.addVertex(2, 'c')
graph.addVertex(3, 'd')
graph.addVertex(4, 'e')
graph.addVertex(5, 'f')
graph.addVertex(6, 'g') # doing nothing here
graph.addVertex(7, 'h') # doing nothing here

print(graph.getVertices())
graph.addEdge('a', 'b', 1)
graph.addEdge('a', 'c', 2)
graph.addEdge('b', 'd', 3)
graph.addEdge('b', 'e', 4)
graph.addEdge('c', 'd', 5)
graph.addEdge('c', 'e', 6)
graph.addEdge('d', 'e', 7)
graph.addEdge('e', 'a', 8)
print(graph.printMatrix())
print(graph.getEdges())