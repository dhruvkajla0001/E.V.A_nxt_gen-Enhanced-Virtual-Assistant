import pyttsx3

def speak_text(text: str):
    try:
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')

        # Set female voice if available
        for voice in voices:
            if 'female' in voice.name.lower() or 'zira' in voice.name.lower():
                engine.setProperty('voice', voice.id)
                break
        engine.setProperty('rate', 145)  # Try 120–160 range for slower speed    

        engine.say(text)
        engine.runAndWait()
        return {"status": "spoken", "text": text}
    except Exception as e:
        return {"error": str(e)}
