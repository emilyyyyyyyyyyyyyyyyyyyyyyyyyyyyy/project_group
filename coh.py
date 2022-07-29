from pathlib import Path
import re 

fp = Path.cwd()/"csv_reports"/"cash-on-hand-usd.csv"
file = Path.cwd()/"csv_reports"/"summary_report.txt"

def coh_function(forex):
    with file.open(mode = 'a', encoding = 'UTF-8', newline = '') as text:
        with fp. open(mode="r", newline='') as coh:
            next(coh)
            prevday=0
            cohdiff=0

            for line in coh.readliness():
                line = re.findall(r'')