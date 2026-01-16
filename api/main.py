from fastapi import FastAPI
from .schemas import AnalyzeRequest, AnalyzeResponse
from .analyzer import analyze_url

app = FastAPI(title="Humo Analyzer API")


@app.post("/analyze", response_model=AnalyzeResponse)
def analyze(request: AnalyzeRequest):
    return analyze_url(request.url)
