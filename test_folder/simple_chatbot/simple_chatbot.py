import google.generativeai as genai
import streamlit as st
# import os
# from dotenv import load_dotenv

# load_dotenv()
# api_key = os.getenv("MY_API_KEY")

api_key = st.secrets["MY_API_KEY"]

genai.configure(api_key=api_key)

# Select the model
def select_model():
    return genai.GenerativeModel('gemini-1.5-flash')  # Adjust if needed

# Function to get the response from the model
def getting_response(model, prompt):
    response = model.generate_content(prompt)
    return response.text

# Streamlit UI
st.set_page_config(page_title="Interactive Chatbot", page_icon="🤖", layout="centered")
st.title("🤖 A Simple and Interactive Chatbot")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# User input area
user_input = st.text_input("Please ask Your Question", placeholder="Type your message here...")

if st.button("Send") and user_input:
    # Select the model
    model = select_model()
    
    with st.spinner("Thinking..."):
        # Get the response
        model_reply = getting_response(model, user_input)
        
        # Update chat history
        st.session_state.chat_history.append(("You", user_input))
        st.session_state.chat_history.append(("Bot", model_reply))
        
    # Clear the input box by resetting the widget key
    user_input = ""

# Display chat history
if st.session_state.chat_history:
    for i, (sender, message) in enumerate(st.session_state.chat_history):
        if sender == "You":
            background_color = "#E6F7FF"  # Light blue background for user
            alignment = "right"
        else:
            background_color = "#FFEBE6"  # Light pink background for bot
            alignment = "left"
        
        st.markdown(
            f"<div style='text-align: {alignment}; padding: 10px; background-color: {background_color}; "
            f"border-radius: 10px; margin: 5px 0; color: black;'>{sender}: {message}</div>",
            unsafe_allow_html=True,
        )

# Footer
st.markdown("---")
st.write("My First Interactive ChatBot.")