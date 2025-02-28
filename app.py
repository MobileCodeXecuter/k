from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
import transformers

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load your AI model
try:
    print("Loading model...")
    generator = transformers.pipeline("conversational", model="microsoft/DialoGPT-small")
    print("Model loaded successfully!")
except Exception as e:
    print("Error loading model:", e)
    generator = None

@app.route("/")
def home():
    return "Chatbot is running! Use the /chat endpoint to interact."

@app.route("/chat", methods=["POST"])
def chat():
    if generator is None:
        return jsonify({"error": "Model not loaded. Please check the logs."})

    user_input = request.json.get("message")
    if not user_input:
        return jsonify({"error": "Please provide a message."})

    response = generator(user_input)
    return jsonify({"response": response[0]["generated_text"]})

if __name__ == "__main__":
    app.run(debug=True)
