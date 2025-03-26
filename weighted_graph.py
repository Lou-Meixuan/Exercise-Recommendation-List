from typing import Optional, Any
from similarity_score_calculation import Graph, _Vertex


class Exercise:
    """An exercise and its categories

    Instance Attributes:
    - user_id: A unique identifier for the exercise
    - name: The name of the exercise
    - force: The force the exercise targets
    - level: The level of the exercise
    - mechanic: The mechanic of the exercise
    - equipment: The equipment needed for the exercise
    - primary_muscles: The primary muscles targeted by the exercise
    - secondary_muscles: The secondary muscle(s) targeted by the exercise
    - instructions: The instructions for the exercise
    - category: The category of the exercise
    - images: The images of the exercise


    Representation Invariants:
    - self.id > 0
    - self.name != ""
    """

    user_id: int
    name: str
    force: str
    level: str
    mechanic: Optional[str]
    equipment: Optional[str]
    primary_muscles: list[str]
    secondary_muscles: list[str]
    instructions: str
    category: str
    images: list[str]

    def __init__(self, user_id, name, force, level, mechanic, equipment, primary_muscles, secondary_muscles,
                 instructions, category, images) -> None:
        """Initialize an exercise with the given properties"""
        self.user_id = user_id
        self.name = name
        self.force = force
        self.level = level
        self.mechanic = mechanic
        self.equipment = equipment
        self.primary_muscles = primary_muscles
        self.secondary_muscles = secondary_muscles
        self.instructions = instructions
        self.category = category
        self.images = images


"""
class Vertex:
    A vertex or a node in the graph holding an item of the exercise class"
    
    instance Attributes:
    - item: The item of the exercise class
    - neighbours: The neighbours of the node"
    
    item: Exercise
    neighbours: List["Vertex"] # Fwd reference string to avoid circular import

    def __init__(self, item: Exercise) -> None:
        self.item = item
        self.neighbours = []
    
    def add_neighbour(self, neighbour: Vertex) -> None:
        self.neighbours.append(neighbour)
        neighbour.neighbours.append(self)
    
    def remove_neighbour(self, neighbour: Vertex) -> None:
        self.neighbours.remove(neighbour)
        neighbour.neighbours.remove(self)
"""


class WeightedGraph:
    """A weighted graph holding the vertices of the exercise class"
    
    Instance Attributes:
    -
    """
    _vertices: dict[Any, _Vertex]
    original_graph: Graph
    
    def __init__(self, original_graph) -> None:
        self._vertices = {}
        self.original_graph = original_graph

    def add_vertex(self, item: Any, kind:Any) -> None:
        """
        Add a vertex with the given item to this graph. The new vertex is not adjacent to any other vertices.

        Preconditions:
            - item not in self._vertices
        """
        if item not in self._vertices:
            self._vertices[item] = _Vertex(item, set(), kind)

    def add_edge(self, item1: Any, item2: Any) -> None:
        """
        Add an edge between the two vertices with the given items in this graph. Raise a ValueError if item1 or item2
        do not appear as vertices in this graph.

        Preconditions:
            - item1 != item2
        """
        if item1 in self._vertices and item2 in self._vertices:
            v1 = self._vertices[item1]
            v2 = self._vertices[item2]
            v1.neighbours.add(v2)
            v2.neighbours.add(v1)
        else:
            raise ValueError

    def get_name_vertices(self) -> None:
        for v in self.original_graph.vertices:
            if self.original_graph.vertices[v].kind == "name":
                self.add_vertex(v, "name")
    
    def popular_weighted_graph(self):

