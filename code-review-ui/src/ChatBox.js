import React, { useState } from 'react';
import axios from 'axios';
import './ChatBox.css';

function ChatBox() {
  const [messages, setMessages] = useState([
    { sender: 'PCR', text: "Hi there! I'm your personal code reviewer" }
  ]);
  const [input, setInput] = useState('');

  const handleSend = async () => {
    if (!input.trim()) return;

    // Add user's message
    const newMessage = { sender: 'user', text: input };
    setMessages(prev => [...prev, newMessage]);

    try {
      // Send code to Flask backend
      const response = await axios.post('http://localhost:5000/api/message', { code: input });


      // Choose between 'reply' or 'optimized_code' depending on backend
      const aiText = response.data.optimized_code || response.data.reply || "No response from AI.";

      const aiMessage = { sender: 'ai', text: aiText };
      setMessages(prev => [...prev, aiMessage]);
    } catch (error) {
      console.error('Error sending message:', error);
      setMessages(prev => [
        ...prev,
        { sender: 'ai', text: "Oops! Something went wrong." }
      ]);
    }

    // Clear input
    setInput('');
  };

  return (
    <div className="chat-container">
      <div className="header">AI Code Reviewer</div>
      <div className="chat-box">
        {messages.map((msg, idx) => (
          <div key={idx} className={`message ${msg.sender}`}>
            {msg.text}
          </div>
        ))}
      </div>
      <div className="input-box">
        <input
          type="text"
          placeholder="Type your code here..."
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={(e) => e.key === 'Enter' && handleSend()}
        />
        <button onClick={handleSend}>🔼</button>
      </div>
    </div>
  );
}

export default ChatBox;
