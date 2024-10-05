import pandas as pd
import datetime
dfnow = pd.DataFrame({
    "日時":"2014/03/14",
    "主食":"a",
    "主菜":"b",
    "副菜":"c",
    "カロリー":"d"
    },index=[0])
print(dfnow)
datenow = datetime.datetime.now()
date = "{}/{}/{}".format(datenow.year,datenow.month,datenow.day)
print(date)