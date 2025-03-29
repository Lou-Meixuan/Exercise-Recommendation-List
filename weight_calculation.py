"""CSC111 Winter 2025 Project2: Recommendation System For Gym Exercises

Module Description
==================
This module contains the _Vertex and Graph classes, and the functions for our project

Copyright and Usage Information
===============================
This file is created solely by students (Meixuan Lou, Zimo Huang, Hongyi Mei, Yunji Hwang) taking CSC111 at the
University of Toronto St. George campus. All forms of distribution of this code, whether as given or with any changes,
are expressly prohibited.

This file is Copyright (c) 2025 CSC111 Student Team: Meixuan Lou, Zimo Huang, Hongyi Mei, Yunji Hwang
"""
from __future__ import annotations
from typing import Any
import math


class _Vertex:
    """A vertex or a node in the graph holding an item of the exercise class"

    Instance Attributes:
    - item: The item of the exercise class
    - neighbours: All the vertices that adjacent to this vertex
    - kind: The category that the item is belonged to
    """
    item: Any
    neighbours: set[_Vertex]
    kind: str

    def __init__(self, item: Any, neighbours: set[_Vertex], kind: str) -> None:
        """
        Initialize a new vertex with the given item and neighbours.

        Preconditions:
            - kind in ['name', 'force', 'level', 'mechanic', 'equipment', 'muscles']
        """
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
        adjacent_to_self = set(self.neighbours)
        adjacent_to_other = set(other.neighbours)
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
        adjacent_to_self = set(self.neighbours)
        adjacent_to_other = set(other.neighbours)
        adjacent_to_both = adjacent_to_self.intersection(adjacent_to_other)
        number_list = [len(w.neighbours) for w in adjacent_to_both]
        if len(adjacent_to_both) == 0:
            return 0.0
        else:
            return sum([1 / math.log(each, 10) for each in number_list])

    def score_custom(self, other: Any, choice_lst: list[str]) -> float:
        """
        Return the similarity score where it's based on the user customization. User will enter three choices, where
        indicates the primary aspect, secondary aspect and the trivial aspect that the value for their exercise.
        The first choice will be valued as 6, the second choice will be valued as 4, and the last choice will be valued
        as 1, and other aspects will be valued as 2 each.

        Preconditions:
            - len(choice_lst) == 3
            - choice_lst[0] in ['force', 'level', 'mechanic', 'equipment', 'muscles']
            - choice_lst[1] in ['force', 'level', 'mechanic', 'equipment', 'muscles']
            - choice_lst[2] in ['force', 'level', 'mechanic', 'equipment', 'muscles']
            - self.kind == "name"
            - other.kind == "name"
        """
        adjacent_to_self = set(self.neighbours)
        adjacent_to_other = set(other.neighbours)
        adjacent_to_both = adjacent_to_self.intersection(adjacent_to_other)
        score = 0.0
        for v in adjacent_to_both:
            if v.kind == choice_lst[0]:
                score += 6.0
            elif v.kind == choice_lst[1]:
                score += 4.0
            elif v.kind == choice_lst[2]:
                score += 1.0
            else:
                score += 2.0
        return score


def get_list(lst: list) -> list:
    """
    Return a new list from the list of tuples. This list only contains the index1 items of the first three
    elements in the lst.
    """
    new_lst = [i[1] for i in lst]
    return new_lst[0:3]


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

    def add_vertex(self, item: Any, kind: Any) -> None:
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

    def get_score_popular(self, item1: str, item2: str) -> float:
        """Return the similarity score of score_popular between the two given items in this graph.
        Raise a ValueError if item1 or item2 do not appear as vertices in this graph.

        Preconditions:
            - item1.kind == "name" and item2.kind == name
        """
        if item1 in self.vertices and item2 in self.vertices:
            return self.vertices[item1].score_popular(self.vertices[item2])
        else:
            raise ValueError

    def get_score_unpopular(self, item1: Any, item2: Any) -> float:
        """Return the similarity score of score_unpopular between the two given items in this graph.
        Raise a ValueError if item1 or item2 do not appear as vertices in this graph.

        Preconditions:
            - item1.kind == "name" and item2.kind == name
        """
        if item1 in self.vertices and item2 in self.vertices:
            return self.vertices[item1].score_unpopular(self.vertices[item2])
        else:
            raise ValueError

    def get_score_custom(self, item1: Any, item2: Any, choice_lst: list[str]) -> float:
        """Return the similarity score between the two given items in this graph.
        Raise a ValueError if item1 or item2 do not appear as vertices in this graph.

        Preconditions:
            - item1.kind == "name" and item2.kind == name
        """
        if item1 in self.vertices and item2 in self.vertices:
            return self.vertices[item1].score_custom(self.vertices[item2], choice_lst)
        else:
            raise ValueError

    def get_name_vertices(self) -> set:
        """Return a set of vertices' items. All the vertices that were selected will have the kind 'name'"""
        return_set = set()
        for v in self.vertices:
            if self.vertices[v].kind == "name":
                return_set.add(v)
        return return_set

    def popular_recommendation(self, name_input: str) -> list:
        """
        Return a recommendation list with length 3. The recommendation list used the 'get_score_popular' method of
        the graph, and generate a list of tuple(index 0 is the similarity score and index 1 is the item of the vertex).
        Then sort the list by index0 of the tuple and return the first three item with large score.
        """
        name_set = self.get_name_vertices()
        lst = []
        for name in name_set:
            if name != name_input:
                score = self.get_score_popular(name_input, name)
                lst.append((score, name))
        return_lst = sorted(lst, key=lambda x: (-x[0], x[1]), reverse=True)
        return get_list(return_lst)[0:3]

    def not_popular_recommendation(self, name_input: str) -> list:
        """
        Return a recommendation list with length 3.The recommendation list used the 'get_score_unpopular' method of
        the graph, and generate a list of tuple(index 0 is the similarity score and index 1 is the item of the vertex).
        Then sort the list by index0 of the tuple and return the first three item with large score.
        """
        name_set = self.get_name_vertices()
        lst = []
        for name in name_set:
            if name != name_input:
                score = self.get_score_unpopular(name_input, name)
                lst.append((score, name))
        return_lst = sorted(lst, key=lambda x: (-x[0], x[1]), reverse=True)
        return get_list(return_lst)[0:3]

    def custom_recommendation(self, name_input: str, choice_lst: list[str]) -> list:
        """
        Return a recommendation list with length 3.The recommendation list used the 'get_score_unpopular' method of
        the graph, and generate a list of tuple(index 0 is the similarity score and index 1 is the item of the vertex).
        Then sort the list by index0 of the tuple and return the first three item with large score.
        """
        name_set = self.get_name_vertices()
        lst = []
        for name in name_set:
            if name != name_input:
                score = self.get_score_custom(name_input, name, choice_lst)
                lst.append((score, name))
        return_lst = sorted(lst, key=lambda x: (-x[0], x[1]), reverse=True)
        return get_list(return_lst)[0:3]


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    import python_ta
    python_ta.check_all(config={
        'max-line-length': 120,
        'max-nested-blocks': 4,
        'extra-imports': ["math", "tkinter"]
    })
