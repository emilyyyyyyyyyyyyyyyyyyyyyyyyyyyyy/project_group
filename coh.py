from pathlib import Path
import re

fp = Path.cwd()/"csv_reports"/"cash-on-hand-usd.csv"
# Create a file path to 
file = Path.cwd()/"csv_reports"/"summary_report.txt"

def coh_function(forex):
    # Create a function
    with file.open(mode = 'a', encoding = 'UTF-8', newline = '') as text:
        # Open the summary_report text file
        try:
        # Create an exception
            with fp.open(mode='r', newline='') as coh:
            # Open the cash-on-hand-usd csv file
                next(coh)
                # Skip the header
                prevday=0
                cohdiff=0
                # Let variable prevday and cohdiff be 0
                cash=1
                # Let variable cash be 1

                for line in coh.readlines():
                # Read cash-on-hand-usd.csv line by line
                    try:
                        line = re.findall(r'[0-9]+.',line)
                        # Find all the Cash on hand data
                        cohdiff = float(line[1]) - prevday
                        # Make cohdiff be the line of data minus the previous line of data for cash on hand
                        prevday = float(line[1])
                        # Make prevday be the line of data for cash of hand
                        if cohdiff <0:
                        # If Cash on hand is less than 0
                            cohdiff = abs(cohdiff)
                            # Make it positive
                            text.writelines(f"[CASH DEFICIT] DAY: {line[0]} AMOUNT:SGD{cohdiff*forex}\n")
                            # Write [CASH DEFICIT] DAY: with the variable line [0], AMOUNT: SGD with the variable cohdiff*forex"
                            cash=0
                            # Then variable cash will be 0

                    except IndexError:
                        print("The data is not a number")
                    

                if cash==1:
                # If variable cash is really 1
                    text.writelines("[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n")
                    # Write [CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY

        except FileNotFoundError:
            print("The file is unavailable")
        # Exception if the file is unavailable

                        
                
                