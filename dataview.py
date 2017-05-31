from os import scandir
import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
from matplotlib import style
import re

def main():

    listOfFiles =[arch.name for arch in scandir("./data/few/stations") if arch.is_file()]

    all_stations = {}

    for file_name in sorted(listOfFiles):
        station_name = file_name[:-4]
        print(station_name)
        all_stations[station_name] = pd.read_csv("./data/few/stations/"+file_name,delimiter=',',index_col=8)

        style.use('fivethirtyeight')
        all_stations[station_name]["NUM_OCUPADOS"][0:11].plot()
        all_stations[station_name]["NUM_OCUPADOS"][12:24].plot()

        plt.legend()
        plt.show()

if __name__ == "__main__":
    main()