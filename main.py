import json
from typing import Union

import numpy
from fastapi import FastAPI, status, APIRouter
from pydantic import BaseModel
from NewPredictorController import NewPredictorController
from pydiator_core.mediatr import pydiator
import numpy as np
from bottle import response
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
            indexesWaist = np.where(WaistCm == size.waist)
            index = indexesWaist[0][0]
            resultHips = HipsCm[index]
            print(resultHips)
            if resultHips == size.hips:
                jeans = df['NewJeans'].to_numpy()
                sizeFinal = jeans[index]
                print(sizeFinal)
                return sizeFinal
            else:
                print("ALGO SALIO MAL")
                return False
        case 1:
            return "one"
        case 2:
            return "two"
        case default:
            return "something"