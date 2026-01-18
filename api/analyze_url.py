import sys
import os
import argparse

# Agrega tanto api como utils al path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

from utils.rules import analyze_text
from utils.fetcher import fetch_text_from_url

#API 
def analyze_url_api(url: str) -> dict:
    """Analiza una URL y devuelve los resultados en formato dict para la API"""
    try:
        text = fetch_text_from_url(url)
        result = analyze_text(text)
        
        # Convertir SignalType a dict simple con sus meanings
        signals_detail = {}
        total_score = 0
        
        for signal, count in result.items():
            signal_name = signal.value
            meanings = SIGNAL_MEANINGS.get(signal_name, {})
            meaning = meanings.get(count, f"⚠️ {count} detecciones")
            
            signals_detail[signal_name] = {
                "count": count,
                "meaning": meaning
            }
            total_score += count

        # Categoría final
        if total_score <= 2:
            risk_level = "BAJO_RIESGO"
            category = "🟢 Curso RAZONABLE / Transparente"
        elif total_score <= 5:
            risk_level = "MEDIO_RIESGO"
            category = "🟡 Promesas POCO REALISTAS - Revisar con cuidado"
        else:
            risk_level = "ALTO_RIESGO"
            category = "🔴 ALTO RIESGO de marketing engañoso"
        
        return {
            "url": url,
            "score": total_score,
            "signals": signals_detail,
            "risk_level": risk_level,
            "category": category
        }
            
    except Exception as e:
        raise Exception(f"Error al procesar la URL: {str(e)}")
    
    
# para ver por consola, no para la API 
# Mapeo de interpretaciones por señal y cantidad
SIGNAL_MEANINGS = {
    "promesa_empleo": {
        0: "✅ No promete empleo",
        1: "🟡 Promete 1 empleo",
        2: "🔴 Promete 2+ empleos",
    },
    "promesa_sueldo": {
        0: "✅ Sin promesas salariales falsas",
        1: "🟡 Promesa salarial sospechosa",
        2: "🔴 Múltiples promesas salariales",
    },
    "tiempo_irreal": {
        0: "✅ Tiempos realistas",
        1: "🟡 Tiempos algo irreales",
        2: "🔴 Tiempos muy irreales",
    },
    "seniority_falso": {
        0: "✅ Requiere experiencia apropiada",
        1: "🟡 Contradicción de experiencia",
        2: "🔴 Múltiples contradicciones",
    },
    "exageracion": {
        0: "✅ Lenguaje normal",
        1: "🟡 Algo exagerado",
        2: "🔴 Muy exagerado",
    },
}


def analyze_url(url: str) -> None:
    """Analiza una URL y muestra las señales de alerta encontradas"""
    try:
        print(f"\n🔍 Analizando: {url}\n")
        print("⏳ Descargando contenido...")
        
        text = fetch_text_from_url(url)
        
        print("✅ Contenido descargado. Analizando...\n")
        
        result = analyze_text(text)
        total_score = 0

        print("📊 ANÁLISIS DE SEÑALES DE ALERTA:\n" + "="*50)
        for signal, count in result.items():
            signal_name = signal.value
            meanings = SIGNAL_MEANINGS.get(signal_name, {})
            meaning = meanings.get(count, f"⚠️ {count} detecciones")
            print(f"{signal_name:20} => {count} | {meaning}")
            total_score += count

        print("="*50)
        print(f"{'SCORE TOTAL':20} => {total_score}\n")

        # Categoría final - MÁS ESTRICTA
        if total_score <= 2:
            print("🟢 Curso RAZONABLE / Transparente")
        elif total_score <= 5:
            print("🟡 Promesas POCO REALISTAS - Revisar con cuidado")
        else:
            print("🔴 ALTO RIESGO de marketing engañoso")
            
    except Exception as e:
        print(f"❌ Error al procesar la URL: {str(e)}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analiza una URL para detectar señales de marketing engañoso")
    parser.add_argument("url", help="URL a analizar")
    
    args = parser.parse_args()
    analyze_url(args.url)

