const Navbar = () => {
  return (
    <nav className="bg-gray-900 text-white shadow-md fixed top-0 left-0 w-screen z-50">
      <div className="px-6 flex justify-between items-center h-16">
        {/* Logo */}
        <div className="flex items-center">
          <h1 className="text-2xl font-bold text-blue-400">E.V.A 2.0</h1>
        </div>

        {/* Navigation Links */}
        <div className="flex space-x-8 text-sm sm:text-base">
          <a href="/dashboard" className="hover:text-blue-400 transition-colors">Dashboard</a>
          <a href="/assistant" className="hover:text-blue-400 transition-colors">Assistant</a>
          <a href="/logs" className="hover:text-blue-400 transition-colors">Logs</a>
          <a href="/profile" className="hover:text-blue-400 transition-colors">Profile</a>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
