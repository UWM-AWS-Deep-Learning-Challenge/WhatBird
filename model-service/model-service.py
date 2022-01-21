from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from modelrun import *

app = FastAPI()

##############################################################
# production endpoints
##############################################################

# TODO
@app.post('/production/predict')
async def production_predict(fileToPredict: str):
    return predict(fileToPredict, False)


# TODO
@app.post('/production/get_valid_files')
async def production_get_valid_files(numberOfFiles):
    return get_random_files_as_json(numberOfFiles)


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
    return predict(fileToPredict, True)


# TODO make paths static
@app.post('/test/get_valid_files')
async def test_get_valid_files():
    return {
        'validFiles': {
            '0': {
                'path': get_random_files(),
            },
            '1': {
                'path': get_random_files(),
            },
            '2': {
                'path': get_random_files(),
            },
            '3': {
                'path': get_random_files(),
            },
            '4': {
                'path': get_random_files(),
            },
        }
    }


@app.get('/')
async def hello_world():
    return {
        'hello': 'hello world'
    }
