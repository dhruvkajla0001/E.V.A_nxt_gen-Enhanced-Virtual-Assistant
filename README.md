<!DOCTYPE html>
<html>
<head>
  <title>EVA 2.0 – Enhanced Virtual Assistant</title>
</head>
<body>

  <h1>🤖 EVA 2.0 – Enhanced Virtual Assistant</h1>
  <p>
    EVA is a multimodal AI assistant built with voice, vision, and gesture control. It's designed for natural interaction using FastAPI, Gemini Pro, YOLOv8, and MediaPipe. The frontend (upcoming) will offer a beautiful React.js interface to interact with EVA in real time.
  </p>

  <h2>🚀 Features</h2>
  <ul>
    <li>🎙️ Voice-controlled chatbot using Google Gemini</li>
    <li>🗣️ Text-to-speech with slow-paced female voice</li>
    <li>📷 Object detection using YOLOv8</li>
    <li>✋ Hand gesture detection using MediaPipe</li>
    <li>⚡ Gesture-action mapping (e.g. fist = standby, thumb = scan)</li>
    <li>🧠 EVA introduces herself as a true assistant (not an LLM)</li>
  </ul>

  <h2>🧠 Backend Tech Stack</h2>
  <ul>
    <li>FastAPI (Python)</li>
    <li>Google Generative AI SDK (Gemini)</li>
    <li>SpeechRecognition, PyAudio, pyttsx3</li>
    <li>YOLOv8 (Ultralytics), OpenCV</li>
    <li>MediaPipe for gesture detection</li>
    <li>LangChain + OpenAI (optional fallback)</li>
  </ul>

  <h2>🎨 Frontend Roadmap (React.js)</h2>
  <ul>
    <li>🧑‍💻 EVA Chat UI with real-time response rendering</li>
    <li>🎤 Mic button to trigger EVA speech loop</li>
    <li>📷 Webcam stream panel for gesture + object feedback</li>
    <li>🖐️ Overlay that displays detected gesture + action</li>
    <li>🧩 API status and logs dashboard</li>
    <li>🌗 Dark mode toggle</li>
  </ul>

  <h2>📦 Installation</h2>
  <pre>
git clone https://github.com/dhruvkajla/eva-2.0.git
cd eva-2.0
pip install -r requirements.txt
  </pre>

  <h2>🔐 .env File (Gemini API)</h2>
  <pre>
GOOGLE_API_KEY=your_gemini_api_key_here
  </pre>

  <h2>▶️ Running EVA Backend</h2>
  <pre>python app.py</pre>
  <p>Visit: <code>http://localhost:8000/docs</code> for Swagger UI</p>

  <h2>📮 API Endpoints</h2>
  <ul>
    <li><code>GET /assistant/run</code> – Voice in → Gemini → Speak back</li>
    <li><code>GET /assistant/gesture</code> – Detect gesture only</li>
    <li><code>GET /assistant/gesture-action</code> – Detect gesture and trigger mapped action</li>
    <li><code>GET /assistant/detect-objects</code> – Detect objects from webcam</li>
  </ul>

  <h2>📁 Project Structure</h2>
  <pre>
eva-2.0/
│
├── app.py
├── requirements.txt
├── README.html
│
└── server/
    └── app/
        ├── api/
        │   ├── assistant_routes.py
        │   └── gesture_routes.py
        │
        ├── services/
        │   ├── chatbot_services.py
        │   ├── text_to_speech_service.py
        │   ├── speech_recognition_service.py
        │   ├── object_detection_service.py
        │   └── gesture_detection_service.py
  </pre>

  <h2>📌 Future Add-ons</h2>
  <ul>
    <li>🏠 Smart home device controls (lights, fans, etc)</li>
    <li>📊 Voice command history with timestamps</li>
    <li>📁 File summarizer using Gemini (upload + answer)</li>
    <li>📞 Face recognition + calling system integration</li>
    <li>🧩 Plugin system to extend EVA modules (AI doctor, AI tutor, etc)</li>
  </ul>

  <p><strong>👨‍💻 Built with love by Dhruv Kajla , Mukund Malik , Vipan Kumar, Aakash Yadav
  </strong></p>

</body>
</html>
