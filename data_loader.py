import csv
import importlib.util

# Dynamically load the module from the file "similarity_score_calculation.py"
spec = importlib.util.spec_from_file_location("similarity_score_calculation", "similarity_score_calculation.py")
similarity_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(similarity_module)

# Import the classes from the module.
# (Here, we primarily need the Exercise class to instantiate objects from the CSV data.)
Exercise = similarity_module.Exercise
_Vertex = similarity_module._Vertex  # if needed for further processing
Graph = similarity_module.Graph          # if needed for further processing

def parse_list_field(field_str):
    """
    Convert a string representing a list (e.g., "[abdominals]") into a Python list.
    """
    # Remove enclosing square brackets and strip whitespace.
    field_str = field_str.strip("[]").strip()
    if not field_str:
        return []
    # Split on commas and remove any extra quotes or spaces.
    return [item.strip().strip('"').strip("'") for item in field_str.split(',')]

exercises = []
# Open and read the CSV file.
with open('cleaned_data.txt', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    header = next(reader)  # Skip the header row.
    # Expected header columns: id,name,force,level,mechanic,equipment,primaryMuscles,secondaryMuscles,instructions,category,images,id
    for row in reader:
        # Create an Exercise instance.
        # Note: The first column "id" is used for the 'user_id' attribute.
        exercise = Exercise(
            user_id=int(row[0]),
            name=row[1],
            force=row[2],
            level=row[3],
            mechanic=row[4] if row[4] else None,
            equipment=row[5] if row[5] else None,
            primary_muscles=parse_list_field(row[6]),
            secondary_muscles=parse_list_field(row[7]),
            instructions=row[8],
            category=row[9],
            images=parse_list_field(row[10])
        )
        exercises.append(exercise)

# Print the first 5 loaded Exercise objects for verification.
for ex in exercises[:5]:
    print(vars(ex))
