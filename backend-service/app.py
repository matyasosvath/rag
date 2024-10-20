import traceback
from fastapi import FastAPI
from fastapi.responses import JSONResponse

import version

from src.logging import logger
from src import helper, typing
from src.service import rag


app = FastAPI()


helper.log_startup_diagnostics()


@app.exception_handler(Exception)
async def exception_handler(req, exc):
    logger.error("An error occurred: %s", exc)
    logger.error(traceback.format_exc())
    return JSONResponse({"error": "Error during model response!"}, 500)


@app.get('/')
@app.get('/info')
def info():
    return {"version": version}


@app.post('/question/{model_name}')
def generate(model_name: typing.RagModels, question: typing.Question):
    result = rag.inference(model_name, question)
    return {"result": result}



