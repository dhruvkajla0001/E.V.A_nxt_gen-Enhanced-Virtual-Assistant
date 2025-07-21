import { createContext, useContext, useState, useEffect } from "react";
import { loginUser, registerUser, getProfile, logoutUser } from "../api/auth";

const AuthContext = createContext();

export const useAuth = () => useContext(AuthContext);

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  // Check token & load profile on app start
  useEffect(() => {
    const token = localStorage.getItem("authToken");
    if (token) {
      const profile = getProfile();
      setUser(profile);
    } else {
      setUser(null); // No token = not logged in
    }
    setLoading(false);
  }, []);

  const login = async (email, password) => {
    const res = await loginUser(email, password);
    setUser(getProfile());
    return res;
  };

  const register = async (username, email, password) => {
    return await registerUser(username, email, password);
  };

  const logout = () => {
    logoutUser();
    setUser(null);
  };

  const value = {
    user,
    isAuthenticated: !!(user && localStorage.getItem("authToken")), // Only true if token exists
    login,
    register,
    logout,
  };

  if (loading) {
    return <div className="flex justify-center items-center h-screen">Loading...</div>;
  }

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
};
