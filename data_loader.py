import csv
import importlib.util
from typing import Optional

from similarity_score_calculation import _Vertex, Graph

class Exercise:
    """
    An exercise and its categories

    Instance Attributes:
    - name: The name of the exercise
    - force: The force the exercise targets
    - level: The level of the exercise
    - mechanic: The mechanic of the exercise
    - equipment: The equipment needed for the exercise
    - muscles: The primary and secondary muscle(s) targeted by the exercise
    - instructions: The instructions for the exercise
    - category: The category of the exercise
    - images: The images of the exercise


    Representation Invariants:
    - self.name != ""
    """

    name: str
    force: str
    level: str
    mechanic: Optional[str]
    equipment: Optional[str]
    muscles: list[str]
    instructions: str
    category: str
    images: list[str]

    def __init__(self, name: str, force: str, level: str, mechanic:Optional[str], equipment:Optional[str],
                muscles: Optional[str], instructions: str, category: str, images: list[str]) -> None:
        """Initialize an exercise with the given properties"""
        self.name = name
        self.force = force
        self.level = level
        self.mechanic = mechanic
        self.equipment = equipment
        self.muscles = muscles
        self.instructions = instructions
        self.category = category
        self.images = images


def parse_list_field(field_str):
    """Convert a string representing a list (e.g., "[abdominals]") into a Python list."""
    # Remove enclosing square brackets and strip whitespace.
    field_str = field_str.strip("[]").strip()
    if not field_str:
        return []
    # Split on commas and remove any extra quotes or spaces.
    return [item.strip().strip('"').strip("'") for item in field_str.split(',')]

def get_all_exercises():
    exercises = []
    # Open and read the CSV file.
    with open('cleaned_data.csv', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row.
        # Expected header columns: id,name,force,level,mechanic,equipment,
        # primaryMuscles,secondaryMuscles,instructions,category,images,id
        for row in reader:
            # Create an Exercise instance.
            exercise = Exercise(
                name = row[1],
                force = row[2],
                level = row[3],
                mechanic = row[4] if row[4] else None,
                equipment = row[5] if row[5] else None,
                muscles = parse_list_field(row[6]) + parse_list_field(row[7]),
                instructions = row[8],
                category = row[9],
                images = parse_list_field(row[10])
            )
            exercises.append(exercise)

# Print the first 5 loaded Exercise objects for verification.
    for ex in exercises[:5]:
        print(vars(ex))


get_all_exercises()



if __name__ == '__main__':
    import doctest
    doctest.testmod()

    import python_ta
    python_ta.check_all(config={
        'max-line-length': 120,
        'max-nested-blocks': 4,
        'extra-imports': ["csv", "importlib.util"]
    })
