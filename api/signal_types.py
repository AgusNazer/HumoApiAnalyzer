from enum import Enum


class SignalType(str, Enum):
    PROMESA_EMPLEO = "promesa_empleo"
    PROMESA_SUELDO = "promesa_sueldo"
    TIEMPO_IRREAL = "tiempo_irreal"
    SENIORITY_FALSO = "seniority_falso"
    EXAGERACION = "exageracion"
