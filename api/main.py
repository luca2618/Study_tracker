from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware
from classifier import predict
from pydantic import BaseModel

app = FastAPI()

class Data(BaseModel):
    input: str

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#uvicorn main:app --reload
@app.get("/get_classify/{item_id}")
async def read_user_item(item_id: str):
    print(item_id)
    result = predict(item_id)
    print(result)
    return result[0]

#uvicorn main:app --reload
@app.post("/classify")
async def read_post(data: str):
    print(data)
    result = predict(data)
    print(result)
    return result[0]

@app.get("/hello")
async def root():
    return {"message": "Hello World"}

@app.get("/no_hello")
def root():
    return {"message": "No Hello World"}