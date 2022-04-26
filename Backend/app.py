from fastapi import FastAPI, Request
from model import mine_data
app = FastAPI()

 

@app.get("/")
def test(request: Request):
    return {"testing passed"}
@app.post("/grade")
def grade(email:str,password:str):
        res=mine_data(email,password)
        print(res)
        return {"output":res}
        
         