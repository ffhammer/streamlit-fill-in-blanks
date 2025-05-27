import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  base: "./", // Important for relative paths in the build
  server: { // Add this
    port: 3001,
  },
  build: {
    outDir: 'dist', // Output to 'dist' folder
    rollupOptions: {
      output: {
        entryFileNames: `assets/[name].js`, // No hash in dev, hash in prod by default
        chunkFileNames: `assets/[name].js`,
        assetFileNames: `assets/[name].[ext]`
      }
    }
  }
})