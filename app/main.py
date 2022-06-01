from fastapi import FastAPI, APIRouter, HTTPException
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware

from app.NewPredictorController import NewPredictorController
import numpy as np
import pandas as pd

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
def get_new_size(size: Size):
    if size.type == 0:
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
            return sizeFinal
        else:
            raise HTTPException(status_code=400, detail="La talla no existe, favor de comunicarse con algún asesor")
    if size.type == 1:
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
            return sizeFinal
        else:
            raise HTTPException(status_code=400, detail="La talla no existe, favor de comunicarse con algún asesor")
    else:
        raise HTTPException(status_code=404, detail="No hay o existe una opcion por favor elija una para continuar")
