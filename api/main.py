from fastapi import FastAPI

app = FastAPI()
#uvicorn ./api/main:app --reload
@app.get("/classify/{item_id}")
async def read_user_item(item_id: str):
    print(item_id)
    return item_id

@app.get("/hello")
async def root():
    return {"message": "Hello World"}

@app.get("/no_hello")
def root():
    return {"message": "No Hello World"}