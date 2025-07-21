const Footer = () => {
  return (
    <footer className="bg-gray-900 text-gray-400 py-4 w-full mt-auto">
      <div className="px-6 flex flex-col sm:flex-row justify-between items-center">
        <p className="text-sm">
          © {new Date().getFullYear()} E.V.A 2.0. All rights reserved.
        </p>
        <p className="text-xs mt-2 sm:mt-0">
          Powered by AI · Built with React & Tailwind
        </p>
      </div>
    </footer>
  );
};

export default Footer;
