import { defineConfig } from 'vite'
import tailwindcss from '@tailwindcss/vite'
export default defineConfig({
  plugins: [
    tailwindcss(),
  ],
})
// This Vite configuration file sets up Tailwind CSS for the project.
// It imports the necessary modules and exports a configuration object that includes the Tailwind CSS plugin.