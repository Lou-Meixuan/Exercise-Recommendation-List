from typing import annotations
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
    mechanic: str
    equipment: str
    primaryMuscles: str
    secondaryMuscles: str
    instructions: str
    category: str
    images: List[str]

    def __init__(self, id: int, name: str, force: str, level: str, mechanic: str, equipment: str, primaryMuscles: str, secondaryMuscles: str, instructions: str, category: str, images: List[str]) -> None:
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