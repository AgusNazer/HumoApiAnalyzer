from pydantic import BaseModel
from datetime import datetime
from typing import Dict, Any


class SignalDetail(BaseModel):
    """Detalle de cada señal detectada"""
    count: int
    meaning: str


class AnalysisSignals(BaseModel):
    """Todos los 5 tipos de señales detectadas"""
    promesa_empleo: SignalDetail
    promesa_sueldo: SignalDetail
    tiempo_irreal: SignalDetail
    seniority_falso: SignalDetail
    exageracion: SignalDetail


class AnalyzeRequest(BaseModel):
    url: str


class AnalyzeResponse(BaseModel):
    category: str
    score: int
    signals: AnalysisSignals
    explanation: str
    created_at: datetime
