import { BrowserRouter as Router, Routes, Route, Navigate } from "react-router-dom";
import Navbar from "./components/Navbar";
import Footer from "./components/Footer";
import Login from "./pages/Login";
import Register from "./pages/Register";
import Dashboard from "./pages/Dashboard";
import Assistant from "./pages/Assistant";
import ProtectedRoute from "./components/Protectedroutes";

function App() {
  return (
    <Router>
      <div className="flex flex-col min-h-screen">
        {/* Navbar stays on all pages */}
        <Navbar />

        {/* Page Content */}
        <div className="flex-grow pt-16"> {/* pt-16 avoids overlap with fixed Navbar */}
          <Routes>
            {/* Public Routes */}
            <Route path="/login" element={<Login />} />
            <Route path="/register" element={<Register />} />

            {/* Protected Routes */}
            <Route
              path="/dashboard"
              element={
                <ProtectedRoute>
                  <Dashboard />
                </ProtectedRoute>
              }
            />
            <Route
              path="/assistant"
              element={
                <ProtectedRoute>
                  <Assistant />
                </ProtectedRoute>
              }
            />

            {/* Redirect unknown routes to login */}
            <Route path="*" element={<Navigate to="/login" replace />} />
          </Routes>
        </div>

        {/* Footer stays on all pages */}
        <Footer />
      </div>
    </Router>
  );
}

export default App;
