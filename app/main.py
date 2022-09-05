import os
import sys
import pickle
import numpy as np
from pathlib import Path
from fastapi import Body, FastAPI
from pydantic import BaseSettings, BaseModel

from .data import example, make_df_from_single, FeatureData


class Settings(BaseSettings):
    model_path: str


class SinglePrediction(BaseModel):
    pred: int
    probability: float


app = FastAPI()
settings = Settings()

model_path = Path(settings.model_path)

if not model_path.exists():
    raise ValueError(
        f"model is not found in provided path: {settings.model_path}")

with open(settings.model_path, 'rb') as f:
    pipeline = pickle.load(f)

# cwd = os.getcwd()
# print("Current working directory: {0}".format(cwd))


def single_prediction(data: FeatureData) -> SinglePrediction:
    df = make_df_from_single(data.dict())
    preds = pipeline.predict_proba(df)[0]
    idx = np.argmax(preds)
    return SinglePrediction(pred=idx, probability=preds[idx])


@app.get("/")
async def root():
    return single_prediction(example)


@app.post("/predict")
async def predict(payload: FeatureData = Body(example=example.dict())):
    return single_prediction(payload)
