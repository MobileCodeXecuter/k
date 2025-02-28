from flask import Flask, request, jsonify
from flask_cors import CORS
import transformers
import logging

app = Flask(__name__)

# Enable CORS for all routes
CORS(app, origins=["https://k-t7mp.vercel.app"])  # Allow requests from your frontend

# Set up logging
logging.basicConfig(level=logging.DEBUG)

# Load your AI model
try:
    app.logger.info("Loading model...")
    generator = transformers.pipeline("conversational", model="microsoft/DialoGPT-small")
    app.logger.info("Model loaded successfully!")
except Exception as e:
    app.logger.error("Error loading model:", e)
    generator = None

@app.route("/")
def home():
    return "Chatbot is running! Use the /chat endpoint to interact."

@app.route("/chat", methods=["POST", "OPTIONS"])  # Allow POST and OPTIONS methods
def chat():
    if request.method == "OPTIONS":
        # Handle preflight request
        response = jsonify({"message": "Preflight request successful"})
        response.headers.add("Access-Control-Allow-Origin", "https://k-t7mp.vercel.app")
        response.headers.add("Access-Control-Allow-Headers", "Content-Type")
        response.headers.add("Access-Control-Allow-Methods", "POST")
        return response

    app.logger.debug("Received request: %s", request.json)
    if generator is None:
        app.logger.error("Model not loaded.")
        return jsonify({"error": "Model not loaded. Please check the logs."})

    user_input = request.json.get("message")
    if not user_input:
        app.logger.error("No message provided.")
        return jsonify({"error": "Please provide a message."})

    try:
        response = generator(user_input)
        app.logger.debug("Generated response: %s", response)
        return jsonify({"response": response[0]["generated_text"]})
    except Exception as e:
        app.logger.error("Error generating response:", e)
        return jsonify({"error": "Sorry, I encountered an error. Please try again."})

if __name__ == "__main__":
    app.run(debug=True)
