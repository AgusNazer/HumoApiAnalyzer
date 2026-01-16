from datetime import datetime
from .schemas import AnalyzeResponse, AnalysisSignals


def analyze_url(url: str) -> AnalyzeResponse:
    # Log inicial
    print("URL analizada:", url)

    # Señales (hardcodeadas por ahora)
    signals = AnalysisSignals(
        promesas_laborales=2,
        lenguaje_exagerado=3,
        falta_transparencia=1,
        autoridad_dudosa=2,
    )

    # Score total
    score = (
        signals.promesas_laborales
        + signals.lenguaje_exagerado
        + signals.falta_transparencia
        + signals.autoridad_dudosa
    )

    # Categoría segn score
    def calculate_category(score: int) -> str:
        if score <= 6:
            return "🟢 Curso razonable / transparente"
        elif score <= 13:
            return "🟡 Promesas poco realistas"
        else:
            return "🔴 Alto riesgo de marketing engañoso"

    category = calculate_category(score)

    # Logs finales
    print("Señales:", signals)
    print("Score total:", score)
    print("Categoría:", category)

    # Respuesta
    return AnalyzeResponse(
        category=category,
        score=score,
        signals=signals,
        explanation="El contenido presenta indicadores claros de marketing exagerado.",
        created_at=datetime.utcnow(),
    )
