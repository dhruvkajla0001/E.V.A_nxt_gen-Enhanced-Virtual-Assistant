// src/api/axiosInstance.js
import axios from "axios";

// Set your FastAPI backend URL
const api = axios.create({
  baseURL: "http://127.0.0.1:8000", // Change to your backend URL if needed
  headers: {
    "Content-Type": "application/json",
  },
});

export default api;
