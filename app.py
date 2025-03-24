from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import pipeline

app = Flask(__name__)
CORS(app)  # Allow frontend access

# ✅ Load Phi-4-mini-instruct model from Microsoft
try:
    pipe = pipeline("text-generation", model="microsoft/Phi-4-mini-instruct", trust_remote_code=True)
except Exception as e:
    print(f"Error loading model: {e}")
    pipe = None  # Gracefully handle errors if the model cannot be loaded

@app.route("/", methods=["GET"])
def home():
    return "Welcome to the AI Code Analyzer! Go to /analyze to submit your code for analysis."

@app.route("/analyze", methods=["POST"])
def analyze_code():
    if not pipe:
        return jsonify({"error": "AI model is not available"}), 500
    
    data = request.json
    user_code = data.get("code", "").strip()

    if not user_code:
        return jsonify({"error": "No code provided"}), 400

    # Hidden prompt for AI (it will not be exposed to the user)
    prompt = f"""
    You are a junior software engineer reviewing the following code. Please provide an optimized version of the code, 
    write comments explaining the changes you made, and make the tone friendly and approachable. 
    Add emojis where appropriate to make the explanation more engaging, as if you're chatting with a colleague.

    ### Given Code:
    {user_code}

    ### Optimized Code and Comments:
    """

    try:
        # ✅ Generate AI response (optimized code and comments with emojis)
        response = pipe(prompt)

        # Extract the generated text, which will contain both optimized code and comments
        generated_text = response[0]["generated_text"].strip()

        # Return the generated optimized code and comments to the user (without revealing the prompt)
        return jsonify({
            "comment": "AI-generated review and optimization suggestion (from a junior engineer's perspective):",
            "optimized_code": generated_text
        })
    except Exception as e:
        return jsonify({"error": f"Error during model inference: {e}"}), 500

if __name__ == "__main__":
    app.run(debug=True)
