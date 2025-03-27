import re
import csv
import ast

def clean_field(field):
    # check if the field looks like a list (starts with '[' and ends with ']')
    if field.startswith('[') and field.endswith(']'):
        # extract all the words between double quotes
        words = re.findall(r'"([^"]+)"', field)
        if words:
            return words  # Return as a real list
        else:
            return []  # Return empty list if no words found
    return field  # Return as-is if not a list

# open input file and create an output CSV
with open('ugly_data_exercises.txt', 'r', encoding='utf-8', newline='') as infile, \
     open('cleaned_data.csv', 'w', encoding='utf-8', newline='') as outfile:
    
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    
    for row in reader:
        cleaned_row = [clean_field(cell) for cell in row]
        writer.writerow(cleaned_row)
