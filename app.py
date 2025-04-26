from flask import Flask, request, jsonify
import os
from dotenv import load_dotenv
import requests
from flask_cors import CORS

# Load environment variables from .env file
load_dotenv()
# Enable CORS for cross-origin requests
app = Flask(__name__)
CORS(app)



# Read DeepSeek API key from environment
deepseek_api_key = os.getenv("DEEPSEEK_API_KEY")\

if not deepseek_api_key:
    raise ValueError("⚠️ DEEPSEEK_API_KEY is missing. Set it in your .env file.")

@app.route("/", methods=["GET"])
def home():
    return "Welcome to the AI Code Analyzer! Go to /api/message to submit your code for analysis."

@app.route("/api/message", methods=["POST"])
def analyze_code():
    # Get the code from the request
    data = request.json
    user_code = data.get("code", "").strip()

    if not user_code:
        return jsonify({"error": "No code provided"}), 400

    # Set up DeepSeek API request
    url = "https://api.deepseek.ai/v1/code/optimize"
    headers = {
        "Authorization": f"Bearer {deepseek_api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "code": user_code
    }

    try:
        # Send the code to DeepSeek API for analysis
        response = requests.post(url, json=payload, headers=headers)
        response_data = response.json()

        if response.status_code == 200:
            # Get the optimized code and comments from DeepSeek response
            optimized_code = response_data.get("optimized_code", "No optimized code returned.")
            comments = response_data.get("comments", "No comments provided.")

            return jsonify({
                "comment": comments,
                "optimized_code": optimized_code
            })
        else:
            return jsonify({"error": "Error during DeepSeek API call", "details": response_data}), 500
    except Exception as e:
        return jsonify({"error": f"Error during API request: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)
