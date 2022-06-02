import pandas as pd


class NewPredictorController:

    def get_Columns(self):
        sizes = pd.read_csv('new_jeans_dataset.csv')
        waistCol = sizes['Waist']
        print(waistCol.tolist())
        return waistCol.tolist()

    def get_Size(type, waist, hips):
        if type == 0:
            return "zero"
        if type == 1:
            return "one"
        if type == 2:
            return "two"
        else:
            return "something"
