import os
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
app = FastAPI(title="MLOps Milestone 1 Model Serving")
model = joblib.load("model.pkl")

class PredictRequest(BaseModel):
    features: list[float]
class PredictResponse(BaseModel):
    prediction: float
    model_version: str

@app.get("/")
def home():
    return {"status": "running"}
@app.post("/predict", response_model=PredictResponse)
def predict(request: PredictRequest):
    data = np.array(request.features).reshape(1, -1)
    prediction = model.predict(data)[0]
    return PredictResponse(
        prediction=float(prediction),
        model_version="1.0"
    )
if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8080))
    uvicorn.run(app, host="0.0.0.0", port=port)
