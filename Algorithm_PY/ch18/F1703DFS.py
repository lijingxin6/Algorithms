# -*- coding:utf-8 -*-
"""
@author: lijingxin
@contact: lijingxin666@gmail.com
@site: https://github.com/lijingxin666
@time: Created on 9:09 PM 5/16/20

Question: 

"""
from AdjListGraph import Graph
from AdjListGraph import Vertex
G = Graph(True)
G.addVertex('a')
G.addVertex('b')
G.addVertex('c')
G.addVertex('d')
G.addVertex('e')
G.addVertex('f')
G.addEdge('a', 'b', 1)
G.addEdge('a', 'c', 1)
G.addEdge('b', 'd', 1)
G.addEdge('b', 'e', 1)
G.addEdge('c', 'd', 1)
G.addEdge('c', 'e', 1)
G.addEdge('d', 'e', 1)
G.addEdge('e', 'a', 1)
G.addEdge('a', 'f', 1)
print (G.getEdges())
for k in G.getEdges():
    print(k)


def dfs(G, currentVert, visited):
    visited[currentVert] = True  # mark the visited node
    print("traversal: " + currentVert.getVertexID())
    for nbr in currentVert.getConnections():  # take a neighbouring node
        if nbr not in visited:  # condition to check whether the neighbour node is already visited
            dfs(G, nbr, visited)  # recursively traverse the neighbouring node
    return


def DFSTraversal(G):
    visited = {}  # Dictionary to mark the visited nodes
    for currentVert in G:  # G contains vertex objects
        if currentVert not in visited:  # Start traversing from the root node only if its not visited
            dfs(G, currentVert, visited)  # For a connected graph this is called only onc

