class Vertex:
    _x = 0
    _y = 0
    _value = 0

    def __init__(self, x: int, y: int, value: int) -> None:
        self._x = x
        self._y = y
        self._value = value

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