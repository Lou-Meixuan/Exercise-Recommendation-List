"""CSC111 Winter 2025 Project2 - Recommendation System For Gym Exercises: Workout Wizard

Module Description
==================
This module contains the functions to clean up the dataset for our project

Copyright and Usage Information
===============================
This file is created solely by students (Meixuan Lou, Zimo Huang, Hongyi Mei, Yunji Hwang) taking CSC111 at the
University of Toronto St. George campus. All forms of distribution of this code, whether as given or with any changes,
are expressly prohibited.

This file is Copyright (c) 2025 CSC111 Student Team: Meixuan Lou, Zimo Huang, Hongyi Mei, Yunji Hwang
"""
import re
import csv


def clean_field(field: str) -> list | str:
    """Clean the data"""
    # check if the field looks like a list (starts with '[' and ends with ']')
    if field.startswith('[') and field.endswith(']'):
        # extract all the words between double quotes
        words = re.findall(r'"([^"]+)"', field)
        if words:
            return words  # Return as a real list
        else:
            return []  # Return empty list if no words found
    return field  # Return as-is if not a list


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    import python_ta
    python_ta.check_all(config={
        'max-line-length': 120,
        'max-nested-blocks': 4,
        'extra-imports': ["csv", "re"],
        'allow-local-imports': True,
        "forbidden-io-functions": None
    })

    # open input file and create an output CSV
    with (open('data/ugly_data_exercises.txt', 'r', encoding='utf-8', newline='') as infile,
          open('data/cleaned_data.csv', 'w', encoding='utf-8', newline='') as outfile):
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        for row in reader:
            cleaned_row = [clean_field(cell) for cell in row]
            writer.writerow(cleaned_row)
