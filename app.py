from fastapi import FastAPI
import joblib
import numpy as np
import os
import time

app = FastAPI()

MODEL_PATH = os.getenv("MODEL_PATH", "model_v1.pkl")
model = joblib.load(MODEL_PATH)

@app.get("/")
def home():
    return {"message": f"ML Model API running, version {MODEL_PATH}"}

@app.post("/predict")
def predict(features: list):
    start_time = time.time()
    try:
        prediction = model.predict([np.array(features)])
        latency = round(time.time() - start_time, 4)
        return {"prediction": int(prediction[0]), "version": MODEL_PATH, "latency": latency}
    except Exception as e:
        return {"error": str(e)}
