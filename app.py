from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os
import requests
import traceback

load_dotenv()

app = Flask(__name__)
CORS(app)

DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
DEEPSEEK_URL = "https://api.deepseek.com/v1/chat/completions"

@app.route("/api/message", methods=["POST"])
def analyze_code():
    try:
        data = request.json
        user_code = data.get("code", "").strip()
        if not user_code:
            return jsonify({"error": "No code provided"}), 400

        prompt = f"""You are a junior developer who answers coding questions. If the user asks for code, provide a solution directly without unnecessary explanations. If there are multiple solutions, choose the most optimal one. When the solution contains code, format it in a box with a grey background. if you have any code then write it inside```code```
\n{user_code}\n"""

        headers = {
            "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
            "Content-Type": "application/json"
        }

        body = {
            "model": "deepseek-coder",
            "messages": [
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.5,
            "max_tokens": 500
        }

        response = requests.post(DEEPSEEK_URL, headers=headers, json=body)
        response.raise_for_status()
        output = response.json()

        ai_reply = output["choices"][0]["message"]["content"]

        return jsonify({
            "comment": "Here's the improved code and explanation:",
            "optimized_code": ai_reply
        })
    except Exception as e:
        print("❌ Error:", e)
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
