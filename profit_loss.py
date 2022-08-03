from pathlib import Path
import re

fp = Path.cwd()/"csv_reports"/"profit-and-loss-usd.csv"
# Create a file path to profit-and-loss-usd.csv
file = Path.cwd()/"summary_report.txt"
# Create a file path to file summary_report

def profitloss_function(forex):
# Create a function
    with file.open(mode= 'a', encoding = 'UTF-8', newline = '') as text:
    # Open the summary_report text file
        try:
        # Create an exception
            with fp.open(mode="r", newline='') as pal:
            # Open the file
                next(pal)
                # Skip the header
                prevday=0
                npdiff=0
                # Let variables prevday and paldiff be 0
                surplus=1
                # Let variable surplus be 1

                for line in pal.readlines():
                # Read profit-and-loss-usd.csv line by line
                    try:
                    # Create an exception
                        line = re.findall(r'[0-9]+.', line)
                        # Find all the net profit data
                        npdiff = float(line[4]) - prevday
                        # Make npdiff be the line of data minus the previous line of data for net profit in profit and loss
                        prevday = float(line[4])
                        # Make prevday be the line of data for net profit in profit and loss
                        
                        if npdiff <0:
                        # If npdiff is less than 0
                            npdiff = abs(npdiff)
                            # Make it positive
                            text.writelines(f'[PROFIT DEFICIT] DAY: {line[0]} AMOUNT: SGD{round(npdiff*forex,1)}\n')
                            # Print [PROFIT DEFICIT] DAY: {line[0]} AMOUNT: SGD{npdiff*forex}
                            surplus=0
                            # Then variable surplus will be 0
                        
                    except IndexError:
                        print("The data is not a number")
                    # Exception if the data in the csv file is not a number

                if surplus==1:
                # If surplus is really 1
                    text.writelines('[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n')
                    # Write [NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY

        except FileNotFoundError:
            print("The file is unavailable")
        # Exception if the file is unvailable 