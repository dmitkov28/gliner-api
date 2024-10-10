import os
from typing import List, Optional

from fastapi import FastAPI, Response
from pydantic import BaseModel

from model import default_labels, model

os.environ["HF_HOME"] = "/tmp/huggingface"
os.environ["TRANSFORMERS_CACHE"] = "/tmp/huggingface"


class Input(BaseModel):
    keywords: List[str]
    labels: Optional[List[str]] = None


app = FastAPI()


@app.get("/health")
def health():
    return Response(status_code=200)


@app.post("/predict")
def predict(input_: Input):
    labels = input_.labels if input_.labels else default_labels

    if input_.keywords:
        predictions = model.batch_predict_entities(
            input_.keywords, labels, threshold=0.5, flat_ner=True
        )
        if predictions:
            return predictions
