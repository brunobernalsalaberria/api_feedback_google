from google.cloud import language_v1

def analyze_text(text):
    client = language_v1.LanguageServiceClient()

    document = {
        "content": text,
        "type_": language_v1.Document.Type.PLAIN_TEXT,
        "language": "es"
    }

    sentiment_response = client.analyze_sentiment(
        request={"document": document}
    )

    entities_response = client.analyze_entities(
        request={"document": document}
    )

    return {
        "sentiment": sentiment_response.document_sentiment,
        "entities": entities_response.entities
    }