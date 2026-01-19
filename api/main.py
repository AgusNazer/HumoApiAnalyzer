import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from fastapi import FastAPI
from schemas import AnalyzeRequest, AnalyzeResponse
from analyzer import analyze_url

app = FastAPI(title="Humo Analyzer API")

@app.post("/analyze", response_model=AnalyzeResponse)
def analyze(request: AnalyzeRequest):
    return analyze_url(request.url)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)