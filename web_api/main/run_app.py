from fastapi import FastAPI
from joblib import load
from pydantic import BaseModel, conlist
from app import api

clf = load("app/forest_model.joblib")
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


class DataModel(BaseModel):
    data: conlist(float, min_items=29, max_items=29)


@app.post("/calc/")
async def create_item(sent_data: DataModel):
    try:
        result = clf.predict([sent_data.data])
        if result[0] == 0:
            response = "Not Fraud!"
        else:
            response = "A Fraud!"

    except Exception as e:
        print("EXECPTION: ", e)

    return {"messege": "Successfully Done!", "response": response}


app.include_router(api.router)

