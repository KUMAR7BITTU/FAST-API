from fastapi import FastAPI

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

@app_name.get('/query')
async def query_fun(name:str, roll_no:int):
    var_name = {"name":name,"roll_no":roll_no}
    return (var_name)