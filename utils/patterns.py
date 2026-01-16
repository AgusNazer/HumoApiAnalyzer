
# ---------------- PROMESAS DE EMPLEO ----------------
PROMESA_EMPLEO = [
    r"trabajo garantizado",
    r"salida laboral inmediata",
    r"empleo asegurado",
    r"consegu[ií] trabajo",
    r"oferta laboral al egresar",
    r"empresas te buscan",
]

# ---------------- PROMESAS DE SUELDO ----------------
PROMESA_SUELDO = [
    r"sueldo (alto|elevado|en d[oó]lares)",
    r"cobra en d[oó]lares",
    r"salario internacional",
    r"\d{4,5}\s*(usd|d[oó]lares)",
    r"ganar \d{4,5}",
    r"sueldo en d[oó]lares asegurado",
    r"vivir programando",
    r"trabaja para el exterior",
]

# ---------------- TIEMPOS IRREALES ----------------
TIEMPO_IRREAL = [
    r"en \d+\s*(meses|semanas)",
    r"en menos de \d+ meses",
    r"en tiempo r[eé]cord",
    r"aprend[eé] en d[ií]as",
    r"aprend[eé] r[aá]pido",
]

# ---------------- SENIORITY FALSO ----------------
SENIORITY_FALSO = [
    r"nivel senior",
    r"listo para senior",
    r"como un profesional",
    r"perfil job ready",
    r"experto en",
    r"master en",
    # Contradicciones junior/senior
    r"junior.*\d+\s*años",
    r"juniors?.*\d+\s*años de experiencia",
    r"sin experiencia.*\d+\s*años",
]

# ---------------- EXAGERACIONES / HYPE ----------------
EXAGERACION = [
    # absolutos
    r"100% garantizado",
    r"sin experiencia previa",
    r"desde cero absoluto",
    r"no necesit[aá]s saber matem[aá]tica",
    r"no necesit[aá]s programar",

    # mercado laboral inflado
    r"alta demanda asegurada",
    r"faltan miles de profesionales",
    r"el mercado explota",
    r"las empresas se pelean",

    # manipulación emocional
    r"no te quedes afuera",
    r"[uú]ltimos cupos",
    r"oportunidad [uú]nica",
    r"es ahora",
    r"solo hoy",

    # validación dudosa
    r"casos reales",
    r"testimonios reales",
    r"alumnos trabajando",
    r"historias de [eé]xito",

    # IA / humo
    r"inteligencia artificial sin saber programar",
    r"ia sin c[oó]digo",
    r"machine learning f[aá]cil",
    r"data science desde cero",
]
