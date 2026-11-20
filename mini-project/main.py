from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import pipeline
import spacy

# 1. Initialize the FastAPI app
app = FastAPI(title="NLP Sentiment API")

# 2. Load the model ONCE when the server starts (Global scope)
# This prevents the server from reloading the model on every single request
print("Loading model...")
classifier = pipeline("sentiment-analysis")
print("Model loaded successfully!")


# 3. Define the Request and Response Data Schemas using Pydantic
class TextRequest(BaseModel):
    text: str


class PredictionResponse(BaseModel):
    label: str
    confidence: float


# 4. Create the API Endpoint
@app.post("/analyze-sentiment", response_model=PredictionResponse)
def analyze_sentiment(request: TextRequest):
    # Basic validation to ensure text isn't empty
    if not request.text.strip():
        raise HTTPException(status_code=400, detail="Text cannot be empty")

    try:
        # Run the text through the Hugging Face pipeline
        result = classifier(request.text)[0]

        # Return the formatted response
        return PredictionResponse(
            label=result["label"], confidence=round(result["score"], 4)
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Load spaCy model (make sure you have run: python -m spacy download en_core_web_sm)
nlp = spacy.load("en_core_web_sm")


class AdvancedResponse(BaseModel):
    label: str
    confidence: float
    entities: list


@app.post("/analyze-full", response_model=AdvancedResponse)
def analyze_full(request: TextRequest):
    # 1. Sentiment Analysis (Transformers)
    sentiment_result = classifier(request.text)[0]

    # 2. Named Entity Recognition (spaCy)
    doc = nlp(request.text)
    entities = [{"text": ent.text, "type": ent.label_} for ent in doc.ents]

    return AdvancedResponse(
        label=sentiment_result["label"],
        confidence=round(sentiment_result["score"], 4),
        entities=entities,
    )
