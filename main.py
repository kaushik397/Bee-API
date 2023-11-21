from typing import Union
from fastapi import FastAPI,File, UploadFile
from pydantic import BaseModel, ValidationError, root_validator
from fastapi.exceptions import RequestValidationError
from fastapi.responses import FileResponse, JSONResponse
import os
from questions import questionGen
from topics import TopicGen

class Questions(BaseModel):
    Topic:str
    APIkey:str
    @root_validator (pre=True,skip_on_failure=True)
    def change_input_data(cls, v):
        if len(v) < 2:
            raise ValueError("All the fields are required")
        return v

class Topics(BaseModel):
    Topic:str
    difficulty:str
    APIkey:str
    @root_validator (pre=True,skip_on_failure=True)
    def change_input_data(cls, v):
        if len(v) < 3:
            raise ValueError("All the fields are required")
        return v

app = FastAPI()
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    errors = []
    for error in exc.errors():
        field = '.'.join(error['loc'])
        message = error['msg']
        errors.append({'field': field, 'message': message})

    return JSONResponse(
        status_code=422,
        content={'detail': 'Validation error', 'errors': errors},
    )

@app.get("/",status_code=200)
def status():
    return{"status":200}

@app.post("/questions")
async def RequestedData(item:Questions):
    item=item.dict()
    topic=item['Topic']
    apikey=item['APIkey']
    response = questionGen(topic=topic,apikey=apikey)
    if response!='':
        return response

@app.post("/questions/subtopics")
async def RequestedTopic(topics:Topics):
    topics=topics.dict()
    topicsloc=topics['Topic']
    difficulty=topics['difficulty']
    apikey=topics['APIkey']
    response =TopicGen(topic=topicsloc,difficulty=difficulty,apiKey=apikey)
    if response!='':
        return response

    
