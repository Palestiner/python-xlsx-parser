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

fromDir = confList[0].strip()
toDir = confList[1].strip()

try:
    pause = int(confList[2].strip())
except:
    pause = 5
    print("Invalid third parametr")

filesList = os.listdir(fromDir)
while True:
    try:
        for file in filesList:
            if file.endswith(".log"):
                df = pd.read_csv(fromDir + "\\" + file,
                                sep="\t", encoding="iso-8859-1")
                writer = pd.ExcelWriter(
                    toDir + "\\" + file.replace("log", "xlsx"), engine="xlsxwriter")
                df.to_excel(writer, "Лист1")
                writer.save()
    except:
        print("")
    time.sleep(pause * 60)
