import { useState, useRef } from "react";
import { Mic, Camera, Hand } from "lucide-react";
import { runAssistant } from "../api/assistant";

const Assistant = () => {
  const [listening, setListening] = useState(false);
  const [status, setStatus] = useState("Tap the mic to speak");
  const recognitionRef = useRef(null);
  const synthRef = useRef(window.speechSynthesis);

  const initRecognition = () => {
    const SpeechRecognition =
      window.SpeechRecognition || window.webkitSpeechRecognition;

    if (!SpeechRecognition) {
      alert("Your browser does not support speech recognition.");
      return null;
    }

    const recognition = new SpeechRecognition();
    recognition.lang = "en-US";
    recognition.continuous = false;
    recognition.interimResults = false;
    return recognition;
  };

  const startListening = () => {
    if (!recognitionRef.current) {
      recognitionRef.current = initRecognition();
    }
    const recognition = recognitionRef.current;
    if (!recognition) return;

    setStatus("Listening...");
    setListening(true);
    recognition.start();

    recognition.onresult = async (event) => {
      const transcript = event.results[0][0].transcript;
      setStatus(`Heard: "${transcript}"`);
      setListening(false);

      // Send transcript to EVA backend
      const response = await runAssistant(transcript);
      const { reply, trigger, detected, gesture } = response;

      let finalResponse = reply;
      if (trigger === "vision" && detected) {
        finalResponse += ` Objects detected: ${detected || "None"}.`;
      }
      if (trigger === "gesture" && gesture) {
        finalResponse += ` Detected gesture: ${gesture}.`;
      }

      speakResponse(finalResponse);
    };

    recognition.onerror = (event) => {
      console.error("Speech recognition error:", event.error);
      setStatus("Error: " + event.error);
      setListening(false);
    };

    recognition.onend = () => {
      if (listening) {
        recognition.start(); // Auto-restart if user keeps mic on
      } else {
        setStatus("Tap the mic to speak");
      }
    };
  };

  const stopListening = () => {
    if (recognitionRef.current) {
      recognitionRef.current.stop();
    }
    setListening(false);
    setStatus("Mic stopped");
  };

  const speakResponse = (text) => {
    if (synthRef.current.speaking) {
      synthRef.current.cancel();
    }
    const utterance = new SpeechSynthesisUtterance(text);
    utterance.lang = "en-US";
    synthRef.current.speak(utterance);
  };

  return (
    <div className="flex flex-col justify-center items-center min-h-screen bg-gray-950 text-white p-6">
      <div className="text-lg mb-4">{status}</div>

      {/* Mic Button */}
      <button
        onClick={() => (listening ? stopListening() : startListening())}
        className={`p-6 rounded-full transition-colors shadow-lg ${
          listening ? "bg-red-500 animate-pulse" : "bg-green-500 hover:bg-green-600"
        }`}
      >
        <Mic className="w-8 h-8" />
      </button>

      <div className="mt-6 text-sm text-gray-400">
        EVA 2.0 Voice Assistant is {listening ? "listening..." : "idle"}.
      </div>
    </div>
  );
};

export default Assistant;
