import React, { useState } from 'react';
import axios from 'axios';
import './CodeChat.css'; // If you have specific styles

const Review = () => {
  const [code, setCode] = useState("");
  const [history, setHistory] = useState([]);

  const handleInputChange = (event) => {
    setCode(event.target.value);
  };

  const handleSubmit = async () => {
    if (code) {
      try {
        // Sending the code to the Flask backend for optimization
        const response = await axios.post('http://127.0.0.1:5000/optimize', { code });

        // Assuming the Flask response contains the optimized code
        const optimizedCode = response.data.optimized_code;

        // Update history with both original and optimized code
        setHistory([
          ...history,
          { message: code, response: optimizedCode },
        ]);
        setCode(""); // Reset the input box
      } catch (error) {
        console.error("Error during optimization:", error);
      }
    }
  };

  return (
    <div className="chat-container">
      <h1>AI Code Optimizer</h1>
      <div className="chat-history">
        {history.map((item, index) => (
          <div key={index}>
            <div className="chat-message">
              <strong>Code:</strong> {item.message}
            </div>
            <div className="chat-message">
              <strong>Optimized Code:</strong> {item.response}
            </div>
          </div>
        ))}
      </div>

      <div className="text-box-container">
        <input
          type="text"
          value={code}
          onChange={handleInputChange}
          className="text-box"
          placeholder="Write your code here..."
        />
        <button onClick={handleSubmit} className="optimize-button">
          Optimize Code
        </button>
      </div>
    </div>
  );
};

export default Review;
