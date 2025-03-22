from typing import List, Optional
class Exercise:
    """An exercise and its categories

    Instance Attributes:
    - id: A unique identifier for the exercise
    - name: The name of the exercise
    - force: The force the exercise targets
    - level: The level of the exercise
    - mechanic: The mechanic of the exercise
    - equipment: The equipment needed for the exercise
    - primaryMuscles: The primary muscles targeted by the exercise
    - secondaryMuscles: The secondary muscle(s) targeted by the exercise
    - instructions: The instructions for the exercise
    - category: The category of the exercise
    - images: The images of the exercise    
    

    Representation Invariants:
    - self.id > 0
    - self.name != ""
    """

    id: int
    name: str
    force: str
    level: str
    mechanic: Optional[str]
    equipment: Optional[str]
    primaryMuscles: List[str]
    secondaryMuscles: List[str]
    instructions: str
    category: str
    images: List[str]

    def __init__(self, id, name, force, level, mechanic, equipment, primaryMuscles, secondaryMuscles, instructions, category, images) -> None:
        self.id = id
        self.name = name
        self.force = force
        self.level = level
        self.mechanic = mechanic
        self.equipment = equipment
        self.primaryMuscles = primaryMuscles
        self.secondaryMuscles = secondaryMuscles
        self.instructions = instructions
        self.category = category
        self.images = images

class Vertex:
    """A vertex or a node in the graph holding an item of the exercise class"
    
    instance Attributes:
    - item: The item of the exercise class
    - neighbours: The neighbours of the node"
    """
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


class Graph:
    """A weighted graph holding the vertices of the exercise class"
    
    Instance Attributes:
    - _vertices: The vertices of the graph
    - edges: The edges of the graph
    """

    _vertices: List[Vertex]
    
    def __init__(self) -> None:
        self._vertices = []
    
    def add_vertex(self, exercise: Exercise) -> None: # not sure about here
        self._vertices.append(Vertex(exercise))