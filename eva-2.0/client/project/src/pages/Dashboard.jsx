import { useAuth } from "../context/AuthContext";

const Dashboard = () => {
  const { user, logout } = useAuth();

  return (
    <div className="flex flex-col justify-center items-center min-h-screen bg-gray-50 px-4">
      <div className="bg-white shadow-lg rounded-lg p-8 max-w-lg w-full text-center">
        <h1 className="text-3xl font-bold text-gray-800">
          Welcome, {user?.username || "User"}!
        </h1>
        {user?.email && (
          <p className="text-gray-600 mt-2">Email: {user.email}</p>
        )}

        <p className="text-lg text-gray-600 mt-4">
          You’re logged in to your E.V.A 2.0 Dashboard.
        </p>

        {/* Logout Button */}
        <button
          onClick={logout}
          className="mt-6 bg-red-500 hover:bg-red-600 text-white px-4 py-2 rounded-lg transition-colors"
        >
          Logout
        </button>
      </div>
    </div>
  );
};

export default Dashboard;
