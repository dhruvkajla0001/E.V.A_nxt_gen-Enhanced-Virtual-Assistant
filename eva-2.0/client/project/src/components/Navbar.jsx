import { useState } from "react";
import { useAuth } from "../context/AuthContext";

const Navbar = () => {
  const [isMenuOpen, setIsMenuOpen] = useState(false);
  const { user, isAuthenticated, logout } = useAuth();

  return (
    <nav className="bg-gray-900 text-white shadow-md w-full fixed top-0 left-0 z-50">
      <div className="px-6 flex justify-between items-center h-16">
        {/* Logo */}
        <h1 className="text-2xl font-bold text-blue-400">E.V.A 2.0</h1>

        {/* Desktop Menu */}
        <div className="hidden md:flex space-x-8 text-sm sm:text-base">
          {isAuthenticated ? (
            <>
              <a href="/dashboard" className="hover:text-blue-400">Dashboard</a>
              <a href="/assistant" className="hover:text-blue-400">Assistant</a>
              <a href="/logs" className="hover:text-blue-400">Logs</a>
              <a href="/profile" className="hover:text-blue-400">Profile</a>
              <span className="text-gray-300">Hi, {user?.username || "User"}</span>
              <button
                onClick={logout}
                className="bg-red-500 hover:bg-red-600 text-white px-3 py-1 rounded-md transition-colors"
              >
                Logout
              </button>
            </>
          ) : (
            <>
              <a href="/login" className="hover:text-blue-400">Login</a>
              <a href="/register" className="hover:text-blue-400">Register</a>
            </>
          )}
        </div>

        {/* Mobile Menu Button */}
        <button
          className="md:hidden text-white"
          onClick={() => setIsMenuOpen(!isMenuOpen)}
        >
          {isMenuOpen ? "✖" : "☰"}
        </button>
      </div>

      {/* Mobile Sidebar */}
      {isMenuOpen && (
        <div className="md:hidden bg-gray-800 w-48 fixed top-16 left-0 h-full p-4 shadow-lg z-40">
          <nav className="flex flex-col space-y-4">
            {isAuthenticated ? (
              <>
                <a href="/dashboard" className="hover:text-blue-400">Dashboard</a>
                <a href="/assistant" className="hover:text-blue-400">Assistant</a>
                <a href="/logs" className="hover:text-blue-400">Logs</a>
                <a href="/profile" className="hover:text-blue-400">Profile</a>
                <span className="text-gray-300 mt-2">Hi, {user?.username || "User"}</span>
                <button
                  onClick={() => {
                    logout();
                    setIsMenuOpen(false);
                  }}
                  className="mt-4 bg-red-500 hover:bg-red-600 text-white px-3 py-1 rounded-md transition-colors"
                >
                  Logout
                </button>
              </>
            ) : (
              <>
                <a href="/login" className="hover:text-blue-400">Login</a>
                <a href="/register" className="hover:text-blue-400">Register</a>
              </>
            )}
          </nav>
        </div>
      )}
    </nav>
  );
};

export default Navbar;
