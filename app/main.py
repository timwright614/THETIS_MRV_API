from typing import List
from fastapi import FastAPI
import pandas as pd


app = FastAPI()

mrv_df = pd.read_pickle("data/mrv_df.pkl")

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/get_vessels")
async def get_vessels(vessel_IMOs: List[int]):

    df = mrv_df[mrv_df.IMO_Number.isin(vessel_IMOs)].sort_values("IMO_Number")

    not_found = [IMO for IMO in vessel_IMOs if IMO not in list(mrv_df.IMO_Number)]
    if len(not_found) == 0:
        not_found.append("no missing IMOs")

    return {"data": df.to_json(orient='records'),
            "not_found" : not_found
    }
