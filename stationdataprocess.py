from os import scandir
import pandas as pd
import numpy as np
import datetime
import sys
from time import strptime

import re

def roundtooclockorhalf (times):
    myhours = list( map(lambda  x: int(x[0:2]), times))
    myminutes = list(map(lambda  x: int(x[3:5]),times))
    myroundhours = list(map(lambda h,m: h+1 if m > 45 else h, myhours,myminutes))
    myroundminutes = list(map(lambda x: 30 if x > 15 and x < 45 else 0, myminutes))
    myroundtime = list(map(lambda h,m : '{:02d}'.format(h) + ":"+ '{:02d}'.format(m),myroundhours, myroundminutes))
    return myroundtime

def main():
    listOfFiles =[arch.name for arch
                  in scandir("./stations") if arch.is_file()]

    all_stations = {}

    for file_name in sorted(listOfFiles):
        station_name = file_name[:-4]
        print(station_name)
        all_stations[station_name] = pd.read_csv("./stations/"+file_name.encode(sys.getfilesystemencoding()).decode(),delimiter=',',index_col=8)
        times = all_stations[station_name]["HORA"].tolist()
        myroundtime = roundtooclockorhalf(times)
        all_stations[station_name].drop("HORA",1)
        all_stations[station_name]["HORA"] = myroundtime
        all_stations[station_name]["OCUPACION"] = list(map(lambda o,l: o/(o+l),all_stations[station_name]['NUM_OCUPADOS'],all_stations[station_name]['NUM_LIBRES'] ))
        print(all_stations[station_name]["OCUPACION"])
        all_stations[station_name].to_csv("./stations/processed_"+file_name)






if __name__ == "__main__":
    main()
