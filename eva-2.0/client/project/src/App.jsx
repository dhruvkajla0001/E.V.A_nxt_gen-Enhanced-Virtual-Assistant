import Navbar from "./components/Navbar";
import Footer from "./components/Footer";

function App() {
  return (
    <div className="flex flex-col min-h-screen">
      <Navbar />
      <main className="flex-grow p-6"> {/* Page content goes here */}</main>
      <Footer />
    </div>
  );
}

export default App;
