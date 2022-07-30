from pathlib import Path
import re



fp = Path.cwd()/"csv_reports"/"overheads-day-42.csv"
#Create a file path to overheads-day-41.csv
file = Path.cwd()/"csv_reports"/"summary_report.txt"
#Create a file path to file summary_report 


def overhead_function(forex):
    #Create a function
    with file.open(mode = 'a', encoding = 'UTF-8', newline = '') as text:
    #Open the summary_report text file 
        with fp.open(mode='r', mewline='') as overheads:
            #Open the file
            next(overheads)
            #Skip the header
            max_value = float(0)
            #Let variable max_value be float 0

            for line in overheads.readlines():
            #Read overheads-day-41.csv line by line 
                line = line.split(",")
                #split the line on ","
                category =  line[0].strip('"').strip('"').upper()
                #Find the respective  categories
                overheads = re.findall(r'[0-9].+[0-9].+' , line[1]) 
                #Find the overhead values
                a = float(overheads[0])
                #Let variable a be overhead values



                if a > max_value:
                    #If a is more than max_value
                    max_value = a
                    #a becomes the new max value 



            text.writelines(f"[HIGHEST OVERHEADS] {category}, EXPENSE: SGD{max_value*forex}\n")
            #Write [HIGHEST OVERHEADS] with the variable category, EXPENSE: SGD with the variable max_value 
