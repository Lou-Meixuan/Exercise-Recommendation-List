"""CSC111 Winter 2025 Project2 - Recommendation System For Gym Exercises: Workout Wizard

Module Description
==================
This is the main file for our project

Copyright and Usage Information
===============================
This file is created solely by students (Meixuan Lou, Zimo Huang, Hongyi Mei, Yunji Hwang) taking CSC111 at the
University of Toronto St. George campus. All forms of distribution of this code, whether as given or with any changes,
are expressly prohibited.

This file is Copyright (c) 2025 CSC111 Student Team: Meixuan Lou, Zimo Huang, Hongyi Mei, Yunji Hwang
"""
import tkinter as tk
from user_interface import ExerciseRecommendationApp

root = tk.Tk()
app = ExerciseRecommendationApp(root)
root.mainloop()