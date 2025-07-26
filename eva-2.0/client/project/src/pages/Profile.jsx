import { useState } from "react";
import { useAuth } from "../context/AuthContext";
import axios from "axios";

const Profile = () => {
  const { user } = useAuth();
  const [username, setUsername] = useState(user?.username || "");
  const [email, setEmail] = useState(user?.email || "");
  const [status, setStatus] = useState("");

  const handleUpdate = async (e) => {
    e.preventDefault();
    setStatus("Updating...");

    try {
      // Update API (adjust endpoint based on your backend)
      const res = await axios.put("http://localhost:8000/profile/update", {
        username,
        email,
      });

      if (res.status === 200) {
        setStatus("Profile updated successfully!");
      } else {
        setStatus("Update failed. Try again.");
      }
    } catch (error) {
      setStatus("Error updating profile.");
    }
  };

  return (
    <div className="flex flex-col justify-center items-center min-h-screen bg-gradient-to-br from-gray-900 via-black to-gray-900 px-6 text-white">
      <div className="bg-gray-800 rounded-2xl shadow-xl p-8 max-w-lg w-full">
        <h1 className="text-4xl font-bold text-blue-400 text-center mb-6">My Profile</h1>

        <form onSubmit={handleUpdate} className="space-y-4">
          {/* Username */}
          <div>
            <label className="block text-gray-300 mb-1">Username</label>
            <input
              type="text"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              className="w-full p-3 rounded-lg bg-gray-900 text-white border border-gray-700 focus:outline-none focus:border-blue-400"
            />
          </div>

          {/* Email */}
          <div>
            <label className="block text-gray-300 mb-1">Email</label>
            <input
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              className="w-full p-3 rounded-lg bg-gray-900 text-white border border-gray-700 focus:outline-none focus:border-blue-400"
            />
          </div>

          {/* Update Button */}
          <button
            type="submit"
            className="w-full bg-blue-500 hover:bg-blue-600 text-white font-semibold py-3 px-4 rounded-lg transition-all shadow-md hover:shadow-xl"
          >
            Update Profile
          </button>
        </form>

        {status && <p className="mt-4 text-center text-gray-300">{status}</p>}
      </div>
    </div>
  );
};

export default Profile;
