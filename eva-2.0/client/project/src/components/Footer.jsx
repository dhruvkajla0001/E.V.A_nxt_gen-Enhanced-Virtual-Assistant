const Footer = () => {
  return (
    <footer className="bg-gray-900 text-gray-300 py-4 mt-6">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <p className="text-sm">
          © {new Date().getFullYear()} E.V.A 2.0. All Rights Reserved.
        </p>
        <p className="text-xs mt-1">
          Built with ❤️ using React, Tailwind, and AI-powered tech.
        </p>
      </div>
    </footer>
  );
};

export default Footer;
