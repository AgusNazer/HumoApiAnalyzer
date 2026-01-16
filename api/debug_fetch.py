import sys
import os

# Agrega tanto api como utils al path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

from utils.fetcher import fetch_text_from_url

url = "https://www.soyhenry.com/carrera-ai-engineering"

try:
    print(f"Descargando: {url}\n")
    text = fetch_text_from_url(url)
    
    # Mostrar primeros 2000 caracteres
    print("CONTENIDO DESCARGADO (primeros 2000 caracteres):")
    print("="*50)
    print(text[:2000])
    print("\n" + "="*50)
    print(f"\nTamaño total: {len(text)} caracteres")
    
except Exception as e:
    print(f"Error: {str(e)}")
