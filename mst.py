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
    _start: Vertex
    _end: Vertex

    def __init__(self) -> None:
        pass

class Mst:
    _count = 0
    _edge = []
    _vertex = []

    def __init__(self) -> None:
        pass

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