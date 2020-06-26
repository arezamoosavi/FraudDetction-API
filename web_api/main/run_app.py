from fastapi import FastAPI
from joblib import load
from pydantic import BaseModel, conlist
from app.db import connection
from app import api
from app.db import models

clf = load("app/forest_model.joblib")
app = FastAPI()


@app.on_event("startup")
async def startup_event():
    global cassandradb
    cassandradb = connection.Cassandra()
    cassandradb.sync_table(database=models.result)


@app.on_event("shutdown")
def shutdown_event():
    cassandradb.disconnect()


@app.get("/")
def read_root():
    number_result = models.result.count_all()
    return {"Hello": "World", "number of all data": number_result}


class DataModel(BaseModel):
    data: conlist(float, min_items=29, max_items=29)


@app.post("/calc/")
async def create_item(sent_data: DataModel):
    try:
        result = clf.predict([sent_data.data])
        if result[0] == 0:
            response = "Not Fraud!"
            new_result = models.results(data=[sent_data.data], is_fraud=False)
            print(new_result.items())
            new_result.save()
        else:
            response = "A Fraud!"
            new_result = models.results(data=[sent_data.data], is_fraud=True)

    except Exception as e:
        print("EXECPTION: ", e)

    return {"messege": "Successfully Done!", "response": response}


app.include_router(api.router)
