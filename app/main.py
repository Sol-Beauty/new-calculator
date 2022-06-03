import json

from fastapi import FastAPI, status, APIRouter, HTTPException

from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware
import pandas as pd
from app.NewPredictorController import NewPredictorController
import numpy as np

app = FastAPI(
    title="FastAPI Pydiator",
    description="FastAPI pydiator integration project",
    version="1.0.0",
    root_path="/calculator",

)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
router = APIRouter()


class Size(BaseModel):
    type: int
    waist: float
    hips: float
    measure_type: str


@app.get("/", status_code=200)
def read_root():
    return {"Hello": "World"}


@app.get("/v2/getColumns", status_code=200)
def get_columns():
    predictor = NewPredictorController()
    predictor.get_Columns()


@app.post("/v2/newcalc", status_code=200)
def get_new_size(sizetype: Size):
    if sizetype.type == 0:
        if sizetype.measure_type == "cm":
            df = pd.read_csv('app/new_jeans_dataset.csv')
            WaistCm = df['WaistCm'].to_numpy()
            HipsCm = df['HipsCm'].to_numpy()
            indexesWaist = np.where(WaistCm == sizetype.waist)
            index = indexesWaist[0][0]
            resultHips = HipsCm[index]
            print(resultHips)
            if resultHips == sizetype.hips:
                jeans = df['NewJeans'].to_numpy()
                size = jeans[index]
                return {"size": size}
            else:
                raise HTTPException(status_code=400,
                                    detail="La talla no existe, favor de comunicarse con algún asesor")

        if sizetype.measure_type == "in":
            df = pd.read_csv('app/new_jeans_dataset.csv')
            WaistIn = df['WaistIn'].to_numpy()
            HipsIn = df['HipsIn'].to_numpy()
            indexesWaistIn = np.where(WaistIn == sizetype.waist)
            print(sizetype.waist)
            print(sizetype.hips)
            print("Indexes WaistIn", indexesWaistIn)
            indexIn = indexesWaistIn[0][0]
            resultHips = HipsIn[indexIn]
            print("WaistIn", WaistIn)
            print("HipsIn", HipsIn)
            if resultHips == sizetype.hips:
                jeans = df['NewJeans'].to_numpy()
                size = jeans[indexIn]
                return {"size": size}
            else:
                raise HTTPException(status_code=400, detail="La talla no existe, favor de comunicarse con algún "
                                                            "asesor")
    if sizetype.type == 1:

        if sizetype.measure_type == "cm":
            df = pd.read_csv('app/new_jeans_dataset.csv')
            WaistCm = df['WaistCm'].to_numpy()
            HipsCm = df['HipsCm'].to_numpy()
            indexesWaist = np.where(WaistCm == sizetype.waist)
            index = indexesWaist[0][0]
            resultHips = HipsCm[index]
            print(resultHips)
            if resultHips == sizetype.hips:
                jeans = df['JeansSBC'].to_numpy()
                size = jeans[index]
                return {"size": size}
            else:
                raise HTTPException(status_code=400,
                                    detail="La talla no existe, favor de comunicarse con algún asesor")

        if sizetype.measure_type == "in":
            df = pd.read_csv('app/new_jeans_dataset.csv')
            WaistIn = df['WaistIn'].to_numpy()
            HipsIn = df['HipsIn'].to_numpy()
            indexesWaistIn = np.where(WaistIn == sizetype.waist)
            print(sizetype.waist)
            print(sizetype.hips)
            print("Indexes WaistIn", indexesWaistIn)
            indexIn = indexesWaistIn[0][0]
            resultHips = HipsIn[indexIn]
            if resultHips == sizetype.hips:
                jeans = df['JeansSBC'].to_numpy()
                size = jeans[indexIn]
                return {"size": size}
            else:
                raise HTTPException(status_code=400, detail="La talla no existe, favor de comunicarse con algún "
                                                            "asesor")
    else:
        raise HTTPException(status_code=404, detail="No hay o existe una opcion por favor elija una para continuar")
