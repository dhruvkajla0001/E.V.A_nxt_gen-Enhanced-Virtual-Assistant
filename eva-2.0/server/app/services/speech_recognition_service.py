# server/app/services/speech_recognition_service.py

import speech_recognition as sr

def transcribe_from_mic():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("🎤 Speak now...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        return {"transcription": text}
    except sr.UnknownValueError:
        return {"error": "Could not understand audio."}
    except sr.RequestError as e:
        return {"error": f"Google Speech API error: {str(e)}"}
