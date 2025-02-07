from flask import Flask ,request, jsonify
import openai
from flask_cors import CORS 
from supabase import create_client,Client
import os 
from dotenv import load_dotenv

load_dotenv()

app=Flask(__name__)

openai.api_key=os.getenv("OPENAI_API_KEY")

SUPABASE_URL=os.getenv("SUPABASE_URL")
SUPABASE_KEY=os.getenv("SUPABASE_KEY")
supabase:Client =create_client(SUPABASE_URL, SUPABASE_KEY)

@app.route('/')
def home():
    return "Welcome to the Code Optimizer!"

@app.route('/optimize',methods=['POST'])
def optimize_code():
    code=request.json.get("code")
    
    response = openai.Completion.create(
        model="gpt-4o-mini",
        prompt=f"Optimize the following code and give me the comments on what you have imporved with in a very gen-z way with using emojis ocasionally:\n\n{code}\n",
        max_tokens=250
    )
    
    optimized_code = response.choices[0].text.strip()
    
    return jsonify({
        "optimized_code":optimized_code
    })
    
if __name__=='__main__':
    app.run(debug=True)