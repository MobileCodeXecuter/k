# Step 1: Import necessary libraries
from transformers import pipeline
import os

# Step 2: Load the API key directly from the environment variable
api_key = os.getenv("HUGGINGFACE_API_KEY")
if not api_key:
    raise ValueError("HUGGINGFACE_API_KEY not found in environment variables.")

# Step 3: Load the Microsoft DialoGPT model
try:
    print("Loading model...")
    generator = pipeline("conversational", model="microsoft/DialoGPT-small", use_auth_token=api_key)
    print("Model loaded successfully!")
except Exception as e:
    print("Error loading model:", e)
    generator = None  # Ensure generator is defined even if loading fails

# Step 4: Chatbot loop
print("Chatbot is ready! Type 'exit' to end the conversation.")
while True:
    # Get user input
    user_input = input("You: ")

    # Exit the chatbot if the user types 'exit'
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break

    # Generate a response
    if generator is None:
        print("Chatbot: Model is not loaded. Please check the error logs.")
    else:
        try:
            response = generator(user_input)
            print(f"Chatbot: {response}")
        except Exception as e:
            print(f"Chatbot: Sorry, I encountered an error. Please try again. Error: {e}")
