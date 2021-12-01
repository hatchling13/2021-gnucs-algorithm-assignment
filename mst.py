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

    def prim(self, *, half=False):
        pass

    def kruskal(self, *, half=False):
        pass