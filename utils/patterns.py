
# ---------------- PROMESAS DE EMPLEO ----------------
PROMESA_EMPLEO = [
    r"trabajo garantizado",
    r"salida laboral",
    r"empleo asegurado",
    r"consegu[ií] trabajo",
    r"oferta laboral",
    r"empresas te buscan",
    r"demandan",
    r"demanda",
    r"bolsa de trabajo",
    r"colocaci[oó]n",
    r"reclutamiento",
    r"oportunidades laborales",
    r"salida professional",
    r"inserci[oó]n laboral",
    r"job placement",
    r"mercado laboral",
    r"compan[ií]as",
    r"contrata",
    r"recluta",
]

# ---------------- PROMESAS DE SUELDO ----------------
PROMESA_SUELDO = [
    r"sueldo alto",
    r"sueldo elevado",
    r"cobra en d[oó]lares",
    r"salario internacional",
    r"\d{4,5}\s*(usd|d[oó]lares|pesos)",
    r"ganar \d{4,5}",
    r"sueldo en d[oó]lares",
    r"vivir programando",
    r"trabaja para el exterior",
    r"remote.*pago",
    r"trabajar desde casa ganando",
    r"dinero r[aá]pido",
    r"ingresos pasivos",
    r"multiplicar sueldo",
    r"salario competitivo",
    r"sueldo",
]

# ---------------- TIEMPOS IRREALES ----------------
TIEMPO_IRREAL = [
    r"en \d+\s*(meses|semanas|d[ií]as)",
    r"en menos de",
    r"tiempo r[eé]cord",
    r"aprend[eé] en",
    r"aprend[eé] r[aá]pido",
    r"pocas semanas",
    r"un mes",
    r"r[aá]pidamente",
    r"intensivo",
    r"bootcamp",
    r"acelerado",
]

# ---------------- SENIORITY FALSO ----------------
SENIORITY_FALSO = [
    r"nivel senior",
    r"listo para senior",
    r"como un profesional",
    r"job ready",
    r"experto en",
    r"master en",
    # Contradicciones junior/senior
    r"junior.*\d+\s*años",
    r"juniors?.*\d+\s*años",
    r"sin experiencia.*\d+\s*años",
    r"principiante.*profesional",
    r"cero experiencia",
    r"desde cero",
    r"profesional de",
    r"convi[eé]rtete en",
]

# ---------------- EXAGERACIONES / HYPE ----------------
EXAGERACION = [
    # Absolutos y garantías
    r"100% garantizado",
    r"garantizado",
    r"sin experiencia",
    r"desde cero",
    r"no necesit[aá]s",
    
    # Rankings y validación
    r"1st.ranked",
    r"ranking",
    r"mejor",
    r"#1",
    r"top",
    r"lider",
    
    # mercado laboral inflado
    r"alta demanda",
    r"faltan",
    r"explota",
    r"se pelean",
    r"demanda laboral",
    r"miles de oportunidades",
    r"crecimiento exponencial",
    r"economia digital",
    r"transformaci[oó]n digital",

    # manipulación emocional - IMPORTANTE
    r"cupos limitados",
    r"[uú]ltimos cupos",
    r"oportunidad [uú]nica",
    r"es ahora",
    r"solo hoy",
    r"revolucion[aá]rio",
    r"transformador",
    r"cambiar tu vida",
    r"llevar.*al siguiente nivel",
    r"pr[oó]ximo nivel",
    r"potencia",
    r"acelera",
    r"[eé]xito",

    # validación dudosa
    r"casos reales",
    r"testimonios",
    r"alumnos trabajando",
    r"historias de [eé]xito",
    r"miles de graduados",
    r"egresados en",
    r"expertos",
    r"experto en",

    # IA / humo - MUY IMPORTANTE
    r"inteligencia artificial",
    r"ia",
    r"machine learning",
    r"data science",
    r"blockchain",
    r"llm",
    r"agentes",
    r"produccion",
    r"portafolio",
    r"cloud",
    
    # Lenguaje extremo
    r"mejor carrera",
    r"nunca vuelvas",
    r"ser millonario",
    r"libertad financiera",
    r"diseñado por expertos",
    r"con experiencia",
    r"basado en proyectos",
]



