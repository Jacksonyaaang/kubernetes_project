import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [data, setData] = useState("");

  useEffect(() => {
      fetch("http://localhost:8000/api/data")
          .then(response => response.json())
        .then(data => setData(data.data));
  }, []);

  return (
      <div className="App">
        <header className="App-header">
          {data}
        </header>
      </div>
  );
}

export default App;
