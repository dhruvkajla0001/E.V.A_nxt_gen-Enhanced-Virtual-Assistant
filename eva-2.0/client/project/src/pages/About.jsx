const About = () => {
  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-900 via-black to-gray-900 text-white flex flex-col items-center px-6 py-12">
      {/* Title */}
      <h1 className="text-5xl font-extrabold bg-gradient-to-r from-blue-400 via-purple-500 to-pink-500 text-transparent bg-clip-text animate-pulse drop-shadow-lg text-center">
        About E.V.A 2.0
      </h1>

      <p className="text-gray-400 text-center max-w-2xl mt-6 text-lg">
        E.V.A 2.0 (Enhanced Virtual Assistant) is a next-generation AI-powered assistant, 
        designed to help you interact with technology through natural language, 
        vision, and gestures — all in one seamless experience.
      </p>

      {/* Features Section */}
      <div className="mt-12 grid gap-6 md:grid-cols-3 w-full max-w-5xl">
        {/* Assistant */}
        <div className="bg-gray-800 rounded-2xl shadow-xl p-6 hover:shadow-2xl hover:scale-105 transform transition-all duration-300">
          <h2 className="text-xl font-bold text-blue-400">Conversational AI</h2>
          <p className="text-gray-300 mt-3">
            EVA communicates through chat and speech, offering answers, task automation, and smart responses.
          </p>
        </div>

        {/* Object Detection */}
        <div className="bg-gradient-to-r from-blue-500 to-purple-600 rounded-2xl shadow-xl p-6 hover:shadow-2xl hover:scale-105 transform transition-all duration-300">
          <h2 className="text-xl font-bold">Computer Vision</h2>
          <p className="text-gray-200 mt-3">
            Real-time detection using YOLOv8 for tracking people, objects, and suspicious activity.
          </p>
        </div>

        {/* Gesture Recognition */}
        <div className="bg-gradient-to-r from-purple-500 to-pink-500 rounded-2xl shadow-xl p-6 hover:shadow-2xl hover:scale-105 transform transition-all duration-300">
          <h2 className="text-xl font-bold">Gesture Controls</h2>
          <p className="text-gray-200 mt-3">
            Control EVA with hand gestures using MediaPipe — no need for clicks or typing.
          </p>
        </div>
      </div>

      {/* Footer Info */}
      <div className="mt-12 text-center text-gray-400">
        <p className="text-sm">
          Version 2.0 • Powered by React, TailwindCSS, YOLOv8, and AI APIs
        </p>
        <p className="text-sm mt-1">Created by Team EVA</p>
      </div>
    </div>
  );
};

export default About;
