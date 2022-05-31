import pandas as pd

class NewPredictorController:

    def get_Columns(self):
        sizes = pd.read_csv('new_jeans_dataset.csv')
        waistCol = sizes['Waist']
        print(waistCol.tolist())
        return waistCol.tolist()

    def get_Size(type, waist, hips):
        match type:
            case 0:
                return "zero"
            case 1:
                return "one"
            case 2:
                return "two"
            case default:
                return "something"


