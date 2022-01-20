from enum import Enum
from typing import Any, Optional, Dict, List, Callable
from Stos_FIFO import Queue


class Iterator:
    def __init__(self):
        self.num = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.num += 1
        return self.num


class EdgeType(Enum):
    directed = 1
    undirected = 2


class Vertex:
    data: Any
    index: int

    def __init__(self, value: Any, index: int):
        self.data = value
        self.index = index


class Edge:
    source: Vertex
    destination: Vertex
    weight: Optional[float]

    def __init__(self, source: Vertex, destination: Vertex, weight: Optional[float] = None):
        self.source = source
        self.destination = destination
        self.weight = weight


class Graph:
    adjacencies: Dict[Vertex, List[Edge]]

    def __init__(self, value: Any):
        self.iterator = Iterator()
        self.adjacencies = dict([(Vertex(value, next(self.iterator)), list())])

    def __str__(self):
        napis = ""
        for x in self.adjacencies.keys():
            napis = napis + str(x.data) + ": " + str(x.index) + " ---> [" + str(self.ok(self.adjacencies[x])) + "]" + "\n"
        return napis

    def ok(self, lista: List[Edge]) -> str:
        napis = ""
        for x in lista:
            napis = napis + str(x.destination.data) + ": " + str(x.destination.index) + ", "
        return napis

    def create_vertex(self, data: Any):
        self.adjacencies.update([(Vertex(data, next(self.iterator)), list())])

    def get(self, data: Any):
        x = None
        for x in self.adjacencies.keys():
            if x.data == data:
                return x
        return x

    def add_directed_edge(self, source: Vertex, destination: Vertex, weight: Optional[float] = None):
        self.adjacencies[source].append(Edge(source, destination, weight))

    def add_undirected_edge(self, source: Vertex, destination: Vertex, weight: Optional[float] = None):
        self.adjacencies[source].append(Edge(source, destination, weight))
        self.adjacencies[destination].append(Edge(destination, source, weight))

    def add(self, edge: EdgeType, source: Vertex, destination: Vertex, weight: Optional[float] = None):
        if edge == 1 or EdgeType.directed:
            self.add_directed_edge(source, destination, weight)
        elif edge == 2 or EdgeType.undirected:
            self.add_undirected_edge(source, destination, weight)
        else:
            return None

    def traverse_breadth_first(self, visit: Callable[[Any], None]):
        kolejka = Queue()
        first = list(self.adjacencies)[0]
        kolejka.enqueue(first)
        odw = []
        while len(kolejka) != 0:
            v = kolejka.dequeue()
            visit(v.data)
            for x in self.adjacencies[v]:
                od = 0
                for y in odw:
                    if x.destination == y:
                        od += 1
                if od != 0:
                    continue
                else:
                    kolejka.enqueue(x.destination)
                    odw.append(x.destination)

    def traverse_depth_first(self, vertex: Vertex, visit: Callable[[Any], None], visited: List[Vertex] = []):
        visit(vertex.data)
        visited.append(vertex)
        for x in self.adjacencies[vertex]:
            ok = 0
            for y in visited:
                if x.destination == y:
                    ok += 1
            if ok != 0:
                continue
            self.traverse_depth_first(x.destination, visit, visited)

    def count(self, poczatek: Any, koniec: Any) -> int:
        many = 0
        kolejka = Queue()
        kolejka.enqueue(self.get(poczatek))
        odw = []
        while len(kolejka) != 0:
            odw2 = []
            v = kolejka.dequeue()
            odw.append(v)
            odw2.append(v)
            for x in self.adjacencies[v]:
                if x.destination.data == koniec:
                    many += 1
                else:
                    ok = 0
                    for y in odw:
                        if x.destination == y:
                            ok += 1
                    if ok == 0:
                        kolejka.enqueue(x.destination)
        return many


def paths_count(g: Graph, a: Any, b: Any) -> int:
    return g.count(a, b)

graf = Graph(0)
graf.create_vertex(1)
graf.create_vertex(2)
graf.create_vertex(3)
graf.create_vertex(4)
graf.create_vertex(5)
graf.add_directed_edge(graf.get(0), graf.get(1))
graf.add_directed_edge(graf.get(0), graf.get(5))
graf.add_directed_edge(graf.get(5), graf.get(1))
graf.add_directed_edge(graf.get(5), graf.get(2))
graf.add_directed_edge(graf.get(2), graf.get(3))
graf.add_directed_edge(graf.get(2), graf.get(1))
graf.add_directed_edge(graf.get(3), graf.get(4))
graf.add_directed_edge(graf.get(4), graf.get(1))
graf.add_directed_edge(graf.get(4), graf.get(5))
graf2 = Graph(0)
graf2.create_vertex(1)
graf2.create_vertex(2)
graf2.create_vertex(3)
graf2.create_vertex(4)
graf2.create_vertex(5)
graf2.add_directed_edge(graf2.get(0), graf2.get(1))
graf2.add_directed_edge(graf2.get(0), graf2.get(5))
graf2.add_directed_edge(graf2.get(0), graf2.get(4))
graf2.add_directed_edge(graf2.get(1), graf2.get(2))
graf2.add_directed_edge(graf2.get(2), graf2.get(3))
graf2.add_directed_edge(graf2.get(2), graf2.get(1))
graf2.add_directed_edge(graf2.get(2), graf2.get(4))
graf2.add_directed_edge(graf2.get(3), graf2.get(1))
graf2.add_directed_edge(graf2.get(4), graf2.get(5))
graf2.add_directed_edge(graf2.get(4), graf2.get(3))
graf2.add_directed_edge(graf2.get(4), graf2.get(2))
graf2.add_directed_edge(graf2.get(5), graf2.get(0))
graf2.add_directed_edge(graf2.get(5), graf2.get(4))
graf3 = Graph(0)
graf3.create_vertex(1)
graf3.create_vertex(2)
graf3.create_vertex(3)
graf3.create_vertex(4)
graf3.create_vertex(5)
graf3.add_directed_edge(graf3.get(0), graf3.get(1))
graf3.add_directed_edge(graf3.get(0), graf3.get(5))
graf3.add_directed_edge(graf3.get(5), graf3.get(1))
graf3.add_directed_edge(graf3.get(2), graf3.get(5))
graf3.add_directed_edge(graf3.get(2), graf3.get(3))
graf3.add_directed_edge(graf3.get(2), graf3.get(1))
graf3.add_directed_edge(graf3.get(4), graf3.get(0))
graf3.add_directed_edge(graf3.get(4), graf3.get(1))
graf3.add_directed_edge(graf3.get(4), graf3.get(5))
# graf.traverse_breadth_first(print)
# graf.traverse_depth_first(graf.get(0), print)
# print(graf.adjacencies)
# print(graf)
print(paths_count(graf, 2, 5))
print(paths_count(graf2, 0, 5))
print(paths_count(graf3, 0, 5))
