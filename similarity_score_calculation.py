from __future__ import annotations
from typing import Any, Optional
import math

class Exercise:
    """
    An exercise and its categories

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
                 instructions,
                 category, images) -> None:
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


class _Vertex:
    """A vertex or a node in the graph holding an item of the exercise class"

    instance Attributes:
    - item: The item of the exercise class
    - neighbours: All the vertices that adjacent to this vertex
    """
    item: Any
    neighbours: set[_Vertex]
    kind: str

    def __init__(self, item: Any, neighbours: set[_Vertex], kind) -> None:
        """Initialize a new vertex with the given item and neighbours."""
        self.item = item
        self.neighbours = neighbours
        self.kind = kind

    def check_connected(self, target_item: Any, visited: set[_Vertex]) -> bool:
        """Return whether this vertex is connected to a vertex corresponding to the target_item

        Preconditions:
            - self not in visited
        """
        if self.item == target_item:
            return True
        else:
            visited.add(self)
            for u in self.neighbours:
                if u not in visited:
                    if u.check_connected(target_item, visited):
                        return True
            return False

    def score_popular(self, other: Any) -> float:
        """
        Return the similarity score between this vertex and other.
        sim(v1, v2) = 0, if any of v1, v2 doesn’t have neighbour;
        sim(v1, v2) = number of vertices adjacent to both v1 and v2(intersection)/ number of vertices adjacent to v1
        or v2(union), otherwise

        Preconditions:
            - self is not other
            - self.kind == "name"
            - other.kind == "name"
        """
        adjacent_to_self = {v for v in self.neighbours}
        adjacent_to_other = {u for u in other.neighbours}
        adjacent_to_both = adjacent_to_self.intersection(adjacent_to_other)
        all_adjacent = adjacent_to_self.union(adjacent_to_other)
        if len(adjacent_to_both) == 0 or len(all_adjacent) == 0:
            return 0.0
        else:
            return len(adjacent_to_both) / len(all_adjacent)

    def score_unpopular(self, other: Any) -> float:
        """
        Return the similarity score. It is defined as the sum of the inverse logarithmic degree centrality of the
        neighbours shared by the two nodes. The definition is based on the concept that common elements with very large
        neighbourhoods are less significant when predicting a connection between two nodes compared with elements
        shared between a small number of nodes.
        sim(v1, v2) = 0, if d(v1) = 0 or d(v2) = 0
        sim(v1, v2) = the sum of the 1/log(len(w.neighbours)) for w in the intersection of the neighbours of v1 and v2.

        Preconditions:
            - self is not other
            - self.kind == "name"
            - other.kind == "name"
        """
        adjacent_to_self = {v for v in self.neighbours}
        adjacent_to_other = {u for u in other.neighbours}
        adjacent_to_both = adjacent_to_self.intersection(adjacent_to_other)
        number_list = [len(w.neighbours) for w in adjacent_to_both]
        if len(adjacent_to_both) == 0:
            return 0.0
        else:
            return sum([1 / math.log(each, 10) for each in number_list])

    def score_custom(self, other:Any, first_choice:str, second_choice:str, last_choice:str) -> float:
        """
        Return the similarity score where it's based on the user customization. User will enter three choices, where
        indicates the primary aspect, secondary aspect and the trivial aspect that the value for their exercise.
        The first choice will be valued as 6, the second choice will be valued as 4, and the last choice will be valued
        as 1, and other aspects will be valued as 2 each.

        Preconditions:
            - first_choice in ['force', 'level', 'mechanic', 'equipment', 'primary_muscles', 'secondary_muscles']
            - second_choice in ['force', 'level', 'mechanic', 'equipment', 'primary_muscles', 'secondary_muscles']
            - last_choice in ['force', 'level', 'mechanic', 'equipment', 'primary_muscles', 'secondary_muscles']
            - self.kind == "name"
            - other.kind == "name"
        """
        adjacent_to_self = {v for v in self.neighbours}
        adjacent_to_other = {u for u in other.neighbours}
        adjacent_to_both = adjacent_to_self.intersection(adjacent_to_other)
        score = 0.0
        for v in adjacent_to_both:
            if v.kind == first_choice:
                score += 6.0
            elif v.kind == second_choice:
                score += 4.0
            elif v.kind == last_choice:
                score += 1.0
            else:
                score += 2.0
        return score


class Graph:
    """
    A normal graph.

    Representation Invariants:
        - all(item == self._vertices[item].item for item in self._vertices)
    """
    # Private Instance Attributes:
    #     - _vertices:
    #         A collection of the vertices contained in this graph.
    #         Maps item to _Vertex object.
    vertices: dict[Any, _Vertex]

    def __init__(self) -> None:
        """Initialize an empty graph (no vertices or edges)."""
        self.vertices = {}

    def add_vertex(self, item: Any, kind:Any) -> None:
        """
        Add a vertex with the given item to this graph. The new vertex is not adjacent to any other vertices.

        Preconditions:
            - item not in self.vertices
        """
        if item not in self.vertices:
            self.vertices[item] = _Vertex(item, set(), kind)

    def add_edge(self, item1: Any, item2: Any) -> None:
        """
        Add an edge between the two vertices with the given items in this graph. Raise a ValueError if item1 or item2
        do not appear as vertices in this graph.

        Preconditions:
            - item1 != item2
        """
        if item1 in self.vertices and item2 in self.vertices:
            v1 = self.vertices[item1]
            v2 = self.vertices[item2]
            v1.neighbours.add(v2)
            v2.neighbours.add(v1)
        else:
            raise ValueError

    def adjacent(self, item1: Any, item2: Any) -> bool:
        """
        Return whether item1 and item2 are adjacent vertices in this graph. Return False if item1 or item2 do not
        appear as vertices in this graph.
        """
        if item1 in self.vertices and item2 in self.vertices:
            v1 = self.vertices[item1]
            return any(v2.item == item2 for v2 in v1.neighbours)
        else:
            return False

    def connected(self, item1: Any, item2: Any) -> bool:
        """
        Return whether item1 and item2 are connected vertices in this graph. Return False if item1 or item2 do not
        appear as vertices in this graph.
        """
        if item1 in self.vertices and item2 in self.vertices:
            v1 = self.vertices[item1]
            return v1.check_connected(item2, set())  # Pass in an empty "visited" set
        else:
            return False

    def get_score_popular(self, item1: Any, item2: Any, ) -> float:
        """Return the similarity score of score_popular between the two given items in this graph.
        Raise a ValueError if item1 or item2 do not appear as vertices in this graph.

        Preconditions:
            - item1.kind == "name" and item2.kind == name
        """
        if item1 in self.vertices and item2 in self.vertices:
                return self.vertices[item1].score_popular(self.vertices[item2])
        else:
            raise ValueError

    def get_score_unpopular(self, item1: Any, item2: Any, ) -> float:
        """Return the similarity score of score_unpopular between the two given items in this graph.
        Raise a ValueError if item1 or item2 do not appear as vertices in this graph.

        Preconditions:
            - item1.kind == "name" and item2.kind == name
        """
        if item1 in self.vertices and item2 in self.vertices:
                return self.vertices[item1].score_unpopular(self.vertices[item2])
        else:
            raise ValueError

    def get_score_custom(self, item1: Any, item2: Any, first_choice:str, second_choice:str, last_choice:str) -> float:
        """Return the similarity score between the two given items in this graph.
        Raise a ValueError if item1 or item2 do not appear as vertices in this graph.

        Preconditions:
            - item1.kind == "name" and item2.kind == name
        """
        if item1 in self.vertices and item2 in self.vertices:
                return self.vertices[item1].score_custom(self.vertices[item2],
                                                          first_choice, second_choice, last_choice)
        else:
            raise ValueError


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    import python_ta
    python_ta.check_all(config={
        'max-line-length': 120,
        'max-nested-blocks': 4
    })