from os import scandir
from os import remove
import pandas as pd
import numpy as np
import datetime

# remove each of 6 files
def main():
    listOfFiles =[arch.name for arch in scandir("./data") if arch.is_file()]
    i = 0
    for file_name in sorted(listOfFiles):
        timestamp = datetime.datetime.fromtimestamp(int(file_name[11:21]))
        full_file = "./data/" + file_name
        i+=1
        if i%6 == 0:
            print("mantener " + full_file)
        else:
            print("borrar " + full_file)
            remove(full_file)

if __name__ == "__main__":
    main()