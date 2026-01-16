import re
import sys
from typing import Dict
from pathlib import Path

# Agregar carpeta api al path para importar signal_types
api_path = str(Path(__file__).parent.parent / 'api')
if api_path not in sys.path:
    sys.path.insert(0, api_path)

from signal_types import SignalType
from .patterns import (
    PROMESA_EMPLEO,
    PROMESA_SUELDO,
    TIEMPO_IRREAL,
    SENIORITY_FALSO,
    EXAGERACION,
)


def count_matches(text: str, patterns: list[str]) -> int:
    total = 0
    for pattern in patterns:
        if re.search(pattern, text, re.IGNORECASE):
            total += 1
    return total


def analyze_text(text: str) -> Dict[SignalType, int]:
    return {
        SignalType.PROMESA_EMPLEO: count_matches(text, PROMESA_EMPLEO),
        SignalType.PROMESA_SUELDO: count_matches(text, PROMESA_SUELDO),
        SignalType.TIEMPO_IRREAL: count_matches(text, TIEMPO_IRREAL),
        SignalType.SENIORITY_FALSO: count_matches(text, SENIORITY_FALSO),
        SignalType.EXAGERACION: count_matches(text, EXAGERACION),
    }
