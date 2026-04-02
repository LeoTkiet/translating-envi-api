from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

app = FastAPI()

class TranslateInput(BaseModel):
    text: str = Field(..., title="Text to translate", min_length=2)
    source_lang: str = Field(default="English", title="Source Language")
    target_lang: str = Field(default="Vietnamese", title="Target Language")

# global variables for AI
tokenizer = None
model = None

# event run when startup server
@app.on_event("startup")
async def load_model():
    global tokenizer, model
    try:
        print("Loading tokenizer and model... (This might take a minute)")
        model_name = "Helsinki-NLP/opus-mt-en-vi"
        
        # load tokenizer and model
        # Note: Helsinki-NLP models require 'sentencepiece' and 'sacremoses'
        try:
            tokenizer = AutoTokenizer.from_pretrained(model_name)
        except Exception as e:
            print(f"Error loading tokenizer: {e}")
            print("Hint: Make sure 'sentencepiece' and 'sacremoses' are installed.")
            raise e

        try:
            model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
        except Exception as e:
            print(f"Error loading model: {e}")
            raise e
        
        print("Model loaded successfully!")
    except Exception as e:
        print(f"Critical error during startup: {e}")

# API root
@app.get("/")
async def root():
    return {
        "message": "Translating API is ready",
        "model": "Helsinki-NLP/opus-mt-en-vi"
    }

# API translate
@app.post("/translate")
async def predict(data: TranslateInput):
    # check empty data
    if not data.text.strip():
        raise HTTPException(status_code=400, detail="Text cannot be empty.")
    
    # check model loaded
    if model is None or tokenizer is None:
        raise HTTPException(status_code=503, detail="Model is still loading. Please try again in a moment.")

    try:
        # convert text to number (Tensor)
        inputs = tokenizer(data.text, return_tensors="pt")
        
        # AI process and generate answer
        with torch.no_grad():
            outputs = model.generate(**inputs)
        
        # convert Tensor to text
        translated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
        
        return {
            "source_text": data.text,
            "translation": translated_text,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating answer: {str(e)}")
