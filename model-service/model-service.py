from fastapi import FastAPI
from fastapi.exceptions import HTTPException

app = FastAPI()

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

# TODO
@app.post('/test/ping')
async def test_ping():
    raise HTTPException(status_code=501, detail="not implemented!")

# TODO
@app.post('/test/predict')
async def test_predict():
    raise HTTPException(status_code=501, detail="not implemented!")

# TODO
@app.post('/test/get_valid_files')
async def test_get_valid_files():
    raise HTTPException(status_code=501, detail="not implemented!")
