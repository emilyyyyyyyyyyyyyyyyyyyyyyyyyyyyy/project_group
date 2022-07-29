import json, requests, re
from pathlib import Path

file = Path.cwd()/"csv_reports"/"summary_report.txt"
file.touch()
def api_function():
    with file.open(mode = "w") , encoding = 'UTF-8 , newline = '') as text:
        