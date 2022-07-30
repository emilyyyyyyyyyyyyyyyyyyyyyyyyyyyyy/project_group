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
                
            for line in pal.readlines():
                line = re.findall(r'[0-9]+.', line)
                npdiff = float(line[4]) - prevday
                prevday = float(line[4])

                if npdiff <0:
                    npdiff = abs(npdiff)
                    text.writelines(f'[PROFIT DEFICIT] DAY: {line[0]}, AMOUNT: SGD{npdiff*forex}')
                else:
                    text.writelines(['[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY'])