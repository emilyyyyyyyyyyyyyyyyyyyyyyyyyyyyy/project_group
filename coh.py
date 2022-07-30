from pathlib import Path
import re

fp = Path.cwd()/"csv_reports"/"cash-on-hand-usd.csv"
# Create a file path to cash-on-hand-usd.csv
file = Path.cwd()/"csv_reports"/"summary_report.txt"
# Create a file path to file summary_report

def coh_function(forex):
    # Create a function
    with file.open(mode = 'a', encoding = 'UTF-8', newline = '') as text:
        # Open the summary_report text file
        with fp.open(mode="r", newline='') as coh:
            # Open the cash-on-hand-usd csv file
            next(coh)
            # Skip the header
            prevday=0
            cohdiff=0
            # Let variables prevday and cohdiff be 0

            for line in coh.readlines():
                line = re.findall(r'[0-9]+.',line)
                cohdiff = float(line[1]) - prevday
                prevday = float(line[1])

                if cohdiff <0:
                    cohdiff = abs(cohdiff)
                    text.writelines(f"[CASH DEFICIT] DAY: {line[0]} AMOUNT:SGD{cohdiff*forex}\n")
