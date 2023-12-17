from fastapi import FastAPI;

# Correrlo: python -m uvicorn main:app --reload
# Url: http://127.0.0.1:8000/docs

app = FastAPI();

@app.get('/')
async def root():
    return {"message": "Hello World!"};

@app.get('/url')
async def url():
    return {"url": "https://mouredev.com/python"};


