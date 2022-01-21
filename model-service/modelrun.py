import random
import pathlib
import os

DEBUG_MODE = True
if not DEBUG_MODE:
    from Predictor import Predictor

def get_random_files_as_json(amount: int = 5):
    filePaths = {}
    filesInDir = os.listdir('../data/valid')
    for x in range(0, amount):
        newFile = pathlib.Path(random.choice(filesInDir)).resolve()
        while newFile in filePaths:
            newFile = pathlib.Path(random.choice(filesInDir)).resolve()
        filePaths[x] = {'path': newFile}
    return {'validFiles': filePaths}


def predict(path: str, test: bool = DEBUG_MODE) -> dict:
    if not os.path.exists(path) or test:
        return DEBUG_MAP
    else:
        return Predictor().predict(path)


DEBUG_MAP = {
       "results": {
           "0": {
               "species": "Robin",
               "confidence": ".88"
            },
           "1": {
               "species": "eagle",
               "confidence": ".11"
            },
           "2": {
               "species": "Birb",
               "confidence": ".11"
            },
       }
    }
