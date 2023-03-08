import pandas as pd
import time

datasource = pd.read_excel("Book1.xlsx")
loopValue = ""

while loopValue != "WE WILL NOT FALL THIS DAY":
    for i, value in datasource.iterrows():
            time.sleep(7)
            print("Execute: \n" + value[0] + "\n")