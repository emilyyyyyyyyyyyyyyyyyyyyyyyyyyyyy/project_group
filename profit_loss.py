from pathlib import Path
import re

fp = Path.cwd()/"csv_reports"/"profit-and-loss-usd.csv"
file = Path.cwd()/"csv_reprts"/"summary_report.txt"

def profitloss_function(forex):
    with file.open(mode= 'a', encoding = 'UTF-8', newline = '') as text:
        with fp.open(mode="r", newline='') as pal:
            next(pal)
            prevday=0
            npdiff=0