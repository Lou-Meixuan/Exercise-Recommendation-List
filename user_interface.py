import tkinter as tk
from tkinter import ttk  # widgets
import data_loader
from similarity_score_calculation import Graph

class ExerciseRecommendationApp:
    """
    A GUI app for exercise recommendation based on user input.
    
    Preconditions:
        - 
    """

    def __init__(self, root):
        """Initialize the app with a Tkinter root window."""
        self.root = root
        self.root.geometry("800x600")
        self.root.title("Workout Wizard")
        
        self.exercises = data_loader.get_all_exercises()
        self.exercise_names = [exercise.properties[0] for exercise in self.exercises]
        self.graph = Graph(self.exercises)

        # store user selections
        self.selected_exercises = tk.StringVar()
        self.selected_score_type = tk.StringVar()
        self.first_choice = tk.StringVar()
        self.second_choice = tk.StringVar()
        self.last_choice = tk.StringVar()

        # default values
        self.selected_exercises.set("Pick an exercise you enjoy or find rewarding!")
        self.selected_score_type.set("Pick your preferred recommendation type")
        self.first_choice.set("Pick your first choice")
        self.second_choice.set("Pick your second choice")
        self.last_choice.set("Pick your third choice")

        # frames/screens
        self.exercise_frame = tk.Frame(self.root)
        self.calculation_frame = tk.Frame(self.root)
        self.recommendation_frame = tk.Frame(self.root)

        # initialize frames
        self.setup_exercise_screen()
        self.setup_calculation_screen()
        self.setup_recommendation_screen()

        # start with the exercise frame
        self.show_exercise_screen()

    def setup_exercise_screen(self):
        """set the exercise picking screen w/ dropdown"""

        title_label = tk.Label(self.exercise_frame, text="Pick an exercise to use for your recommendations!", font=("Helvetica", 24, "bold"))
        title_label.pack()

        description = tk.Label(self.exercise_frame, 
                               text="Select an exercise from the dropdown menu below:", 
                               font=("Helvetica", 16))
        description.pack()

        exercise_label = tk.Label(self.exercise_frame, text="Exercise:", font=("Helvetica", 14))
        exercise_label.pack()

        # combobox: dropdown and scroll bar and entry
        self.exercise_combobox = ttk.Combobox(self.exercise_frame,
                                              textvariable=self.selected_exercises,
                                              values=self.exercise_names,
                                              width=50)
        self.exercise_combobox.pack(pady=5)

        next_button = tk.Button(self.exercise_frame, text="Next", 
                                command=self.show_calculation_screen,
                                font=("Helvetica", 12),
                                width=20, height=2,
                                bg="lightblue", fg="black")
        next_button.pack()

    def setup_calculation_screen(self):
        """Set up the calculation screen"""
        title_label = tk.Label(self.calculation_frame,
                               text='Select calculation method',
                               font=("Helvetica", 24, "bold"))
        title_label.pack()

        description = tk.Label(self.calculation_frame,
                               text="Choose how you want to calculate exercise recommendations",
                               font=("Helvetica", 12))
        description.pack()

        score_frame = tk.Frame(self.calculation_frame)
        score_frame.pack(pady=10)

        score_label = tk.Label(score_frame,
                               text="Recommendation type:",
                               font=("Helvetica", 14))
        score_label.pack(anchor="w")
        
        score_options = ["popular", "unpopular", "custom"]

        # radio buttons for score type:
        for option in score_options:
            rb = tk.Radiobutton(score_frame,
                                text=option,
                                variable=self.selected_score_type,
                                value=option,
                                font=("Helvetica", 12))
            rb.pack(anchor="w", pady=5)
        
        # custom calculation options (only show when custom is selected!!!)
        self.custom_frame = tk.Frame(self.calculation_frame)
        self.custom_frame.pack(pady=20, fill="x")


root = tk.Tk()
root.mainloop()    