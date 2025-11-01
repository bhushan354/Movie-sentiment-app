from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import numpy as np
import pickle
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model

with open("tokenizer.pkl", "rb") as f:
    tokenizer = pickle.load(f)

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class ReviewInput(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "LSTM Sentiment API is running!"}

@app.post("/predict")
def predict_sentiment(data: ReviewInput):
    text = data.text

    seq = tokenizer.texts_to_sequences([text])
    padded = pad_sequences(seq, maxlen=200)

    pred = model.predict(padded)
    sentiment = "positive" if pred[0][0] >= 0.5 else "negative"
    confidence = round(float(pred[0][0]) if pred[0][0] >= 0.5 else 1 - float(pred[0][0]), 2)

    return {"sentiment": sentiment, "confidence": confidence}
