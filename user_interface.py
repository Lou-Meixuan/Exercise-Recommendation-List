"""CSC111 Winter 2025 Project2: Recommendation System For Gym Exercises

Module Description
==================
This module contains the user interface class and its methods.

Copyright and Usage Information
===============================
This file is created solely by students (Meixuan Lou, Zimo Huang, Hongyi Mei, Yunji Hwang) taking CSC111 at the
University of Toronto St. George campus. All forms of distribution of this code, whether as given or with any changes,
are expressly prohibited.

This file is Copyright (c) 2025 CSC111 Student Team: Meixuan Lou, Zimo Huang, Hongyi Mei, Yunji Hwang
"""

import tkinter as tk
from tkinter import ttk  # widgets
import data_loader
import os
from PIL import Image, ImageTk  # Import Pillow modules


class ExerciseRecommendationApp:
    """
    A GUI app for exercise recommendation based on user input.
    
    Instance Attributes:
        - root: Tkinter root window
        - exercises: list of all available exercises from data loader
        - exercise_names: list of exercise names for the dropdown menu
        - graph: a graph representation of the exercises
        - selected_exercises: the exercise selected by the user
        - selected_score_type: the calculation type selected by the user
        - first_choice: the 1st custom choice selected by the user
        - second_choice: the 2nd custom choice selected by the user
        - last_choice: the 3rd and last custom choice selected by the user
        - exercise_frame: frame for the exercise selection screen
        - calculation_frame: frame for the calculation method selection screen
        - recommendation_frame: The frame for the recommendation results screen
    """

    def __init__(self, root):
        """Initialize the app with a Tkinter root window."""
        self.root = root
        self.root.geometry("800x1000")
        self.root.title("Workout Wizard")
        
        self.exercises = data_loader.get_all_exercises()
        self.exercise_names = [exercise.properties[0] for exercise in self.exercises]
        self.graph = data_loader.create_graph(self.exercises)

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
        self.results_frame = tk.Frame(self.root)

        # initialize frames
        self.setup_exercise_screen()
        self.setup_calculation_screen()
        self.setup_results_screen()

        # start with the exercise frame
        self.show_exercise_screen()


    def setup_exercise_screen(self):
        """set the exercise picking screen w/ dropdown"""

        title_label = tk.Label(self.exercise_frame, text="Pick an exercise to use for your recommendations!", 
                               font=("Helvetica", 24, "bold"))
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

        custom_label = tk.Label(self.custom_frame,
                                text="Custom calculation preferences.\n"
                                "For more accurate recommendations,\n"
                                "please do not select any option more than once!",
                                font=("Helvetica", 14))
        custom_label.pack()

        # category options 
        category_options = [
            "force",
            "level",
            "mechanic",
            "equipment",
            "primary muscles",
            "secondary muscles"
        ]

        # first choice
        first_choice_frame = tk.Frame(self.custom_frame)
        first_choice_frame.pack(pady=5, fill="x")

        first_choice_label = tk.Label(first_choice_frame,
                                      text="First priority:",
                                      font=("Helvetica", 12))
        first_choice_label.pack(padx=5)

        first_choice_dropdown = ttk.Combobox(first_choice_frame, textvariable=self.first_choice, values=category_options, width=30)
        first_choice_dropdown.pack(padx=5)

        # second choice
        second_choice_frame = tk.Frame(self.custom_frame)
        second_choice_frame.pack(fill="x", pady=5)
        
        second_choice_label = tk.Label(second_choice_frame, text="Second priority:", font=("Helvetica", 12))
        second_choice_label.pack(padx=5)
        
        second_choice_dropdown = ttk.Combobox(second_choice_frame, 
                                            textvariable=self.second_choice,
                                            values=category_options,
                                            width=30)
        second_choice_dropdown.pack(padx=5)

        # last choice
        last_choice_frame = tk.Frame(self.custom_frame)
        last_choice_frame.pack(fill="x", pady=5)
        
        last_choice_label = tk.Label(last_choice_frame, text="Third priority:", font=("Helvetica", 12))
        last_choice_label.pack(padx=5)
        
        last_choice_dropdown = ttk.Combobox(last_choice_frame, 
                                          textvariable=self.last_choice,
                                          values=category_options,
                                          width=30)
        last_choice_dropdown.pack(padx=5)

        # HIDE CUSTOM FRAME (only show when custom is selected)
        self.custom_frame.pack_forget()

        # trace to show/hide
        self.selected_score_type.trace("w", self.toggle_custom_frame)

        # buttons
        button_frame = tk.Frame(self.calculation_frame)
        button_frame.pack()

        back_button = tk.Button(button_frame, text="Back", 
                                   command=self.reset_and_show_exercise_screen,
                                   font=("Helvetica", 12),
                                   width=15, height=2,
                                   bg="lightblue", fg="black")
        back_button.pack(padx=10)

        calculate_button = tk.Button(button_frame,
                                     text="Calculate",
                                     command=self.calculate_and_show_results,
                                     font=("Helvetica", 12),
                                     width=15, height=2)
        calculate_button.pack(padx=10)

    def setup_results_screen(self):
        """Setup the results screen"""
        title_label = tk.Label(self.results_frame,
                               text="Recommended Exercises",
                               font=("Helvetica", 24, "bold"))
        title_label.pack()

        # selected exercise label
        self.selected_exercise_label = tk.Label(self.results_frame, text="Based on your entries: ", font=("Helvetica", 14))
        self.selected_exercise_label.pack()

        # results frame
        results_container = tk.Frame(self.results_frame)
        results_container.pack(fill="both", expand=True)

        # create a frame for each recommendation (might add pics to each later)
        self.recommendation_frames = []
        for i in range(3):
            rec_frame = tk.Frame(results_container, relief=tk.RIDGE, borderwidth=2)
            rec_frame.pack(pady=10, fill="x", padx=50)
            
            rec_title = tk.Label(rec_frame, text=f"Recommendation {i + 1}", font=("Helvetica", 14, "bold"))
            rec_title.pack(pady=5)
            
            rec_name = tk.Label(rec_frame, text="", font=("Helvetica", 12))
            rec_name.pack(pady=5)
            
            self.recommendation_frames.append((rec_frame, rec_name))

        # nav buttons
        button_frame = tk.Frame(self.results_frame)
        button_frame.pack()

        back_button = tk.Button(button_frame, text="Back to Calculation",
                                command=self.show_calculation_screen,
                                font=("Helvetica", 12),
                                width=20, height=2)
        back_button.pack(padx=10, side=tk.LEFT)

        new_search_button = tk.Button(button_frame, text="New Search",
                                      command=self.show_exercise_screen,
                                      font=("Helvetica", 12),
                                      width=20, height=2)
        new_search_button.pack(padx=10, side=tk.LEFT)

    def toggle_custom_frame(self, *args):
        if self.selected_score_type.get() == "custom":
            self.custom_frame.pack(fill="x", pady=20,
                                   after=self.calculation_frame.winfo_children()[2])
        else:
            self.custom_frame.pack_forget()

    def show_exercise_screen(self):
        """Show the exercise screen"""
        self.calculation_frame.pack_forget()
        self.results_frame.pack_forget()
        self.exercise_frame.pack(fill="both", expand=True)
        self.root.update_idletasks()

    def show_calculation_screen(self):
        """Show the calculation screen"""
        self.exercise_frame.pack_forget()
        self.results_frame.pack_forget()
        self.calculation_frame.pack(fill="both", expand=True)

        # clear the images from the recommendation frame
        rec_frame, _ = self.recommendation_frames[0]
        if rec_frame:
            for widget in rec_frame.winfo_children():
                if isinstance(widget, tk.Label) and hasattr(widget, 'image'):
                    widget.destroy()

        # toggle custom based on current selection
        self.toggle_custom_frame()
        self.root.update_idletasks()

    def show_results_screen(self):
        """Show the results screen"""
        self.exercise_frame.pack_forget()
        self.calculation_frame.pack_forget()
        self.results_frame.pack(fill="both", expand=True)
        self.root.update_idletasks()

    def reset_and_show_exercise_screen(self):
        """Reset selections & go back to prev screen"""
        self.selected_exercises.set("Pick an exercise you enjoy or find rewarding!")
        self.selected_score_type.set("Pick your preferred recommendation type")
        self.first_choice.set("Pick your first choice")
        self.second_choice.set("Pick your second choice")
        self.last_choice.set("Pick your third choice")
        self.show_exercise_screen()

    def calculate_and_show_results(self):
        """Calculate recs and show results, including pictures & instructions for #1 rec"""
        exercise = self.selected_exercises.get()
        score_type = self.selected_score_type.get()

        self.selected_exercise_label.config(text=f"Based on your entries: {exercise}")

        recommendations = []

        if score_type == "popular":
            recommendations = self.graph.popular_recommendation(exercise)
        elif score_type == "unpopular":
            recommendations = self.graph.not_popular_recommendation(exercise)
        elif score_type == "custom":
            choice_lst = [
                self.first_choice.get(),
                self.second_choice.get(),
                self.last_choice.get()
            ]
            recommendations = self.graph.custom_recommendation(exercise, choice_lst)

        # get name of the #1 recommendation
        first_recommendation = recommendations[0] if recommendations else None

        # update frames
        for i, (_, name_label) in enumerate(self.recommendation_frames):
            if i < len(recommendations):
                name_label.config(text=recommendations[i])
            else:
                name_label.config(text="No recommendations available :(")

        # display the instructions and images for the #1 rec
        if first_recommendation:
            try:
                # replace spaces with hyphens in the directory name
                exercise_dir_name = first_recommendation.replace(" ", "_")
                exercise_dir = os.path.join("exercises", exercise_dir_name)
                image_path_0 = os.path.join(exercise_dir, "0.jpg")
                image_path_1 = os.path.join(exercise_dir, "1.jpg")

                # load the 2 images
                img0 = Image.open(image_path_0)
                img1 = Image.open(image_path_1)

                # resize the images
                img0 = img0.resize((200, 200))
                img1 = img1.resize((200, 200))

                tk_img0 = ImageTk.PhotoImage(img0)
                tk_img1 = ImageTk.PhotoImage(img1)

                # display images in the recommendation frame
                rec_frame, _ = self.recommendation_frames[0]

                # clear existing images
                for widget in rec_frame.winfo_children():
                    if isinstance(widget, tk.Frame):
                        for img_widget in widget.winfo_children():
                            img_widget.destroy()
                        widget.destroy()

                # create a frame to hold the images side by side
                image_frame = tk.Frame(rec_frame)
                image_frame.pack()

                image_label_0 = tk.Label(image_frame, image=tk_img0)
                image_label_0.image = tk_img0  # keep a reference to prevent garbage collection
                image_label_0.pack(side="left")

                image_label_1 = tk.Label(image_frame, image=tk_img1)
                image_label_1.image = tk_img1  # keep a reference to prevent garbage collection
                image_label_1.pack(side="left")

            except FileNotFoundError:
                print(f"File not found: {exercise_dir}")
            except Exception as e:
                print(f"Error displaying images: {e}")
        
        # show results screen
        self.show_results_screen()


if __name__ == "__main__":
    # import python_ta

    # python_ta.check_all(config={'extra-imports': [], 'allowed-io': [], 'max-line-length': 120})

    root = tk.Tk()
    app = ExerciseRecommendationApp(root)
    root.mainloop()
