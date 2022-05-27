import json
from typing import Union

import numpy
from fastapi import FastAPI, status, APIRouter
from pydantic import BaseModel
from NewPredictorController import NewPredictorController
from pydiator_core.mediatr import pydiator
import numpy as np

app = FastAPI()
router = APIRouter()
import pandas as pd


class Size(BaseModel):
    type: int
    waist: int
    hips: int


@app.get("/", status_code=200)
def read_root():
    return {"Hello": "World"}


@app.get("/getColumns", status_code=200)
def get_columns():
    predictor = NewPredictorController()
    predictor.get_Columns()

@app.post("/newcalc", status_code=200)
def get_new_size(size: Size):
    match size.type:
        #For the new one
        case 0:
            df = pd.read_csv('new_jeans_dataset.csv')
            WaistCm = df['WaistCm'].to_numpy()
            HipsCm = df['HipsCm'].to_numpy()
            WaistIn = df['WaistIn'].to_numpy()
            HipsIn = df['HipsIn'].to_numpy()
            resultWaist = np.where(WaistCm == size.waist)
            resultHips = np.where(HipsCm == size.hips)
            print("The index is", resultWaist)
            print("The index is", resultWaist[0][0])
            if resultWaist[0][0] == resultHips[0][0]:
                print(df['NewJeans'][[resultWaist[0][0], resultHips[0][0]]])
                return "Estan en el mismo indice"
            else:
                return "Algo anda mal"
        case 1:
            return "one"
        case 2:
            return "two"
        case default:
            return "something"
