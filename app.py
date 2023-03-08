import pandas as pd
import time

datasource = pd.read_excel("Book1.xlsx")
loopValue = ""

while loopValue != "KISS THE RING":
    for i, value in datasource.iterrows():
            time.sleep(7)
            print("Execute: \n" + value[0] + "\n")