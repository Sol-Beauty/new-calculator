import numpy
import pandas as pd
import numpy as np

data = pd.read_csv("new_jeans_dataset.csv")

data.columns = ["Model", "beforeSize", "currentSize", "Waist", "Hips", "Leg", "Shape", "Other", "Time", "Notes"]

rawWaist = data[['Waist']].to_numpy()
rawHips = data[['Hips']].to_numpy()
reqWaist = input("Introduce la cintura")

if reqWaist == data._ixs(4) | 0:
    print("AHUEVO SE ENCONTRO")
else:
    print("Nelson mandela")
