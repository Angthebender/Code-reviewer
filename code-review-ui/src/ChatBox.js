import React, { useState } from 'react';
import axios from 'axios';
import './ChatBox.css';

function ChatBox() {
  const [messages, setMessages] = useState([
    { sender: 'ai', text: "👋 Hey! I'm your AI Code Reviewer. Send me your code!" }
  ]);
  const [input, setInput] = useState('');
  const [isThinking, setIsThinking] = useState(false);

  const handleSend = async () => {
    if (!input.trim()) return;

    setMessages(prev => [...prev, { sender: 'user', text: input }]);
    setIsThinking(true);

    try {
      const res = await axios.post('http://localhost:5000/api/message', { code: input });
      const reply = res.data.optimized_code || "🤖 No response from AI.";
      setMessages(prev => [...prev, { sender: 'ai', text: reply }]);
    } catch (err) {
      setMessages(prev => [...prev, { sender: 'ai', text: "⚠️ Error contacting AI." }]);
    }

    setIsThinking(false);
    setInput('');
  };

  const renderMessage = (msg) => {
    const parts = msg.text.split(/```([\s\S]+?)```/g);
    return parts.map((part, i) =>
      i % 2 === 1 ? (
        <pre key={i} className="code-block"><code>{part}</code></pre>
      ) : (
        <span key={i}>{part}</span>
      )
    );
  };

  return (
    <div className="chat-container">
      <div className="header">💬 AI Code Reviewer</div>
      <div className="chat-box">
        {messages.map((msg, i) => (
          <div key={i} className={`message ${msg.sender}`}>
            {renderMessage(msg)}
          </div>
        ))}
        {isThinking && <div className="thinking">... thinking</div>}
      </div>
      <div className="input-box">
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Paste your code..."
          onKeyDown={(e) => e.key === 'Enter' && handleSend()}
        />
        <button onClick={handleSend}>Send</button>
      </div>
    </div>
  );
}

export default ChatBox;
