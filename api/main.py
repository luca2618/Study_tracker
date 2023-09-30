from fastapi import FastAPI

app = FastAPI()
#uvicorn main:app --reload
@app.get("/classify/{item_id}")
async def read_user_item(item_id: str):
    print(item_id)
    return item_id

#uvicorn main:app --reload
@app.post("/post")
async def read_post(data: str):
    print(data)
    return data

@app.get("/hello")
async def root():
    return {"message": "Hello World"}

@app.get("/no_hello")
def root():
    return {"message": "No Hello World"}