from flask import Flask, request, jsonify
import openai
from flask_cors import CORS
from supabase import create_client, Client
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)  # To handle Cross-Origin Resource Sharing (CORS) between frontend and backend

# OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")



@app.route('/')
def home():
    return "Welcome to the Code Optimizer!"

@app.route('/optimize', methods=['POST'])
def optimize_code():
    code = request.json.get("code")
    
    response = openai.Completion.create(
        model="gpt-4",  # Using the GPT-4 model
        prompt=f"Optimize the following code and give me the comments on what you have improved in a very Gen-Z way with using emojis occasionally:\n\n{code}\n",
        max_tokens=250
    )
    
    optimized_code = response.choices[0].text.strip()
    
    return jsonify({
        "optimized_code": optimized_code
    })




if __name__ == '__main__':
    app.run(debug=True)
