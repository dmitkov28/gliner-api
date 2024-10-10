from typing import List

from fastapi import FastAPI, Response
from pydantic import BaseModel

from model import default_labels, model
import os

os.environ["HF_HOME"] = "/tmp/huggingface"
os.environ["TRANSFORMERS_CACHE"] = "/tmp/huggingface"


class Input(BaseModel):
    keywords: List[str]


app = FastAPI()


@app.get("/health")
def health():
    return Response(status_code=200)


@app.post("/predict")
def predict(keywords: Input):
    if keywords.keywords:
        predictions = model.batch_predict_entities(
            keywords.keywords, default_labels, threshold=0.5, flat_ner=True
        )
        if predictions:
            return predictions
