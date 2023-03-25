from typing import List
from fastapi import FastAPI, Body
from db import *

create_logs_table();
app = FastAPI()

@app.get("/logs")
async def fetch_logs():
    return get_logs();

@app.post("/logs")
async def create_log(log: str = Body(...)):
    save_log(log)

@app.delete("/logs")
async def delete_logs():
    truncate_logs_table()
