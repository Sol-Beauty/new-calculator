import json
from typing import Union

from fastapi import FastAPI, status, APIRouter
from pydantic import BaseModel
from NewPredictorController import NewPredictorController
from pydiator_core.mediatr import pydiator

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


@app.post("/calculate", status_code=200)
def get_size(size: Size):
    match size.type:
        case 0:
            df = pd.read_csv('new_jeans_dataset.csv')
            print(df.loc[0]['Waist'])
            if df.loc[0]['Waist'] == size.waist and df.loc[0]['Hips'] == size.hips:
                return "Tu talla es 4/14"
            if df.loc[1]['Waist'] == size.waist and df.loc[1]['Hips'] == size.hips:
                return "Tu talla es 2/12"
            if df.loc[2]['Waist'] == size.waist and df.loc[2]['Hips'] == size.hips:
                return "Tu talla es 4/12"
            if df.loc[3]['Waist'] == size.waist and df.loc[3]['Hips'] == size.hips:
                return "Tu talla es 4/10"
            if df.loc[4]['Waist'] == size.waist and df.loc[4]['Hips'] == size.hips:
                return "Tu talla es 6/14"
            if df.loc[5]['Waist'] == size.waist and df.loc[5]['Hips'] == size.hips:
                return "Tu talla es 2/10"
            if df.loc[6]['Waist'] == size.waist and df.loc[6]['Hips'] == size.hips:
                return "Tu talla es 0/8"
            if df.loc[7]['Waist'] == size.waist and df.loc[7]['Hips'] == size.hips:
                return "Tu talla es 4/12"
            if df.loc[8]['Waist'] == size.waist and df.loc[8]['Hips'] == size.hips:
                return "Tu talla es 8/14"
            if df.loc[9]['Waist'] == size.waist and df.loc[9]['Hips'] == size.hips:
                return "Tu talla es 12/18"
            if df.loc[10]['Waist'] == size.waist and df.loc[10]['Hips'] == size.hips:
                return "Tu talla es 2/8"
            if df.loc[11]['Waist'] == size.waist and df.loc[11]['Hips'] == size.hips:
                return "Tu talla es 6/14"
            if df.loc[12]['Waist'] == size.waist and df.loc[12]['Hips'] == size.hips:
                return "Tu talla es 12/18"
            if df.loc[13]['Waist'] == size.waist and df.loc[13]['Hips'] == size.hips:
                return "Tu talla es 0/10"
            if df.loc[14]['Waist'] == size.waist and df.loc[14]['Hips'] == size.hips:
                return "Tu talla es 8/14"
            if df.loc[15]['Waist'] == size.waist and df.loc[15]['Hips'] == size.hips:
                return "Tu talla es 2/8"
            if df.loc[16]['Waist'] == size.waist and df.loc[16]['Hips'] == size.hips:
                return "Tu talla es 2/12"
            if df.loc[17]['Waist'] == size.waist and df.loc[17]['Hips'] == size.hips:
                return "Tu talla es 4/14"
            if df.loc[18]['Waist'] == size.waist and df.loc[18]['Hips'] == size.hips:
                return "Tu talla es 2/12"
            if df.loc[19]['Waist'] == size.waist and df.loc[19]['Hips'] == size.hips:
                return "Tu talla es 4/14"
            if df.loc[20]['Waist'] == size.waist and df.loc[20]['Hips'] == size.hips:
                return "Tu talla es 2/12"
            if df.loc[21]['Waist'] == size.waist and df.loc[21]['Hips'] == size.hips:
                return "Tu talla es 2/12"
            if df.loc[22]['Waist'] == size.waist and df.loc[22]['Hips'] == size.hips:
                return "Tu talla es 4/14"
            if df.loc[23]['Waist'] == size.waist and df.loc[23]['Hips'] == size.hips:
                return "Tu talla es 8/14"
            if df.loc[24]['Waist'] == size.waist and df.loc[24]['Hips'] == size.hips:
                return "Tu talla es 2/8"
            if df.loc[25]['Waist'] == size.waist and df.loc[25]['Hips'] == size.hips:
                return "Tu talla es 4/14"
            if df.loc[26]['Waist'] == size.waist and df.loc[26]['Hips'] == size.hips:
                return "Tu talla es 8/14"
            if df.loc[27]['Waist'] == size.waist and df.loc[27]['Hips'] == size.hips:
                return "Tu talla es 2/8"
            if df.loc[28]['Waist'] == size.waist and df.loc[28]['Hips'] == size.hips:
                return "Tu talla es 8/14"
            if df.loc[29]['Waist'] == size.waist and df.loc[29]['Hips'] == size.hips:
                return "Tu talla es 2/8"
            if df.loc[30]['Waist'] == size.waist and df.loc[30]['Hips'] == size.hips:
                return "Tu talla es 2/10"
            if df.loc[31]['Waist'] == size.waist and df.loc[31]['Hips'] == size.hips:
                return "Tu talla es 4/10"
            if df.loc[32]['Waist'] == size.waist and df.loc[32]['Hips'] == size.hips:
                return "Tu talla es 12/16"
            if df.loc[33]['Waist'] == size.waist and df.loc[33]['Hips'] == size.hips:
                return "Tu talla es 4/12"
            if df.loc[34]['Waist'] == size.waist and df.loc[34]['Hips'] == size.hips:
                return "Tu talla es 4/10"
            if df.loc[35]['Waist'] == size.waist and df.loc[35]['Hips'] == size.hips:
                return "Tu talla es 8/14"
            if df.loc[36]['Waist'] == size.waist and df.loc[36]['Hips'] == size.hips:
                return "Tu talla es 10/10"
            if df.loc[37]['Waist'] == size.waist and df.loc[37]['Hips'] == size.hips:
                return "Tu talla es 4/10"
            if df.loc[38]['Waist'] == size.waist and df.loc[38]['Hips'] == size.hips:
                return "Tu talla es 12/16"
            if df.loc[39]['Waist'] == size.waist and df.loc[39]['Hips'] == size.hips:
                return "Tu talla es 4/10"
            if df.loc[40]['Waist'] == size.waist and df.loc[40]['Hips'] == size.hips:
                return "Tu talla es 0/8"
            if df.loc[41]['Waist'] == size.waist and df.loc[41]['Hips'] == size.hips:
                return "Tu talla es 2/12"
            if df.loc[42]['Waist'] == size.waist and df.loc[42]['Hips'] == size.hips:
                return "Tu talla es 4/12"
            if df.loc[43]['Waist'] == size.waist and df.loc[43]['Hips'] == size.hips:
                return "Tu talla es 4/12"
            if df.loc[44]['Waist'] == size.waist and df.loc[44]['Hips'] == size.hips:
                return "Tu talla es 2/12"
            if df.loc[45]['Waist'] == size.waist and df.loc[45]['Hips'] == size.hips:
                return "Tu talla es 4/12"
            if df.loc[46]['Waist'] == size.waist and df.loc[46]['Hips'] == size.hips:
                return "Tu talla es 4/10"
            if df.loc[47]['Waist'] == size.waist and df.loc[47]['Hips'] == size.hips:
                return "Tu talla es 6/14"
            if df.loc[48]['Waist'] == size.waist and df.loc[48]['Hips'] == size.hips:
                return "Tu talla es 2/10"
            if df.loc[49]['Waist'] == size.waist and df.loc[49]['Hips'] == size.hips:
                return "Tu talla es 0/8"
            if df.loc[50]['Waist'] == size.waist and df.loc[50]['Hips'] == size.hips:
                return "Tu talla es 4/12"
            if df.loc[51]['Waist'] == size.waist and df.loc[51]['Hips'] == size.hips:
                return "Tu talla es 8/14"
            if df.loc[52]['Waist'] == size.waist and df.loc[52]['Hips'] == size.hips:
                return "Tu talla es 12/18"
            if df.loc[53]['Waist'] == size.waist and df.loc[53]['Hips'] == size.hips:
                return "Tu talla es 6/14"
            if df.loc[54]['Waist'] == size.waist and df.loc[54]['Hips'] == size.hips:
                return "Tu talla es 6/14"
            if df.loc[55]['Waist'] == size.waist and df.loc[55]['Hips'] == size.hips:
                return "Tu talla es 12/18"
            if df.loc[56]['Waist'] == size.waist and df.loc[56]['Hips'] == size.hips:
                return "Tu talla es 0/10"
            if df.loc[57]['Waist'] == size.waist and df.loc[57]['Hips'] == size.hips:
                return "Tu talla es 8/14"
            if df.loc[58]['Waist'] == size.waist and df.loc[58]['Hips'] == size.hips:
                return "Tu talla es 2/8"
            if df.loc[59]['Waist'] == size.waist and df.loc[59]['Hips'] == size.hips:
                return "Tu talla es 2/12"
            if df.loc[60]['Waist'] == size.waist and df.loc[60]['Hips'] == size.hips:
                return "Tu talla es 4/14"
            if df.loc[61]['Waist'] == size.waist and df.loc[61]['Hips'] == size.hips:
                return "Tu talla es 2/12"
            if df.loc[62]['Waist'] == size.waist and df.loc[62]['Hips'] == size.hips:
                return "Tu talla es 4/14"
            if df.loc[63]['Waist'] == size.waist and df.loc[63]['Hips'] == size.hips:
                return "Tu talla es 2/12"
            if df.loc[64]['Waist'] == size.waist and df.loc[64]['Hips'] == size.hips:
                return "Tu talla es 2/8"
            if df.loc[65]['Waist'] == size.waist and df.loc[65]['Hips'] == size.hips:
                return "Tu talla es 4/14"
            if df.loc[66]['Waist'] == size.waist and df.loc[66]['Hips'] == size.hips:
                return "Tu talla es 8/14"
            if df.loc[67]['Waist'] == size.waist and df.loc[67]['Hips'] == size.hips:
                return "Tu talla es 2/8"
            if df.loc[68]['Waist'] == size.waist and df.loc[68]['Hips'] == size.hips:
                return "Tu talla es 8/14"
            if df.loc[69]['Waist'] == size.waist and df.loc[69]['Hips'] == size.hips:
                return "Tu talla es 2/8"
            if df.loc[70]['Waist'] == size.waist and df.loc[70]['Hips'] == size.hips:
                return "Tu talla es 2/10"
            if df.loc[71]['Waist'] == size.waist and df.loc[71]['Hips'] == size.hips:
                return "Tu talla es 4/10"
            if df.loc[72]['Waist'] == size.waist and df.loc[72]['Hips'] == size.hips:
                return "Tu talla es 12/16"
            if df.loc[73]['Waist'] == size.waist and df.loc[73]['Hips'] == size.hips:
                return "Tu talla es 4/12"
            if df.loc[74]['Waist'] == size.waist and df.loc[74]['Hips'] == size.hips:
                return "Tu talla es 4/10"
            if df.loc[75]['Waist'] == size.waist and df.loc[75]['Hips'] == size.hips:
                return "Tu talla es 8/14"
            if df.loc[76]['Waist'] == size.waist and df.loc[76]['Hips'] == size.hips:
                return "Tu talla es 10/16"
            if df.loc[77]['Waist'] == size.waist and df.loc[77]['Hips'] == size.hips:
                return "Tu talla es 4/10"
            if df.loc[78]['Waist'] == size.waist and df.loc[78]['Hips'] == size.hips:
                return "Tu talla es 12/16"
            if df.loc[79]['Waist'] == size.waist and df.loc[79]['Hips'] == size.hips:
                return "Tu talla es 4/10"
            if df.loc[80]['Waist'] == size.waist and df.loc[80]['Hips'] == size.hips:
                return "Tu talla es 0/8"
            if df.loc[81]['Waist'] == size.waist and df.loc[81]['Hips'] == size.hips:
                return "Tu talla es 2/12"
            if df.loc[82]['Waist'] == size.waist and df.loc[82]['Hips'] == size.hips:
                return "Tu talla es 4/12"
            if df.loc[83]['Waist'] == size.waist and df.loc[83]['Hips'] == size.hips:
                return "Tu talla es 4/14"
            if df.loc[84]['Waist'] == size.waist and df.loc[84]['Hips'] == size.hips:
                return "Tu talla es 2/12"
            if df.loc[85]['Waist'] == size.waist and df.loc[85]['Hips'] == size.hips:
                return "Tu talla es 6/14"
            if df.loc[86]['Waist'] == size.waist and df.loc[86]['Hips'] == size.hips:
                return "Tu talla es 2/10"
            if df.loc[87]['Waist'] == size.waist and df.loc[87]['Hips'] == size.hips:
                return "Tu talla es 0/8"
            if df.loc[88]['Waist'] == size.waist and df.loc[88]['Hips'] == size.hips:
                return "Tu talla es 4/12"
            if df.loc[89]['Waist'] == size.waist and df.loc[89]['Hips'] == size.hips:
                return "Tu talla es 8/14"
            if df.loc[90]['Waist'] == size.waist and df.loc[90]['Hips'] == size.hips:
                return "Tu talla es 12/18"
            if df.loc[91]['Waist'] == size.waist and df.loc[91]['Hips'] == size.hips:
                return "Tu talla es 2/8"
            if df.loc[92]['Waist'] == size.waist and df.loc[92]['Hips'] == size.hips:
                return "Tu talla es 6/14"
            if df.loc[93]['Waist'] == size.waist and df.loc[93]['Hips'] == size.hips:
                return "Tu talla es 6/14"
            if df.loc[94]['Waist'] == size.waist and df.loc[94]['Hips'] == size.hips:
                return "Tu talla es 0/10"
            if df.loc[95]['Waist'] == size.waist and df.loc[95]['Hips'] == size.hips:
                return "Tu talla es 8/14"
            if df.loc[96]['Waist'] == size.waist and df.loc[96]['Hips'] == size.hips:
                return "Tu talla es 2/8"
            if df.loc[97]['Waist'] == size.waist and df.loc[97]['Hips'] == size.hips:
                return "Tu talla es 8/14"
            if df.loc[98]['Waist'] == size.waist and df.loc[98]['Hips'] == size.hips:
                return "Tu talla es 2/18"
            if df.loc[99]['Waist'] == size.waist and df.loc[99]['Hips'] == size.hips:
                return "Tu talla es 2/12"
            if df.loc[100]['Waist'] == size.waist and df.loc[100]['Hips'] == size.hips:
                return "Tu talla es 4/14"
            if df.loc[101]['Waist'] == size.waist and df.loc[101]['Hips'] == size.hips:
                return "Tu talla es 2/12"
            if df.loc[102]['Waist'] == size.waist and df.loc[102]['Hips'] == size.hips:
                return "Tu talla es 4/14"
            if df.loc[103]['Waist'] == size.waist and df.loc[103]['Hips'] == size.hips:
                return "Tu talla es 2/12"
            if df.loc[104]['Waist'] == size.waist and df.loc[104]['Hips'] == size.hips:
                return "Tu talla es 2/8"
            if df.loc[105]['Waist'] == size.waist and df.loc[105]['Hips'] == size.hips:
                return "Tu talla es 4/14"
            if df.loc[106]['Waist'] == size.waist and df.loc[106]['Hips'] == size.hips:
                return "Tu talla es 8/14"
            if df.loc[107]['Waist'] == size.waist and df.loc[107]['Hips'] == size.hips:
                return "Tu talla es 2/8"
            if df.loc[108]['Waist'] == size.waist and df.loc[108]['Hips'] == size.hips:
                return "Tu talla es 8/14"
            if df.loc[109]['Waist'] == size.waist and df.loc[109]['Hips'] == size.hips:
                return "Tu talla es 2/8"
            if df.loc[110]['Waist'] == size.waist and df.loc[110]['Hips'] == size.hips:
                return "Tu talla es 2/10"
            if df.loc[111]['Waist'] == size.waist and df.loc[111]['Hips'] == size.hips:
                return "Tu talla es 4/10"
            if df.loc[112]['Waist'] == size.waist and df.loc[112]['Hips'] == size.hips:
                return "Tu talla es 12/16"
            if df.loc[113]['Waist'] == size.waist and df.loc[113]['Hips'] == size.hips:
                return "Tu talla es 4/12"
            if df.loc[114]['Waist'] == size.waist and df.loc[114]['Hips'] == size.hips:
                return "Tu talla es 4/10"
            if df.loc[115]['Waist'] == size.waist and df.loc[115]['Hips'] == size.hips:
                return "Tu talla es 8/14"
            if df.loc[116]['Waist'] == size.waist and df.loc[116]['Hips'] == size.hips:
                return "Tu talla es 10/16"
            if df.loc[117]['Waist'] == size.waist and df.loc[117]['Hips'] == size.hips:
                return "Tu talla es 4/10"
            if df.loc[118]['Waist'] == size.waist and df.loc[118]['Hips'] == size.hips:
                return "Tu talla es 0/8"
            if df.loc[119]['Waist'] == size.waist and df.loc[119]['Hips'] == size.hips:
                return "Tu talla es 2/12"
            if df.loc[120]['Waist'] == size.waist and df.loc[120]['Hips'] == size.hips:
                return "Tu talla es 4/12"
            if df.loc[121]['Waist'] == size.waist and df.loc[121]['Hips'] == size.hips:
                return "Tu talla es 4/14"
            if df.loc[122]['Waist'] == size.waist and df.loc[222]['Hips'] == size.hips:
                return "Tu talla es 4/14"
            if df.loc[123]['Waist'] == size.waist and df.loc[123]['Hips'] == size.hips:
                return "Tu talla es 4/12"
            if df.loc[124]['Waist'] == size.waist and df.loc[124]['Hips'] == size.hips:
                return "Tu talla es 6/14"
            if df.loc[125]['Waist'] == size.waist and df.loc[125]['Hips'] == size.hips:
                return "Tu talla es 2/10"
            if df.loc[126]['Waist'] == size.waist and df.loc[126]['Hips'] == size.hips:
                return "Tu talla es 0/8"
            if df.loc[127]['Waist'] == size.waist and df.loc[127]['Hips'] == size.hips:
                return "Tu talla es 6/14"
            if df.loc[128]['Waist'] == size.waist and df.loc[128]['Hips'] == size.hips:
                return "Tu talla es 2/10"
            if df.loc[129]['Waist'] == size.waist and df.loc[129]['Hips'] == size.hips:
                return "Tu talla es 12/18"
            if df.loc[130]['Waist'] == size.waist and df.loc[130]['Hips'] == size.hips:
                return "Tu talla es 2/8"
            if df.loc[131]['Waist'] == size.waist and df.loc[131]['Hips'] == size.hips:
                return "Tu talla es 6/14"
            if df.loc[132]['Waist'] == size.waist and df.loc[132]['Hips'] == size.hips:
                return "Tu talla es 12/18"
            if df.loc[133]['Waist'] == size.waist and df.loc[133]['Hips'] == size.hips:
                return "Tu talla es 2/8"
            if df.loc[134]['Waist'] == size.waist and df.loc[134]['Hips'] == size.hips:
                return "Tu talla es 6/14"
            if df.loc[135]['Waist'] == size.waist and df.loc[135]['Hips'] == size.hips:
                return "Tu talla es 12/18"
            if df.loc[136]['Waist'] == size.waist and df.loc[136]['Hips'] == size.hips:
                return "Tu talla es 0/10"
            if df.loc[137]['Waist'] == size.waist and df.loc[137]['Hips'] == size.hips:
                return "Tu talla es 8/14"
            if df.loc[138]['Waist'] == size.waist and df.loc[138]['Hips'] == size.hips:
                return "Tu talla es 2/8"
            if df.loc[139]['Waist'] == size.waist and df.loc[139]['Hips'] == size.hips:
                return "Tu talla es 2/12"
            if df.loc[140]['Waist'] == size.waist and df.loc[140]['Hips'] == size.hips:
                return "Tu talla es 4/14"
            if df.loc[141]['Waist'] == size.waist and df.loc[141]['Hips'] == size.hips:
                return "Tu talla es 2/12"
            if df.loc[142]['Waist'] == size.waist and df.loc[142]['Hips'] == size.hips:
                return "Tu talla es 2/8"
            if df.loc[143]['Waist'] == size.waist and df.loc[143]['Hips'] == size.hips:
                return "Tu talla es 4/14"
            if df.loc[144]['Waist'] == size.waist and df.loc[144]['Hips'] == size.hips:
                return "Tu talla es 8/14"
            if df.loc[145]['Waist'] == size.waist and df.loc[145]['Hips'] == size.hips:
                return "Tu talla es 2/8"
            if df.loc[146]['Waist'] == size.waist and df.loc[146]['Hips'] == size.hips:
                return "Tu talla es 8/14"
            if df.loc[147]['Waist'] == size.waist and df.loc[147]['Hips'] == size.hips:
                return "Tu talla es 2/8"
            if df.loc[148]['Waist'] == size.waist and df.loc[148]['Hips'] == size.hips:
                return "Tu talla es 2/10"
            if df.loc[149]['Waist'] == size.waist and df.loc[149]['Hips'] == size.hips:
                return "Tu talla es 2/10"
            if df.loc[150]['Waist'] == size.waist and df.loc[1350]['Hips'] == size.hips:
                return "Tu talla es 2/8"
            if df.loc[151]['Waist'] == size.waist and df.loc[151]['Hips'] == size.hips:
                return "Tu talla es 4/12"
            if df.loc[152]['Waist'] == size.waist and df.loc[152]['Hips'] == size.hips:
                return "Tu talla es 4/10"
            if df.loc[153]['Waist'] == size.waist and df.loc[153]['Hips'] == size.hips:
                return "Tu talla es 8/14"
            if df.loc[154]['Waist'] == size.waist and df.loc[154]['Hips'] == size.hips:
                return "Tu talla es 10/16"
            if df.loc[155]['Waist'] == size.waist and df.loc[155]['Hips'] == size.hips:
                return "Tu talla es 4/10"
            if df.loc[156]['Waist'] == size.waist and df.loc[156]['Hips'] == size.hips:
                return "Tu talla es 12/16"
            else:
                return "Algo anda mal"
        case 1:
            return "one"
        case default:
            return "something"


@app.post("/newcalc", status_code=200)
def get_new_size(size: Size):
    match size.type:
        case 0:
            df = pd.read_csv('new_jeans_dataset.csv')

            print(df.iloc[0,2])
        case 1:
            return "one"
        case 2:
            return "two"
        case default:
            return "something"
