from google.cloud import speech_v1 as speech

def transcribe_audio(audio_path):
    client = speech.SpeechClient()

    with open(audio_path, "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)
#He estado investigando un error que estaba teniendo con la API de google,
#la frecuencia si esta a 16000hrz funciona mucho mejor, ademas de que el archivo 
#tiene que ser .WAV (No vale la grabadora de windows, he usado un transformador online)
#https://www.online-convert.com/result#j=c46bdfbb-09b8-4593-9cb1-90f30b5223c1
#Y tambien tiene que ser de 1 canal, es decir mono no estereo
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        language_code="es-ES"
    )

    response = client.recognize(config=config, audio=audio)

    transcript = ""
    for result in response.results:
        transcript += result.alternatives[0].transcript

    return transcript