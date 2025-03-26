from similarity_score_calculation import Graph
import os
import json

def load_whole_graph(filename:str) -> Graph:
    """Return an exercise graph corresponding to the given datasets.

    Preconditions:
        - filename is the path to a html file corresponding to the exercise data
        - each book ID in reviews_file exists as a book ID in book_names_file
    """
    graph = Graph()
    name_list = ["force", "level", "mechanic", "equipment", "primary_muscles", "secondary_muscles"]
    with open(filename, 'r') as f:
        html_string = f.read()
        for row in html_string:
            exercise_name = row[1]
            graph.add_vertex(exercise_name, "name")
            for index in range(6):
                prop = row[index + 2]
                if type(prop) is list:
                    load_lists(prop, exercise_name, graph, index)
                elif prop is not None:
                    graph.add_vertex(prop, name_list[index])
                    graph.add_edge(exercise_name, prop)
    return graph

def load_lists(prop:list[str], exercise_name:str, graph:Graph, index:int)-> None:
    if index == 4:
        for each in prop:
            graph.add_vertex(prop, "primary_muscles")
            graph.add_edge(exercise_name, prop)
    if index == 5:
        for each in prop:
            graph.add_vertex(prop, "secondary_muscles")
            graph.add_edge(exercise_name, prop)
