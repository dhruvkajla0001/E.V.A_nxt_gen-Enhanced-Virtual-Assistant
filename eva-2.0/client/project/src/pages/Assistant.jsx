import { useState } from "react";
import { Send, Mic, Camera, Hand } from "lucide-react"; 
import { runAssistant } from "../api/assistant";

const Assistant = () => {
  const [messages, setMessages] = useState([
    { sender: "assistant", text: "Hello! I’m E.V.A 2.0. How can I assist you today?" }
  ]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSend = async () => {
    if (!input.trim()) return;

    const userMessage = { sender: "user", text: input };
    setMessages((prev) => [...prev, userMessage]);
    setInput("");
    setLoading(true);

    try {
      const response = await runAssistant(input);
      const { reply, trigger, detected, gesture } = response;

      let assistantText = reply;

      if (trigger === "vision" && detected) {
        assistantText += `\n[Vision Mode] Objects detected: ${detected || "None"}`;
      }
      if (trigger === "gesture" && gesture) {
        assistantText += `\n[Gesture Mode] Detected gesture: ${gesture}`;
      }

      setMessages((prev) => [
        ...prev,
        {
          sender: "assistant",
          text: assistantText,
          trigger,
        }
      ]);
    } catch (err) {
      setMessages((prev) => [
        ...prev,
        { sender: "assistant", text: "Error: EVA could not respond." }
      ]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex flex-col justify-between min-h-screen bg-gray-950 text-white p-6">
      {/* Chat Window */}
      <div className="flex-1 overflow-y-auto space-y-4 mb-4 bg-gray-900 p-4 rounded-lg shadow-inner">
        {messages.map((msg, idx) => (
          <div
            key={idx}
            className={`flex ${msg.sender === "user" ? "justify-end" : "justify-start"}`}
          >
            <div
              className={`max-w-xs px-4 py-2 rounded-lg text-sm whitespace-pre-line ${
                msg.sender === "user"
                  ? "bg-blue-500 text-white"
                  : "bg-gray-700 text-gray-100"
              }`}
            >
              {/* Add icons for Vision & Gesture */}
              {msg.trigger === "vision" && (
                <span className="flex items-center mb-1 text-sm text-blue-300">
                  <Camera className="w-4 h-4 mr-1" /> Vision Mode Active
                </span>
              )}
              {msg.trigger === "gesture" && (
                <span className="flex items-center mb-1 text-sm text-green-300">
                  <Hand className="w-4 h-4 mr-1" /> Gesture Mode Active
                </span>
              )}
              {msg.text}
            </div>
          </div>
        ))}

        {loading && (
          <div className="text-gray-400 text-sm italic">E.V.A is thinking...</div>
        )}
      </div>

      {/* Input Area */}
      <div className="flex items-center space-x-3 bg-gray-800 p-3 rounded-lg shadow-lg">
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && handleSend()}
          placeholder="Type your message (e.g., 'look around' or 'look at my hand')..."
          className="flex-1 p-2 rounded-lg bg-gray-900 text-white border border-gray-700 focus:outline-none focus:border-blue-400"
        />
        <button
          onClick={handleSend}
          className="p-2 bg-blue-500 hover:bg-blue-600 rounded-lg transition-colors"
          disabled={loading}
        >
          <Send className="w-5 h-5" />
        </button>
        <button
          className="p-2 bg-green-500 hover:bg-green-600 rounded-lg transition-colors"
          title="Voice Input (Coming Soon)"
        >
          <Mic className="w-5 h-5" />
        </button>
      </div>
    </div>
  );
};

export default Assistant;
