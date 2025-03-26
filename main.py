from similarity_score_calculation import Graph

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
                graph.add_vertex(prop, name_list[index])
                graph.add_edge(exercise_name, prop)
    return graph