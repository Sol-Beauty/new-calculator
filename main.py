import json
from typing import Union

import numpy
from fastapi import FastAPI, status, APIRouter, HTTPException
from pydantic import BaseModel
from NewPredictorController import NewPredictorController
import numpy as np
from bottle import response
app = FastAPI()
router = APIRouter()
import pandas as pd


class Size(BaseModel):
    type: int
    waist: float
    hips: float


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
                raise HTTPException(status_code=400, detail="La talla no existe, favor de comunicarse con algún asesor")
                return False
        case 1:
            df = pd.read_csv('new_jeans_dataset.csv')
            WaistIn = df['WaistIn'].to_numpy()
            HipsIn = df['HipsIn'].to_numpy()
            indexesWaistIn = np.where(WaistIn == size.waist)
            print(size.waist)
            print(size.hips)
            print("Indexes WaistIn", indexesWaistIn)
            indexIn = indexesWaistIn[0]
            resultHips = HipsIn[indexIn]
            print("WaistIn", WaistIn)
            print("HipsIn", HipsIn)
            if resultHips == size.hips:
                jeans = df['NewJeans'].to_numpy()
                sizeFinal = jeans[indexIn]
                print(sizeFinal)
                return sizeFinal
            else:
                raise HTTPException(status_code=400, detail="La talla no existe, favor de comunicarse con algún asesor")
                return False
        case default:
            raise HTTPException(status_code=404, detail="No hay o existe una opcion por favor elija una para continuar")