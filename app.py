from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Chatbot is running! Use the /chat endpoint to interact."

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    if not user_input:
        return jsonify({"error": "Please provide a message."}), 400
    return jsonify({"response": f"You said: {user_input}"})

if __name__ == "__main__":
    app.run(debug=True)
