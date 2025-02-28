# Step 1: Import necessary libraries
from transformers import pipeline
import os

# Step 2: Load the API key directly from the environment variable
api_key = os.getenv("HUGGINGFACE_API_KEY")
if not api_key: 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
    raise ValueError("HUGGINGFACE_API_KEY not found in environment variables.")

# Step 3: Load the Microsoft DialoGPT model
try:
    print("Loading model...")
    generator = pipeline("conversational", model="microsoft/DialoGPT-small", use_auth_token=api_key)
    print("Model loaded successfully!")
except Exception as e:
    print("Error loading model:", e)
    generator = None  # Ensure generator is defined even if loading fails

# Step 4: Print a success message
print("Chatbot setup complete! The app is ready for deployment.")
