import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
import './index.css'; // If you have global styles
import StreamlitComponentEntryPoint from './components.jsx'; // This is your MyComponent

const rootElement = document.getElementById('root');
if (rootElement) {
  createRoot(rootElement).render(
    <StrictMode>
      <StreamlitComponentEntryPoint />
    </StrictMode>,
  );
} else {
  console.error("Failed to find the root element");
}