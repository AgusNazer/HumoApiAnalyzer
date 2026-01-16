from pydantic import BaseModel
from datetime import datetime


class AnalysisSignals(BaseModel):
    promesas_laborales: int
    lenguaje_exagerado: int
    falta_transparencia: int
    autoridad_dudosa: int


class AnalyzeRequest(BaseModel):
    url: str


class AnalyzeResponse(BaseModel):
    category: str
    score: int
    signals: AnalysisSignals
    explanation: str
    created_at: datetime
