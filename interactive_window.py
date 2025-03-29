import tkinter as tk
import data_loader

def calculate_similarity_score(exercise_name, score_type, first_choice=None, second_choice=None, last_choice=None):
    # Placeholder for similarity score calculation
    if score_type == "custom calculation":
        print(f"Calculating {score_type} score for: {exercise_name} with choices: {first_choice}, {second_choice}, {last_choice}")
    else:
        print(f"Calculating {score_type} score for: {exercise_name}")

root = tk.Tk()
root.geometry("600x800")
root.title("Workout Wizard")
label = tk.Label(root, text='Workout Wizard', font=("Courier", 30))
label.pack()

# extract exercise names from data_loader file
exercise_names = [exercise.name for exercise in data_loader.get_all_exercises()]

# Datatype of menu text for exercise selection
exercise_clicked = tk.StringVar()

# Initial menu text for exercise selection
exercise_clicked.set("Pick an exercise you enjoy or find rewarding!")

# dropdown menu options for similarity score type
score_options = [
    "popular",
    "unpopular",
    "custom calculation"
]

# datatype of menu text for score type selection
score_clicked = tk.StringVar()
# initial text for score type selection
score_clicked.set("Pick your preferred recommendation type")

# dropdown menu options for category selection
category_options = [
    'force',
    'level',
    'mechanic',
    'equipment',
    'primary_muscles',
    'secondary_muscles'
]

# datatype of menu text for category selection
first_choice_clicked = tk.StringVar()
second_choice_clicked = tk.StringVar()
last_choice_clicked = tk.StringVar()

# initial text for category selection
first_choice_clicked.set("Pick your first choice")
second_choice_clicked.set("Pick your second choice")
last_choice_clicked.set("Pick your last choice")

# function to update label and calculate similarity score
def show():
    selected_exercise = exercise_clicked.get()
    selected_score_type = score_clicked.get()
    first_choice = first_choice_clicked.get()
    second_choice = second_choice_clicked.get()
    last_choice = last_choice_clicked.get()
    label.config(text=selected_exercise)
    calculate_similarity_score(selected_exercise, selected_score_type, first_choice, second_choice, last_choice)

# dropdown menu for exercise selection
exercise_drop = tk.OptionMenu(root, exercise_clicked, *exercise_names)
exercise_drop.pack()

# dropdown menu for score type selection
score_drop = tk.OptionMenu(root, score_clicked, *score_options)
score_drop.pack()

# create a frame to hold the 3 category dropdowns
category_frame = tk.Frame(root)

# dropdown menu for first/second/third choice category selection
first_choice_drop = tk.OptionMenu(category_frame, first_choice_clicked, *category_options)
first_choice_drop.pack(side=tk.LEFT)

second_choice_drop = tk.OptionMenu(category_frame, second_choice_clicked, *category_options)
second_choice_drop.pack(side=tk.LEFT)

last_choice_drop = tk.OptionMenu(category_frame, last_choice_clicked, *category_options)
last_choice_drop.pack(side=tk.LEFT)

# button to submit
button = tk.Button(root, text="Select Exercise", command=show)
button.pack()

root.mainloop()
