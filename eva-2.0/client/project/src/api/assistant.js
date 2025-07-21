// src/api/assistant.js
import api from "./axiosInstance";

// Calls EVA backend for chat/vision/gesture processing
export const runAssistant = async (message) => {
  try {
    const response = await api.get('/assistant/run', {
      params: { query: message }, // send as query param (GET)
    });
    return response.data;
  } catch (error) {
    console.error("Assistant API Error:", error);
    throw error;
  }
};
