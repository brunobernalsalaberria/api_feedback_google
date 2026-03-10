Sistema de Análisis Multimodal de Feedback

Proyecto desarrollado en Python con Flask,
permite analizar feedback de usuarios en texto, audio e imágenes,
utilizando APIs de Google Cloud para interpretar texto, pasar de audio a texto y interpretar imágenes.

El objetivo es visualizar un dashboard
web mostrando información clave como sentimiento, emociones, entidades,
transcripciones y detección visual.

Funcionalidades
1. Recepción Multimodal

La aplicación acepta tres tipos de entrada:

Texto: reseñas escritas por usuarios

Audio: archivos de voz (.wav, mono, 16kHz) Sino dará errores, 
hay un enlace comentado de una página en la que puedes dar 
esas caracteristicas a cualquier audio

Imagen: fotos con personas y objetos

2. Procesamiento con APIs de Google Cloud
Análisis de Texto (Google Natural Language API)

Sentimiento: positivo / negativo / neutral

Intensidad emocional

Extracción de entidades:
-Productos
-Características
-Problemas

Categoria automática de la reseña

Recomendación automática



Audio → Texto (Google Speech-to-Text)

Transcripción automática del audio

El texto transcrito se analiza con NLP

⚠️ Requisitos del audio ⚠️:

Formato .wav

1 canal (mono)

Frecuencia recomendada: 16000 Hz



Análisis de Imágenes (Google Vision API)

Detección de rostros

Análisis de emociones faciales (alegría, enfado, sorpresa, tristeza)

Detección de objetos

Etiquetas de la imagen



3. Dashboard Web

El dashboard muestra los datos según el tipo de entrada:

Resumen de datos

Tipo de entrada (texto / audio / imagen)

Sentimiento predominante

Score e intensidad


Análisis Detallado

Emociones detectadas

Entidades extraídas

Categoría de la reseña

Recomendación automática



Tecnologías Utilizadas

Backend: Python, Flask

Frontend: HTML + CSS

APIs Cloud:

Google Natural Language API

Google Speech-to-Text API

Google Vision API

Gestión de credenciales: .env

📂 Estructura del Proyecto
feedback_api_google/
│
├── app.py
├── uploads/
├── templates/
│   ├── index.html
│   └── dashboard.html
│
├── services/
│   ├── nlp_service.py
│   ├── speech_service.py
│   ├── vision_service.py
│   ├── formatter.py
│   └── report_service.py
│
├── .env
├── requirements.txt
└── README.md

Configuración del Proyecto

Crear entorno virtual
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
Instalar dependencias
pip install -r requirements.txt
Configurar credenciales

Crear un archivo .env:

GOOGLE_APPLICATION_CREDENTIALS=path/a/tu/credencial.json

Asegúrate de haber habilitado las APIs necesarias en Google Cloud Console.

Ejecución
python app.py

Accede desde el navegador a:

http://127.0.0.1:5000
Rutas Disponibles

POST /analyze-text

POST /analyze-audio

POST /analyze-image

Cada una procesa el input y renderiza el dashboard con los resultados.


Requisitos Cumplidos del Enunciado

Recepción multimodal

Uso de mínimo 3 APIs cloud

Análisis de sentimiento y emociones

Transcripción de audio

Análisis de imágenes (rostros y objetos)

Extracción de información estructurada

Dashboard visual

Gestión de errores y credenciales