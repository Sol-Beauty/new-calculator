import json

from fastapi import FastAPI, status, APIRouter, HTTPException
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware

from app.NewPredictorController import NewPredictorController
import numpy as np

app = FastAPI(
    title="FastAPI Pydiator",
    description="FastAPI pydiator integration project",
    version="1.0.0",
    # root_path="/predictor",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
router = APIRouter()
import pandas as pd


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
def get_new_size(size: Size):
    if size.type == 0:

        if size.measure_type == "cm":

            df = pd.read_csv('/app/new_jeans_dataset.csv')
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
                return json.dumps(sizeFinal)
            else:
                raise HTTPException(status_code=400,
                                    detail="La talla no existe, favor de comunicarse con algún asesor")

        if size.measure_type == "in":
            df = pd.read_csv('/app/new_jeans_dataset.csv')
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
                result = sizeFinal.tolist()
                print(result)
                print(type(result))
                return result
            else:
                raise HTTPException(status_code=400, detail="La talla no existe, favor de comunicarse con algún "
                                                            "asesor")
    if size.type == 1:

        if size.measure_type == "cm":
            df = pd.read_csv('/app/new_jeans_dataset.csv')
            WaistCm = df['WaistCm'].to_numpy()
            HipsCm = df['HipsCm'].to_numpy()
            indexesWaist = np.where(WaistCm == size.waist)
            index = indexesWaist[0][0]
            resultHips = HipsCm[index]
            print(resultHips)
            if resultHips == size.hips:
                jeans = df['JeansSBC'].to_numpy()
                sizeFinal = jeans[index]
                print(sizeFinal)
                return json.dumps({sizeFinal})
            else:
                raise HTTPException(status_code=400,
                                    detail="La talla no existe, favor de comunicarse con algún asesor")

        if size.measure_type == "in":
            df = pd.read_csv('new_jeans_dataset.csv')
            WaistIn = df['WaistIn'].to_numpy()
            HipsIn = df['HipsIn'].to_numpy()
            indexesWaistIn = np.where(WaistIn == size.waist)
            print(size.waist)
            print(size.hips)
            print("Indexes WaistIn", indexesWaistIn)
            indexIn = indexesWaistIn[0]
            resultHips = HipsIn[indexIn]
            if resultHips == size.hips:
                jeans = df['JeansSBC'].to_numpy()
                sizeFinal = jeans[indexIn]
                print(sizeFinal)
                result = sizeFinal.tolist()
                print(result)
                print(type(result))
                return result
            else:
                raise HTTPException(status_code=400, detail="La talla no existe, favor de comunicarse con algún "
                                                            "asesor")
    else:
            raise HTTPException(status_code=404, detail="No hay o existe una opcion por favor elija una para continuar")

