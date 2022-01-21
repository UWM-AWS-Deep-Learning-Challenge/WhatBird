import os
from os import path

from fastapi import FastAPI
from fastapi.exceptions import HTTPException
import random
import pathlib

# from Predictor import *

DEBUG_MODE = True
if not DEBUG_MODE:
    from Predictor import Predictor

    p = Predictor()

DEBUG_MAP = {
    "results": {
        "0": {
            "species": "Robin",
            "confidence": ".88",
            "filePath": "../data/valid/ROBIN/1.jpg"
        },
        "1": {
            "species": "Emu",
            "confidence": ".11",
            "filePath": "../data/valid/EMU/1.jpg"
        },
        "2": {
            "species": "Frigate",
            "confidence": ".11",
            "filePath": "../data/valid/FRIGATE/1.jpg"
        },
    }
}

app = FastAPI()


# TODO pass in model
# p = Predictor()


def get_random_file():
    # birb_dir = random.choice(os.listdir('../data/valid/'))
    # return birb_dir
    # return pathlib.Path(birb_dir).parent.resolve()  # .parent.resolve() for abs path
    # return os.path.join(os.sep, '../data/valid/', birb_dir + '/1.jpg')

    birb_dir = '../data/valid/'
    n = '/' + str(random.randint(1, 5)) + '.jpg'
    return os.path.join(os.sep, birb_dir, random.choice(os.listdir(birb_dir)) + n)


##############################################################
# production endpoints
##############################################################

# TODO
@app.post('/production/predict')
async def production_predict(fileToPredict):
    if not path.exists(fileToPredict):
        raise HTTPException(status_code=503, detail='file does not exist')

    if DEBUG_MODE:
        return DEBUG_MAP
    else:
        return p.predict(fileToPredict)


# TODO
@app.post('/production/get_valid_files')
async def production_get_valid_files(numberOfFiles: int):
    files = {}
    for i in range(numberOfFiles):
        files.update(
            {
                i: {
                    'path': get_random_file()
                }
            })
    return files


###############################################################
# test endpoints.  These should always return the same thing! 
###############################################################

@app.post('/test/ping')
async def test_ping(ping):
    if ping == 'ping':
        return {
            'ping': 'pong'
        }
    raise HTTPException(status_code=400, detail="we only ping in these here parts")


# TODO
@app.post('/test/predict')
async def test_predict(fileToPredict):
    if not path.exists(fileToPredict):
        raise HTTPException(status_code=503, detail='file does not exist')
    if DEBUG_MODE:
        return DEBUG_MAP
    else:
        return p.predict(fileToPredict)


# TODO make paths static
@app.post('/test/get_valid_files')
async def test_get_valid_files():
    return {
        'validFiles': {
            '0': {
                'path': get_random_file(),
            },
            '1': {
                'path': get_random_file(),
            },
            '2': {
                'path': get_random_file(),
            },
            '3': {
                'path': get_random_file(),
            },
            '4': {
                'path': get_random_file(),
            },
        }
    }
    return DEBUG_MAP


@app.get('/')
async def hello_world():
    return {
        'hello': 'hello world'
    }
