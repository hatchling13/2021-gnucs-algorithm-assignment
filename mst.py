from collections import deque
from sys import maxsize
from tkinter.constants import S

class Vertex:
    x = 0
    y = 0
    value = 0
    canvas_id = 0

    def __init__(self, x: int, y: int, value: int) -> None:
        self.x = x
        self.y = y
        self.value = value

class Edge:
    start: Vertex
    end: Vertex
    weight: int

    def __init__(self, start: Vertex, end: Vertex, weight: int) -> None:
        self.start = start
        self.end = end
        self.weight = weight

class Mst:
    _count = 0
    _edge = []
    _vertex = []

    def add_edge(self, start: Vertex, end: Vertex, weight: int) -> None:
        self._edge.append(Edge(start, end, weight))

    def add_vertex(self, x: int, y: int) -> None:
        self._count += 1

        vertex = Vertex(x, y, self._count)

        self._vertex.append(vertex)

    def get_vertex(self, index: int) -> Vertex:
        return self._vertex[index]

    def get_vertex_by_value(self, value: int) -> Vertex:
        for v in self._vertex:
            if v.value == value:
                return v
        
        return None

    def get_edge_by_vertex(self, v: Vertex) -> list:
        result = []

        for e in self._edge:
            if e.start is v or e.end is v:
                result.append(e)
        
        return result

    def prim(self, *, half=False):
        start = self.get_vertex(0)
        connected = [start]

        for edge in self.get_edge_by_vertex(start):
            pass

        while len(self._vertex) != len(connected):
            pass

    def kruskal(self, *, half=False):
        pass