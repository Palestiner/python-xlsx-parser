import pandas as pd
import os
import time
import codecs

configFile = codecs.open("app.txt", encoding="utf-8")
confList = configFile.readlines()

if len(confList) != 3:
    print("Invalid config file: number of lines",
          len(confList), ", should be 3.")
    SystemExit(1)
else:
    print("Valid config file")

fromFile = confList[0].strip()
xlsx = fromFile[fromFile.rindex("\\") + 1: fromFile.index(".") + 1] + "xlsx"
toDir = confList[1].strip()

try:
    pause = int(confList[2].strip())
except:
    pause = 5
    print("Invalid third parameter")

while True:
    try:
        if fromFile.endswith(".log"):
            df = pd.read_csv(fromFile, sep="\t", encoding="iso-8859-1")
            writer = pd.ExcelWriter(toDir + "\\" + xlsx, engine="xlsxwriter")
            df.to_excel(writer, "Лист1")
            writer.save()
    except:
        print("complete")
    time.sleep(pause * 60)
