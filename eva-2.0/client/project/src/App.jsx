import Navbar from "./components/Navbar";
import Footer from "./components/Footer";

function App() {
  return (
    <div className="flex flex-col min-h-screen bg-gray-100">
      <Navbar />
      <main className="flex-grow p-6 mt-16"> {/* Add margin so content is below navbar */}
        <h1 className="text-2xl font-bold">Welcome to EVA 2.0</h1>
      </main>
      <Footer />
    </div>
  );
}

export default App;
