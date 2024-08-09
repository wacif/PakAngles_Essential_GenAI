import google.generativeai as genai
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("MY_API_KEY")

genai.configure(api_key = api_key)

# Select the model
def select_model():
        return genai.GenerativeModel('gemini-1.5-flash')  # Adjust if needed

# Function to get the response from the model
def getting_response(model, prompt):
    response = model.generate_content(prompt)
    return response.text

# Streamlit UI
st.title("A Simple Chatbot")

# Enter user input
user_input = st.text_input("Please ask Your Question")

if user_input:
     # Select the model
     model = select_model()
     # Get and display the response
     model_reply = getting_response(model, user_input)
     st.write(model_reply)
else:
     st.write("Please make sure you ask a valid question.")

# Footer
st.markdown("---")
st.write("My First ChatBot.")




