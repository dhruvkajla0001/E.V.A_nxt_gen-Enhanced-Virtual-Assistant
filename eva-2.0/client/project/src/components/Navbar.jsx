import { useState } from "react";
import { Menu, X } from "lucide-react"; // For menu toggle icon (mobile)

const Navbar = () => {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <nav className="bg-gray-900 text-white shadow-md">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between items-center h-16">
          {/* Logo */}
          <div className="flex items-center">
            <h1 className="text-xl font-bold text-blue-400">E.V.A 2.0</h1>
          </div>

          {/* Desktop Menu */}
          <div className="hidden md:flex space-x-6">
            <a href="/dashboard" className="hover:text-blue-400">Dashboard</a>
            <a href="/assistant" className="hover:text-blue-400">Assistant</a>
            <a href="/logs" className="hover:text-blue-400">Logs</a>
            <a href="/profile" className="hover:text-blue-400">Profile</a>
          </div>

          {/* Mobile Menu Toggle */}
          <div className="md:hidden flex items-center">
            <button onClick={() => setIsOpen(!isOpen)} className="focus:outline-none">
              {isOpen ? <X size={24} /> : <Menu size={24} />}
            </button>
          </div>
        </div>
      </div>

      {/* Mobile Dropdown Menu */}
      {isOpen && (
        <div className="md:hidden bg-gray-800 px-4 py-3 space-y-2">
          <a href="/dashboard" className="block hover:text-blue-400">Dashboard</a>
          <a href="/assistant" className="block hover:text-blue-400">Assistant</a>
          <a href="/logs" className="block hover:text-blue-400">Logs</a>
          <a href="/profile" className="block hover:text-blue-400">Profile</a>
        </div>
      )}
    </nav>
  );
};

export default Navbar;
