from dotenv import load_dotenv
#Como no se me cargaba bien el .env usando esto ya no tengo problema
load_dotenv()

from flask import Flask, request, render_template

from services.nlp_service import analyze_text
from services.speech_service import transcribe_audio
from services.vision_service import analyze_image
from services.formatter import format_nlp_result

import os

app = Flask(__name__)
#folder con los contenidos de prueba
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Ruta raiz
@app.route("/")
def home():
    return render_template("index.html")

# texto -----------------------
@app.route("/analyze-text", methods=["POST"])
def analyze_text_route():
    user_text = request.form.get("text")

    analysis = analyze_text(user_text)
    report = format_nlp_result(user_text, analysis)

    return render_template("dashboard.html", report=report)
# texto -----------------------
# audio -----------------------
@app.route("/analyze-audio", methods=["POST"])
def analyze_audio_route():
    audio_file = request.files["audio"]
    audio_path = os.path.join(UPLOAD_FOLDER, audio_file.filename)
    audio_file.save(audio_path)

    transcript = transcribe_audio(audio_path)
    analysis = analyze_text(transcript)

    report = format_nlp_result(transcript, analysis)
    report["input"]["tipo"] = "audio"
    report["input"]["archivo"] = audio_file.filename
    report["transcripcion"] = transcript

    return render_template("dashboard.html", report=report)
# audio -----------------------
# imagen -----------------------
@app.route("/analyze-image", methods=["POST"])
def analyze_image_route():
    image_file = request.files["image"]
    image_path = os.path.join(UPLOAD_FOLDER, image_file.filename)
    image_file.save(image_path)

    vision_result = analyze_image(image_path)

    report = {
        "input": {
            "tipo": "imagen",
            "archivo": image_file.filename
        },
        "faces": vision_result["faces"],
        "objects": vision_result["objects"],
        "labels": vision_result["labels"]
    }

    return render_template("dashboard.html", report=report)
# imagen -----------------------

#Fask necesita que esta parte de cordigo este aqui sino no muestra lo que haya detrás
if __name__ == "__main__":
    app.run(debug=True)




