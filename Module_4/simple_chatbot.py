import google.generativeai as genai
import streamlit as st

# setting API key
MY_API_KEY = st.text_input("Please Enter API Key.")

genai.configure(api_key = MY_API_KEY)

# selecting the model
model = genai.GenerativeModel('gemini-1.5-flash')

# function to getting the responce
def gettingresponce(user_input):
    response = model.generate_content(user_input)
    return response.text

user_input = st.text_input("Please ask Your Question.")
model_reply = (gettingresponce(user_input))
st.write(model_reply)