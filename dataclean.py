from os import scandir
import pandas as pd
import datetime
import re
import os

datafilespath='./data'

def main():
    listOfFiles =[arch.name for arch
                  in scandir(datafilespath) if arch.is_file()]

    all_stations = pd.DataFrame()

    for file_name in sorted(listOfFiles):
        pattern = re.compile("^(malagabici\-)[0-9]+\.csv$")
        if pattern.match(file_name) and os.path.getsize(datafilespath+"/"+file_name) >0:
            timestamp = datetime.datetime.fromtimestamp(int(file_name[11:21]))
            weekday = 'WD'
            if timestamp.weekday() == 5:
                weekday = 'SA'
            elif timestamp.weekday() == 6:
                weekday = 'SH'
            print(timestamp)
            dockings_historic = pd.read_csv(datafilespath+"/"+file_name,index_col=1,delimiter=',', encoding='utf-8')
            dockings_historic["TIPO_DIA"] = weekday
            dockings_historic["TIMESTAMP"] = timestamp.strftime("%Y-%m-%d %H:%M:%S")
            print(dockings_historic["TIMESTAMP"])
            hours = timestamp.hour
            minutes = "30"
            if timestamp.minute > 45:
                hours = timestamp.hour +1
                minutes = "00"
            elif timestamp.minute <= 15:
                minutes = "00"
            myroundtime = '{:02d}'.format(hours) +":"+ minutes
            dockings_historic["HORA"] = myroundtime
            all_stations = pd.concat([all_stations,dockings_historic])

    all_stations["OCUPACION"] = list(map(lambda o,l: o/(o+l),all_stations["NUM_OCUPADOS"],all_stations["NUM_LIBRES"] ))
    all_stations.to_csv(datafilespath + "/allstationsalltime.csv",encoding='utf-8')


if __name__ == "__main__":
    main()
