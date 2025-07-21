import axios from "axios";

// Configure Axios with your backend base URL
const API = axios.create({
  baseURL: "http://localhost:8000", // Update this if your backend runs elsewhere
});

// Attach the token to every request if it exists
API.interceptors.request.use((config) => {
  const token = localStorage.getItem("authToken");
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

// --- AUTH FUNCTIONS ---

/**
 * Register a new user
 * @param {string} username
 * @param {string} email
 * @param {string} password
 */
export const registerUser = async (username, email, password) => {
  const { data } = await API.post("/auth/register", {
    username,
    email,
    password,
  });
  return data;
};

/**
 * Login a user and store the token
 * @param {string} email
 * @param {string} password
 */
export const loginUser = async (email, password) => {
  const { data } = await API.post("/auth/login", { email, password });

  // Save JWT token if present
  if (data?.access_token) {
    localStorage.setItem("authToken", data.access_token);

    // Save username/email for display (optional)
    if (data?.user) {
      localStorage.setItem("username", data.user.username || "");
      localStorage.setItem("email", data.user.email || email);
    }
  }

  return data;
};

/**
 * Fetch the stored username (since no /profile endpoint exists)
 */
export const getProfile = () => {
  return {
    username: localStorage.getItem("username") || "User",
    email: localStorage.getItem("email") || "",
  };
};

/**
 * Logout and clear local storage
 */
export const logoutUser = () => {
  localStorage.removeItem("authToken");
  localStorage.removeItem("username");
  localStorage.removeItem("email");
};
