from fastapi import FastAPI, Query, Form, File, UploadFile, HTTPException, Depends
from typing import Union, Annotated # To print default value in query parameter
from enum import Enum
from pydantic import BaseModel # To make schema


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

# @app_name.get('/query')
# async def query_fun(roll_no:int=0, name:str="bittu"):
#     var_name = {"name":name,"roll_no":roll_no}
#     return (var_name)


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

class Schema1(BaseModel):
    name:str
    Class:str
    roll_no:int

# request body
@app_name.post('/items/')
async def create_item(item:Schema1):
    return item

# @app_name.get('/query')
# async def query_fun(roll_no:Union[int,None]=None, name:Union[str,None]=None):
#     var_name = {"name":name,"roll_no":roll_no}
#     return (var_name)

# Now that we can add some extra validation with Query
@app_name.get('/query')
async def query_fun(name:Union[str,None]=None, roll_no:Union[str,None] = Query(default=None, min_length=3, max_length=4)):
    var_name = {"name":name,"roll_no":roll_no}
    return (var_name)

# We can't apply min_length and max_length on int variable (roll_no must be str)

# http://127.0.0.1:8000/query?name=bittu&roll_no=9999

# q: str | None = None
# q : Annotated[str | None] = None

# Both of those versions mean the same thing, q is a parameter that can be a str or None, and by default, it is None.

@app_name.get('/query1')
async def query_fun1(name : Annotated[str | None, Query(max_length=4)]=None):
    var_name = {"name":name}
    return (var_name)

# form data
@app_name.post("/login/") 
async def login(username : Annotated[str,Form()], password : Annotated[str,Form()]):
    return {"username":username, "password":password}

@app_name.post('/form/data') # query
async def form_data(username:str):
    return {"username":username}

@app_name.post('/form/data1')
async def form_data1(username : str = Form(), password : str = Form()):
    return {"username":username, "password":password}

class vipan(BaseModel):
    one : str 
    two : str 
    three : int

@app_name.post('/form/data2')
async def form_data2(items:vipan):
    return {"items":items}

# file upload
@app_name.post('/file/upload')
async def file_bytes_len(file : bytes = File()):
    return {"file":len(file)}

@app_name.post('/file/upload1')
async def file_upload(file:UploadFile):
    return {
        "file":file.filename,
        "size":file.size,
        "file-content-type":file.headers.get("content-type")
        }

@app_name.post('/form/data/file_upload')
async def formdata_upload(file1 : UploadFile, file2 : bytes = File(), name : str = Form()):
    return {
        "file1_name" : file1.filename,
        "bytes_file" : len(file2),
        "name" : name
    }

# Depend keyword
async def func1(item:str):
    return {"message":f"Hello, mrs {item}"}

@app_name.get('/func2')
async def func2(name:str = Depends(func1)):
    return {"message":name}


#Error Handling
# @app_name.get('/error/handling')
# async def handle_error(item:int):
#     if item == 2:
#         return HTTPException(status_code=404,detail="Item is equal to 2 try another value")
#     return {"message":item}

items = [1,2,3,4,5,6,7]
@app_name.get('/error/handling')
async def handle_error(item:int):
    if item not in items:
        return HTTPException(status_code=404,detail=f"{item} is not present in items container.")
    return {"message":item}


