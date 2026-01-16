import sys
import os

# Agrega tanto api como utils al path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

from utils.rules import analyze_text

text = """
Ganá 5000 dólares por semana sin experiencia.
Trabajo garantizado en 2 meses.
Buscamos juniors con 10 años de experiencia.
Es una oportunidad única e irrepetible.
"""

result = analyze_text(text)

for signal, count in result.items():
    print(signal.value, "=>", count)