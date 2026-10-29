import '../App.css';
import React, { useState } from 'react';
import api from '../API';

export default function Theraphist() {  
    const [input, setInput] = useState('');
    const [messages, setMessages] = useState([]);

    async function get_Bot(userInput) {
        try {   
            let response = await api.get(`/chat/therapist?input=${userInput}`);
            return response.data; 
        } catch (error) {
            console.error("API Error:", error);
            return "Server error.";
        }
    }

    async function handle(e) {
        e.preventDefault();
        
        if (!input.trim()) return;

        const currentInput = input;
        setMessages((prev) => [...prev, { role: 'user', content: currentInput }]);
        setInput('');
        setTimeout(async () => {
            const botReply = await get_Bot(currentInput);

            setMessages((prev) => [
              ...prev,
              { role: 'bot', content: botReply }
            ]);
        }, 800);
    }

    return (
        <>
            <div className="header">Brutally Honest Theraphist</div>
            <div className="chat-area">
                {messages.map((msg, index) => (
                    <div key={index} className={`bubble ${msg.role}`}>
                        {msg.content}
                    </div>
                ))}
            </div>
            <form id="footer" onSubmit={handle}>
                <input 
                    type="text" 
                    id="input-box" 
                    placeholder="Type a message" 
                    onChange={e => setInput(e.target.value)} 
                    value={input}
                />
                <button type="submit" className="send-btn">➔</button>
            </form>
        </>
    );
}