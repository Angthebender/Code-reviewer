'use client';  // This line marks the file as a client component
import React, { useState } from "react";
import axios from "axios";
import "./CodeChat.css"; // Make sure this exists for styling

const CodeChat = () => {
  const [code, setCode] = useState("");  // To store user input
  const [history, setHistory] = useState<{ message: string; response: string }[]>([]);  // To store chat history

  // Update code input state
  const handleInputChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setCode(event.target.value);
  };

  // Submit the code for optimization
  const handleSubmit = async () => {
    if (code) {
      try {
        // Make the POST request to the Flask backend for code optimization
        const response = await axios.post('http://127.0.0.1:5000/optimize', { code });

        // Get optimized code from the backend response
        const optimizedCode = response.data.optimized_code;

        // Update the history state to display both original and optimized code
        setHistory([
          ...history,
          { message: code, response: optimizedCode },
        ]);
        setCode(""); // Clear the input field after submission
      } catch (error) {
        console.error("Error during optimization:", error);
      }
    }
  };

  return (
    <div className="chat-container">
      {/* Display chat history */}
      <div className="chat-history">
        {history.map((item, index) => (
          <div key={index} className="chat-entry">
            <div className="chat-message">
              <strong>Code:</strong> {item.message}
            </div>
            <div className="chat-message">
              <strong>Optimized Code:</strong> {item.response}
            </div>
          </div>
        ))}
      </div>

      {/* Input section */}
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

export default CodeChat;
