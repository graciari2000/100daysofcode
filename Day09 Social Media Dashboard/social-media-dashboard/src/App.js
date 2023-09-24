// src/App.js

import React from 'react';
import AppRouter from './AppRouter'; // Import your router component

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Social Media Dashboard</h1>
      </header>
      <nav>
        {/* Add navigation links here if needed */}
      </nav>
      <main>
        <AppRouter /> {/* Use your router component here */}
      </main>
    </div>
  );
}

export default App;