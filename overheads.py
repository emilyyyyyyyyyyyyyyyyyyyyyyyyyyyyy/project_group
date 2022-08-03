from pathlib import Path
import re

file_path = Path.cwd()/"csv_reports"/"overheads-day-42.csv"
# Create a file path to overheads-day-41.csv
file = Path.cwd()/"csv_reports"/"summary_report.txt"
# Create a file path to file summary_report 


def overhead_function(forex):
# Create a function 
# function requires parameter: forex
    with file.open(mode = 'a', encoding = 'UTF-8', newline = '') as text:
    # Open the summary_report text file 
        with file_path.open(mode='r', newline='') as overheads:
        # Open the file
            next(overheads)
            # Skip the headers
            max_value = float(0)
            # Let variable max_value be float 0

            try:
                for line in overheads.readlines():
                # Read overheads-day-41.csv line by line 
                    line = line.split(",")
                    # Split the line at ","
                    category =  line[0].strip('"').strip('"').upper()
                    # Find the respective categories
                    overheads = re.findall(r'[0-9].+[0-9].+' , line[1]) 
                    # Find the respective overhead values
                    a = float(overheads[0])
                    # Let variable a be the overhead values


                    if a > max_value:
                    # If a is more than max_value
                        max_value = a
                        # a will overwrite the old value, and become the new max value 
                        text.writelines(f"[HIGHEST OVERHEADS] {category}, EXPENSE: SGD{max_value*forex}\n")
                        # Write [HIGHEST OVERHEADS] with the variable category, EXPENSE: SGD with the variable max_value with f strings
            
            except IndexError:
                print("The data is not a number")
