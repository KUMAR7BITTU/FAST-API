from fastapi import FastAPI
from typing import Union # To print default value in query parameter
from enum import Enum

app_name = FastAPI()

@app_name.get('/hello')
async def read_root():
    return {"message":"Hello from bittu side"}

@app_name.get('/hi')
async def bittu():
    return {"message":"Hi, how are you ?"}

# Path parameter
@app_name.get('/item/{Item}')
async def path_fun(Item):
    var_name= {"path_variable":Item}
    return (var_name)

@app_name.get('/item1/{Item}')
async def path_fun1(Item):
    var_name = {"path_variable":Item}
    return (var_name)

# Path parameter
# @app_name.get('/query')
# async def query_fun(roll_no:int, name:Union[str,None]="bittu"):
#     var_name = {"name":name,"roll_no":roll_no}
#     return (var_name)

@app_name.get('/query')
async def query_fun(roll_no:int=0, name:str="bittu"):
    var_name = {"name":name,"roll_no":roll_no}
    return (var_name)


class Choice_Names(str,Enum):
    one = "one"
    two = "two"
    three = "three"


# @app_name.get('/models/{model_name}')
# async def get_model(model_name:Choice_Names):
#     return (model_name)

@app_name.get('/models/{model_name}')
async def get_model(model_name=Choice_Names):
    if model_name == Choice_Names.one:
        return {"model_name":model_name,"message":"Calling one!"}
    
    if model_name == Choice_Names.two:
        return {"model_name":model_name,"message":"Calling two"}
    
    return {"model_name":model_name,"message":"Calling three"}