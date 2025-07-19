import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { useAuth } from "../context/AuthContext";
import ProtectedRoute from "../components/ProtectedRoute";

// Temporary placeholder pages
const Login = () => <h1 className="text-center mt-10 text-xl">Login Page</h1>;
const Register = () => <h1 className="text-center mt-10 text-xl">Register Page</h1>;
const Dashboard = () => <h1 className="text-center mt-10 text-xl">Dashboard</h1>;

function AppRoutes() {
  return (
    <Router>
      <Routes>
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route
          path="/dashboard"
          element={
            <ProtectedRoute>
              <Dashboard />
            </ProtectedRoute>
          }
        />
      </Routes>
    </Router>
  );
}

export default AppRoutes;
