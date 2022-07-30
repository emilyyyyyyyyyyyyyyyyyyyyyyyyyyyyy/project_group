from pathlib import Path
import re

fp = Path.cwd()/"csv_reports"/"cash-on-hand-usd.csv"
file = Path.cwd()/"csv_reports"/"summary_report.txt"

def coh_function(forex):
    