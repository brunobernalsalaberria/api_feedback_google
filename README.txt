# Sistema de Análisis Multimodal de Feedback

Proyecto desarrollado en Python con Flask que permite analizar feedback de usuarios en texto, audio e imágenes, utilizando Cloud APIs de Google para interpretar texto, transcribir audio y analizar imágenes.

El objetivo es mostrar un dashboard web con información clave como sentimiento, emociones, entidades, transcripciones y detección visual.

---

## Funcionalidades

### 1. Recepción Multimodal

La aplicación acepta tres tipos de entrada:

- Texto → reseñas escritas por usuarios  
- Audio → archivos de voz (.wav, mono, 16kHz)  
- Imagen → fotos con personas y objetos  

⚠️ Si el audio no cumple el formato dará error.  
Hay un enlace comentado en el código para convertir audios al formato correcto.

---

### 2. Procesamiento con Cloud APIs de Google

#### Análisis de Texto (Google Natural Language API)

- Sentimiento: positivo / negativo / neutral  
- Intensidad emocional  
- Extracción de entidades:
  - Productos
  - Características
  - Problemas
- Categoría automática
- Recomendación automática

---

#### Audio → Texto (Google Speech-to-Text API)

- Transcripción automática
- El texto transcrito se analiza con NLP

⚠️ Requisitos del audio:

- Formato `.wav`
- 1 canal (mono)
- Frecuencia recomendada: 16000 Hz

---

#### Análisis de Imágenes (Google Vision API)

- Detección de rostros
- Emociones faciales:
  - alegría
  - enfado
  - sorpresa
  - tristeza
- Detección de objetos
- Etiquetas de la imagen

---

### 3. Dashboard Web

El dashboard muestra los datos según el tipo de entrada.

#### Resumen

- Tipo de entrada
- Sentimiento predominante
- Score
- Intensidad

#### Análisis detallado

- Emociones detectadas
- Entidades extraídas
- Categoría
- Recomendación automática

---

## Tecnologías utilizadas

Backend:
- Python
- Flask

Frontend:
- HTML
- CSS

Cloud APIs:
- Google Natural Language API
- Google Speech-to-Text API
- Google Vision API

Gestión de credenciales:
- .env

---

## Estructura del proyecto

```
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
```

---

## Configuración del proyecto

### Crear entorno virtual

```
python -m venv venv
source venv/bin/activate
# Windows:
venv\Scripts\activate
```

### Instalar dependencias

```
pip install -r requirements.txt
```

### Configurar credenciales

Crear archivo `.env`

```
GOOGLE_APPLICATION_CREDENTIALS=path/a/tu/credencial.json
```

Asegúrate de habilitar las APIs en Google Cloud Console.

---

## Ejecución

```
python app.py
```

Abrir en el navegador:

```
http://127.0.0.1:5000
```

---

## Rutas disponibles

```
POST /analyze-text
POST /analyze-audio
POST /analyze-image
```

Cada ruta procesa el input y muestra el dashboard.

---

## Requisitos cumplidos

- Recepción multimodal
- Uso de 3 Cloud APIs
- Análisis de sentimiento
- Transcripción de audio
- Análisis de imágenes
- Extracción de información estructurada
- Dashboard visual
- Gestión de credenciales
- Manejo de errores
