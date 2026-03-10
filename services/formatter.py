from google.cloud import language_v1
#voy a dar formato a los valores
def format_nlp_result(text, analysis):
    sentiment = analysis["sentiment"]
    entities = analysis["entities"]

    return {
        "input": {
            "tipo": "texto",
            "texto_original": text
        },
        "sentimiento": {
            "polaridad": get_polarity(sentiment.score),
            "score": sentiment.score,
            "intensidad": sentiment.magnitude
        },
        "emociones": infer_emotions(sentiment.score, sentiment.magnitude),
        "entidades": extract_entities(entities),
        "categoria": categorize_review(entities, text),
        "recomendacion": generate_recommendation(sentiment.score, entities)
    }

def get_polarity(score):
    if score > 0.25:
        return "positivo"
    elif score < -0.25:
        return "negativo"
    else:
        return "neutral"
    
def infer_emotions(score, magnitude):
    if score > 0.3:
        return ["satisfacción"]
    if score < -0.3:
        return ["frustración"]
    if magnitude > 1.5:
        return ["intensidad emocional"]
    return ["neutral"]

def extract_entities(entities):
    productos = []
    caracteristicas = []
    problemas = []

    for e in entities:
        name = e.name.lower()

        if e.type_ == language_v1.Entity.Type.CONSUMER_GOOD:
            productos.append(name)

        elif any(word in name for word in ["batería", "pantalla", "cámara"]):
            caracteristicas.append(name)

        elif any(word in name for word in ["problema", "roto", "falla", "mal"]):
            problemas.append(name)

    return {
        "producto": productos,
        "caracteristicas": caracteristicas,
        "problemas": problemas
    }

def categorize_review(entities, text):
    text = text.lower()

    if "envío" in text or "entrega" in text:
        return "logística"

    if "precio" in text or "caro" in text:
        return "precio"

    if "batería" in text or "pantalla" in text:
        return "calidad_del_producto"

    return "general"

def generate_recommendation(score, entities):
    if score < -0.3:
        return "Revisar los problemas más frecuentes del producto"

    if score > 0.3:
        return "Mantener la calidad actual y potenciar puntos fuertes"

    return "Recoger más feedback para detectar mejoras"