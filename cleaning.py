import re
import csv

# def clean_field(field):
#     # This regex matches a field that is exactly of the form:
#     # "[""some text""]"
#     pattern = r'^\["([^"]+)"\]$'
#     match = re.match(pattern, field)
#     if match:
#         return match.group(1)
#     return field
def clean_field(field):
    # Check if the field looks like a list (starts with '[' and ends with ']')
    if field.startswith('[') and field.endswith(']'):
        # Extract all the words between double quotes
        words = re.findall(r'"([^"]+)"', field)
        if words:
            # Reconstruct the list with the words separated by commas and a space
            return '[' + ', '.join(words) + ']'
    return field

# Open the input CSV and create an output CSV
with open('data_exercises.txt', 'r', encoding='utf-8', newline='') as infile, \
     open('cleaned_data.txt', 'w', encoding='utf-8', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    for row in reader:
        # Clean each field in the row
        cleaned_row = [clean_field(cell) for cell in row]
        writer.writerow(cleaned_row)
