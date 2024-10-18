import os
from typing import List, Optional

from fastapi import FastAPI, Request, Response
from pydantic import BaseModel

from model import default_labels, model

os.environ["HF_HOME"] = "/tmp/huggingface"
os.environ["TRANSFORMERS_CACHE"] = "/tmp/huggingface"


class Input(BaseModel):
    keywords: List[str]
    labels: Optional[List[str]] = None


app = FastAPI()


@app.get("/ping")
def ping():
    status = 200 if model else 404
    return Response(status_code=status)


@app.post("/invocations")
async def invocations(request: Request):
    input_ = await request.json()
    labels = input_.get("labels", default_labels)

    if input_.get("keywords"):
        predictions = model.batch_predict_entities(
            input_.get("keywords"), labels, threshold=0.5, flat_ner=True
        )
        if predictions:
            return predictions
