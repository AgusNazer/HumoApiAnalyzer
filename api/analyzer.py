from datetime import datetime
import sys
import os

# Add parent directory to path for module imports
sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from schemas import AnalyzeResponse, AnalysisSignals, SignalDetail
from signal_types import SignalType
from weights import SIGNAL_WEIGHTS
from utils.rules import analyze_text
from utils.fetcher import fetch_text_from_url

# Mapeo de interpretaciones
SIGNAL_MEANINGS = {
    "promesa_empleo": {0: "✅ No promete empleo", 1: "🟡 Promete 1 empleo", 2: "🔴 Promete 2+ empleos"},
    "promesa_sueldo": {0: "✅ Sin promesas salariales falsas", 1: "🟡 Promesa salarial sospechosa", 2: "🔴 Múltiples promesas salariales"},
    "tiempo_irreal": {0: "✅ Tiempos realistas", 1: "🟡 Tiempos algo irreales", 2: "🔴 Tiempos muy irreales"},
    "seniority_falso": {0: "✅ Requiere experiencia apropiada", 1: "🟡 Contradicción de experiencia", 2: "🔴 Múltiples contradicciones"},
    "exageracion": {0: "✅ Lenguaje normal", 1: "🟡 Algo exagerado", 2: "🔴 Muy exagerado"},
}

def analyze_url(url: str) -> AnalyzeResponse:
    try:
        # Obtener contenido
        text = fetch_text_from_url(url)
        
        # Analizar texto
        result = analyze_text(text)
        
        # Convertir a SignalDetail y calcular score
        signals_detail = {}
        total_score = 0
        
        for signal, count in result.items():
            signal_name = signal.value
            meanings = SIGNAL_MEANINGS.get(signal_name, {})
            meaning = meanings.get(count, f"⚠️ {count} detecciones")
            
            signals_detail[signal_name] = SignalDetail(
                count=count,
                meaning=meaning
            )
            total_score += count

        # Determinar categoría
        if total_score <= 2:
            category = "🟢 Curso RAZONABLE / Transparente"
        elif total_score <= 5:
            category = "🟡 Promesas POCO REALISTAS"
        else:
            category = "🔴 ALTO RIESGO de marketing engañoso"
        
        # Crear objeto AnalysisSignals con todos los campos
        signals = AnalysisSignals(
            promesa_empleo=signals_detail.get("promesa_empleo", SignalDetail(count=0, meaning="✅ No promete empleo")),
            promesa_sueldo=signals_detail.get("promesa_sueldo", SignalDetail(count=0, meaning="✅ Sin promesas salariales falsas")),
            tiempo_irreal=signals_detail.get("tiempo_irreal", SignalDetail(count=0, meaning="✅ Tiempos realistas")),
            seniority_falso=signals_detail.get("seniority_falso", SignalDetail(count=0, meaning="✅ Requiere experiencia apropiada")),
            exageracion=signals_detail.get("exageracion", SignalDetail(count=0, meaning="✅ Lenguaje normal"))
        )

        return AnalyzeResponse(
            category=category,
            score=total_score,
            signals=signals,
            explanation=f"Análisis completado. Score: {total_score}. " + 
                       ("Curso confiable." if total_score <= 2 else 
                        "Revisar promesas ofrecidas." if total_score <= 5 else
                        "Advertencia: Alto riesgo detectado."),
            created_at=datetime.utcnow()
        )
            
    except Exception as e:
        raise Exception(f"Error al procesar la URL: {str(e)}")
