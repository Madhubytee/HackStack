import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [message, setMessage] = useState('Loading...');

  useEffect(() => {
    axios.get('http://localhost:8000/api/health')
      .then(res => setMessage(res.data.message))
      .catch(err => setMessage('Backend not connected'));
  }, []);

  return (
    <div style={{
      maxWidth: '800px',
      margin: '50px auto',
      padding: '20px',
      fontFamily: 'system-ui'
    }}>
      <h1 style={{ color: '#3776ab' }}>Python Stack App</h1>
      <div style={{
        background: '#f0f0f0',
        padding: '20px',
        borderRadius: '8px',
        marginTop: '20px'
      }}>
        <strong>Backend Status:</strong> {message}
      </div>
      <div style={{ marginTop: '30px', color: '#666' }}>
        <p>Frontend: React running on port 3000</p>
        <p>Backend: Python + Flask running on port 8000</p>
        <p>Database: PostgreSQL connected</p>
      </div>
    </div>
  );
}

export default App;
