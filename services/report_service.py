def build_report(text, nlp_analysis, image_analysis=None, transcript=None):
    # resumen de valores importantes
    sentimiento = "neutral"
    if nlp_analysis["sentiment"].score > 0.25:
        sentimiento = "positivo"
    elif nlp_analysis["sentiment"].score < -0.25:
        sentimiento = "negativo"

    puntuacion_general = round(
        abs(nlp_analysis["sentiment"].score), 2
    )

    # entidades 
    productos = []
    caracteristicas = []
    problemas = []

    for entity in nlp_analysis["entities"]:
        if entity.type_.name in ["CONSUMER_GOOD"]:
            productos.append(entity.name)
        elif entity.type_.name in ["OTHER"]:
            caracteristicas.append(entity.name)

    # resultado final
    return {
        "resumen_ejecutivo": {
            "sentimiento_predominante": sentimiento,
            "puntuacion_general": puntuacion_general
        },
        "analisis_detallado": {
            "entidades": {
                "productos": productos,
                "caracteristicas": caracteristicas,
                "problemas": problemas
            }
        },
        "informacion_multimodal": {
            "texto": text,
            "audio_transcrito": transcript,
            "imagen": image_analysis
        },
        "recomendaciones": [
            "Revisar problemas mencionados",
            "Analizar satisfacción del cliente"
        ]
    }