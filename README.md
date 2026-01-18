# Humo Analyzer API

**Análisis inteligente de contenido de cursos en línea para detectar promesas engañosas y marketing deceptivo.**

## 📋 Descripción

Humo Analyzer es una API que analiza URLs de cursos en línea y detecta señales de alarma sobre promesas irreales, garantías falsas y marketing engañoso. Utiliza análisis de texto avanzado para identificar patrones que indican posible fraude o exageración.

## ✨ Características

- Análisis automático de contenido web
- Detección de 5 tipos de señales de alarma
- Score cuantitativo de riesgo (0-10)
- Categorización automática de cursos
- Explicaciones detalladas de hallazgos
- Respuestas estructuradas en JSON

## 🚀 Instalación

### Requisitos
- Python 3.8+
- pip

### Setup

```bash
# Clonar repositorio
git clone <repository-url>
cd ApiAnalysis

# Instalar dependencias
pip install -r requirements.txt
```

### Dependencias
- `fastapi` - Framework web
- `requests` - Fetching de URLs
- `beautifulsoup4` - Parsing HTML

## Endpoints

### `POST /analyze`

Analiza una URL y retorna un reporte detallado de señales detectadas.

**Request:**
```json
{
  "url": "https://example.com/curso"
}
```

**Response:**
```json
{
  "category": "🟢 Curso RAZONABLE / Transparente",
  "score": 2,
  "signals": {
    "promesa_empleo": {
      "count": 0,
      "meaning": "✅ No promete empleo"
    },
    "promesa_sueldo": {
      "count": 0,
      "meaning": "✅ Sin promesas salariales falsas"
    },
    "tiempo_irreal": {
      "count": 1,
      "meaning": "🟡 Tiempos algo irreales"
    },
    "seniority_falso": {
      "count": 0,
      "meaning": "✅ Requiere experiencia apropiada"
    },
    "exageracion": {
      "count": 1,
      "meaning": "🟡 Algo exagerado"
    }
  },
  "explanation": "Análisis completado. Score: 2. Curso confiable.",
  "created_at": "2026-01-18T10:30:45.123456"
}
```

## Señales de Detección

| Señal | Descripción | Niveles |
|-------|-------------|---------|
| **promesa_empleo** | Promesas de empleos garantizados | ✅ (0) - 🟡 (1) - 🔴 (2+) |
| **promesa_sueldo** | Promesas de sueldos específicos o garantizados | ✅ (0) - 🟡 (1) - 🔴 (2+) |
| **tiempo_irreal** | Tiempos de aprendizaje irreales | ✅ (0) - 🟡 (1) - 🔴 (2+) |
| **seniority_falso** | Contradicciones en nivel de experiencia requerida | ✅ (0) - 🟡 (1) - 🔴 (2+) |
| **exageracion** | Lenguaje excesivamente exagerado | ✅ (0) - 🟡 (1) - 🔴 (2+) |

## Categorías de Riesgo

- **🟢 Curso RAZONABLE / Transparente** (Score: 0-2)
  - Pocas o ninguna señal de alarma
  - Curso confiable

- **🟡 Promesas POCO REALISTAS** (Score: 3-5)
  - Algunas promesas sospechosas
  - Se recomienda revisar el contenido

- **🔴 ALTO RIESGO** (Score: 6+)
  - Múltiples señales de marketing engañoso
  - Advertencia: Posible fraude

## Estructura del Proyecto

```
ApiAnalysis/
├── api/
│   ├── main.py              # Endpoints principales
│   ├── analyzer.py          # Lógica de análisis
│   ├── schemas.py           # Modelos Pydantic
│   ├── signal_types.py      # Definiciones de señales
│   ├── weights.py           # Pesos de scoring
│   └── patterns.py          # Patrones de regex
├── utils/
│   ├── fetcher.py           # Extrae texto de URLs
│   ├── rules.py             # Reglas de detección
│   └── patterns.py          # Patrones compartidos
├── requirements.txt
└── README.md
```

## 🔧 Uso

### Ejecutar localmente

```bash
# Instalar FastAPI y Uvicorn
pip install fastapi uvicorn

# Iniciar servidor
uvicorn api.main:app --reload

# La API estará disponible en http://localhost:8000
# Documentación interactiva: http://localhost:8000/docs
```

### Ejemplo de uso con curl

```bash
curl -X POST "http://localhost:8000/analyze" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://example.com/course"}'
```

### Ejemplo con Python

```python
import requests

url = "http://localhost:8000/analyze"
payload = {"url": "https://example.com/course"}
response = requests.post(url, json=payload)
print(response.json())
```

## 📝 Licencia

[00000]

## 👥 Autores

Equipo Humo App

## 📞 Contacto

[Agustin.nazer@hotmail.com
www.linkedin.com/in/agustinnazer
]

---

**Nota:** Esta API está en desarrollo. Las señales de detección se mejoran continuamente basado en feedback y análisis.
