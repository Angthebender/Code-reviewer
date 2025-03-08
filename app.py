from flask import Flask, request, jsonify
from transformers import pipeline
import os
from dotenv import load_dotenv
from flask_cors import CORS
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
CORS(app)
# Load environment variables from .env file
load_dotenv()

# Read Hugging Face token from environment
huggingface_token = os.getenv("HUGGING_FACE_HUB_TOKEN")
if not huggingface_token:
    raise ValueError("⚠️ HUGGING_FACE_HUB_TOKEN is missing. Set it in your .env file.")

# Initialize the Hugging Face text generation pipeline with authentication
generator = pipeline(
    "any-to-any",
    model="onnx-community/Janus-1.3B-ONNX",
    token=huggingface_token,
    device="0"
)

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Code Optimizer! This is the backend."

@app.route('/optimize', methods=['POST'])
def optimize_code():
    code = request.json.get("code")
    
    if not code:
        return jsonify({"error": "No code provided"}), 400

    # Prepare the prompt
    prompt = (
        "Give a optimized form of the code given an dont repeat your self if the code is good then give some comment to better the code here is the code:"
        
        f"{code}"
    )
    
    result = generator(prompt, max_length=500, num_return_sequences=1)[0]['generated_text']
    
    return jsonify({
        "optimized_code": result
    })

if __name__ == '__main__':
    app.run(debug=True)
