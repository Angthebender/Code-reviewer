
```markdown
# 🧠 AI Code Reviewer

This is a **React + Flask-based AI Code Reviewer** project powered by **DeepSeek** or other Hugging Face models. It analyzes your code, offers suggestions, and gives optimized versions with helpful comments.

---

## 🔧 Features

- Input any code snippet
- Get feedback from an AI "junior dev"
- See optimized code and friendly suggestions
- React frontend + Flask backend
- Support for Hugging Face models (like DeepSeek, Phi-2, Mistral, etc.)

---

## ⚙️ Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/code-reviewer.git
cd code-reviewer
```

### 2. Set Up Python Backend (Flask)

#### 📦 Install Python dependencies

```bash
pip install -r requirements.txt
```

> If you don’t have `pip`, install Python 3.10+ first.

#### 🛑 Important: Create a `.env` file

In the root directory, create a `.env` file with the following:

```env
DEEPSEEK_API_KEY=your_deepseek_api_key_here
```

> Replace `your_deepseek_api_key_here` with your actual key.  
> You can also use other keys like Hugging Face's `HUGGING_FACE_HUB_TOKEN` depending on which model you're using.

---

### 3. Start the Flask Backend

```bash
python app.py
```

The backend will start on [http://localhost:5000](http://localhost:5000).

---

### 4. Set Up the React Frontend

Go into the frontend directory (e.g., `code-review-ui/`) and run:

```bash
npm install
npm run dev
```

The frontend will open at [http://localhost:5173](http://localhost:5173) (Vite default).

---

## 📂 Folder Structure

```
code-reviewer/
├── app.py               # Flask backend
├── .env                 # Your API keys (not pushed to GitHub)
├── requirements.txt     # Python dependencies
└── code-review-ui/      # React frontend
    ├── src/
    │   └── ChatBox.jsx  # Main chat component
    └── ...
```

---

## 🧠 Supported Models

You can use any LLM model that supports chat-style input:
- `deepseek-chat`
- `microsoft/Phi-2`
- `mistralai/Mistral-7B-Instruct`
- Or any model from Hugging Face (adjust backend accordingly)

---

## 💬 How It Works

The AI receives your code, then responds with:
- Optimized version of your code
- Friendly suggestions and comments (like a helpful junior dev!)
- Markdown-style code formatting

---

## 🛡️ Security

Make sure your `.env` file is **never pushed to GitHub**. It's listed in `.gitignore` for safety.

---

## 📬 Contributing

Pull requests and ideas are welcome. Let’s make this smarter together!

---

## 📜 License

MIT License — free to use, modify, and share.
```
