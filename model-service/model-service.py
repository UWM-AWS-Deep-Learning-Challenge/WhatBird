from os import path

from fastapi import FastAPI
from fastapi.exceptions import HTTPException
import random
import pathlib
from Predictor import *

app = FastAPI()
# TODO pass in model
p = Predictor()


def get_random_file():
    file = random.choice(os.listdir('../data/valid'))
    return pathlib.Path(file).resolve()


##############################################################
# production endpoints
##############################################################

# TODO
@app.post('/production/predict')
async def production_predict():
    raise HTTPException(status_code=501, detail="not implemented!")


# TODO
@app.post('/production/get_valid_files')
async def production_get_valid_files():
    raise HTTPException(status_code=501, detail="not implemented!")


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
# TODO check if invalid path crashes or just returns http exception
@app.post('/test/predict')
async def test_predict(fileToPredict):
    if not path.exists(fileToPredict):
        raise HTTPException(status_code=503, detail='file does not exist')
    # try:
    #     assert os.path.exists(fileToPredict), 'I can\'t find that bird bro'
    # except AssertionError as e:
    #     return {
    #         'e'
    #     }
    return p.predict(fileToPredict)
    # return {
    #     'prediction': 'american coot 2'
    # }


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


@app.get('/')
async def hello_world():
    return {
        'hello': 'hello world'
    }
