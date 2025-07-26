import { useAuth } from "../context/AuthContext";
import { useNavigate } from "react-router-dom";

const Dashboard = () => {
  const { user, logout } = useAuth();
  const navigate = useNavigate();

  return (
    <div className="flex flex-col justify-center items-center min-h-screen bg-gradient-to-br from-gray-900 via-black to-gray-900 px-6 text-white">
      {/* Heading */}
      <h1 className="text-4xl md:text-5xl font-extrabold bg-gradient-to-r from-blue-400 via-purple-500 to-pink-500 text-transparent bg-clip-text animate-pulse drop-shadow-lg text-center">
        Welcome, {user?.username || "Commander"}!
      </h1>
      {user?.email && (
        <p className="mt-2 text-gray-400 text-lg text-center">{user.email}</p>
      )}

      {/* Action Cards */}
      <div className="mt-10 grid gap-6 md:grid-cols-3 w-full max-w-5xl">
        {/* Profile Info Card */}
        <div className="bg-gray-800 rounded-2xl shadow-xl p-6 hover:shadow-2xl hover:scale-105 transform transition-all duration-300">
          <h2 className="text-xl font-bold text-blue-400">Profile</h2>
          <p className="text-gray-300 mt-3">Username: {user?.username || "User"}</p>
          <p className="text-gray-300">Email: {user?.email || "Not available"}</p>
        </div>

        {/* Assistant Card */}
        <div
          onClick={() => navigate("/assistant")}
          className="bg-gradient-to-r from-blue-500 to-purple-600 rounded-2xl shadow-xl p-6 cursor-pointer hover:shadow-2xl hover:scale-105 transform transition-all duration-300"
        >
          <h2 className="text-xl font-bold">E.V.A Assistant</h2>
          <p className="text-gray-200 mt-3">Chat, ask, and get things done.</p>
        </div>

        {/* Logs Card */}
        <div
          onClick={() => navigate("/logs")}
          className="bg-gradient-to-r from-purple-500 to-pink-500 rounded-2xl shadow-xl p-6 cursor-pointer hover:shadow-2xl hover:scale-105 transform transition-all duration-300"
        >
          <h2 className="text-xl font-bold">Activity Logs</h2>
          <p className="text-gray-200 mt-3">Review all EVA activities.</p>
        </div>
      </div>

      {/* Logout Button */}
      <button
        onClick={logout}
        className="mt-12 px-6 py-3 bg-red-600 hover:bg-red-700 rounded-xl text-lg font-semibold transition-all shadow-md hover:shadow-xl transform hover:scale-110"
      >
        Logout
      </button>
    </div>
  );
};

export default Dashboard;
