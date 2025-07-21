// import { useState } from "react";
// import { Menu, X } from "lucide-react"; // Icons (install with: npm install lucide-react)

// const Sidebar = () => {
//   const [isOpen, setIsOpen] = useState(true);

//   return (
//     <div className="flex">
//       {/* Sidebar */}
//       <div
//         className={`bg-gray-800 text-gray-200 h-screen p-5 pt-20 fixed top-0 left-0 transition-all duration-300 z-40
//         ${isOpen ? "w-60" : "w-16"}`}
//       >
//         {/* Toggle Button */}
//         <button
//           onClick={() => setIsOpen(!isOpen)}
//           className="absolute top-4 right-4 text-gray-300 hover:text-white"
//         >
//           {isOpen ? <X size={20} /> : <Menu size={20} />}
//         </button>

//         {/* Menu Items */}
//         <nav className="mt-6 space-y-4">
//           <a href="/dashboard" className="block hover:text-blue-400">🏠 {isOpen && "Dashboard"}</a>
//           <a href="/assistant" className="block hover:text-blue-400">🤖 {isOpen && "Assistant"}</a>
//           <a href="/object-detection" className="block hover:text-blue-400">📷 {isOpen && "Object Detection"}</a>
//           <a href="/gesture-detection" className="block hover:text-blue-400">✋ {isOpen && "Gesture Detection"}</a>
//           <a href="/logs" className="block hover:text-blue-400">📜 {isOpen && "Logs"}</a>
//           <a href="/health-monitor" className="block hover:text-blue-400">❤️ {isOpen && "Health Monitor"}</a>
//           <a href="/profile" className="block hover:text-blue-400">👤 {isOpen && "Profile"}</a>
//         </nav>
//       </div>

//       {/* Main Content Placeholder (shifts based on sidebar width) */}
//       <div className={`flex-1 ml-${isOpen ? "60" : "16"} p-6 mt-16`}>
//         <h2 className="text-xl font-semibold">Main Dashboard Area</h2>
//         <p className="mt-2 text-gray-600">Your main content will appear here.</p>
//       </div>
//     </div>
//   );
// };

// export default Sidebar;
