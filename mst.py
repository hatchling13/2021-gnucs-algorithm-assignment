import heapq

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

    def __lt__(self, other):
        return self.weight < other.weight

    def get_connected_vertex(self, v: Vertex) -> Vertex:
        if self.start is v:
            return self.end
        elif self.end is v:
            return self.start
        else:
            return None

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

    def prim(self, *, half=False) -> list:
        start = self.get_vertex(0)
        connected = [start]
        result_edge = []

        epoch = len(self._vertex)
        if half == True:
            epoch = epoch // 2 - 1
        
        candidate = self.get_edge_by_vertex(start)
        heapq.heapify(candidate)

        while candidate:
            if len(connected) > epoch:
                break

            edge: Edge = heapq.heappop(candidate)

            if edge.start not in connected:
                connected.append(edge.start)
                result_edge.append(edge)

            if edge.end not in connected:
                connected.append(edge.end)
                result_edge.append(edge)

            for e in self.get_edge_by_vertex(edge.end):
                if e.start not in connected:
                    heapq.heappush(candidate, e)
                
                if e.end not in connected:
                    heapq.heappush(candidate, e)

        return result_edge

    def kruskal(self, *, half=False) -> list:
        def find(parent: dict, x: Vertex) -> Vertex:
            if parent[x] == x:
                return x
            parent[x] = find(parent, parent[x])
            return parent[x]
        
        def union(parent: list, a: int, b: int):
            root_a = find(parent, a)
            root_b = find(parent, b)

            if root_a.value < root_b.value:
                parent[b] = a
            else:
                parent[a] = b

        edge_list = [e for e in self._edge]
        heapq.heapify(edge_list)

        parent = {v: v for v in self._vertex}
        result_edge = []

        epoch = len(self._vertex) - 1
        if half == True:
            epoch = epoch // 2 - 1

        while len(result_edge) < epoch:
            edge: Edge = heapq.heappop(edge_list)

            if find(parent, edge.start) != find(parent, edge.end):
                union(parent, edge.start, edge.end)
                result_edge.append(edge)

        return result_edge