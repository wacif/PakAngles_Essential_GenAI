import streamlit as st
import anthropic

# Setting API key
api_key = st.secrets["Anthropic_API_KEY"]
# Initialize the Anthropic client
client = anthropic.Anthropic(api_key=api_key)

# Title and Description
st.title("Diabetic Diet Plan Generator")
st.write("Welcome to the Diabetic Diet Plan Generator! This app helps you create a personalized diet plan based on your blood sugar levels.")

# Warning Message
st.warning("⚠️ Please consult with your healthcare provider before making any changes to your diet plan.")

# Sidebar for User Input
st.sidebar.header("Input Your Information")

# Blood sugar level inputs
fasting_sugar = st.sidebar.number_input("Fasting Sugar Level (mg/dL)", min_value=0)
before_meal_sugar = st.sidebar.number_input("Before Meal Sugar Level (mg/dL)", min_value=0)
after_meal_sugar = st.sidebar.number_input("After Meal Sugar Level (mg/dL)", min_value=0)

# Optional input for diabetes type
diabetes_type = st.sidebar.selectbox("Type of Diabetes (Optional)", ("Select", "Type 1", "Type 2", "Gestational", "Other"))

# Submit Button
if st.sidebar.button("Generate Diet Plan"):
    # Preparing the input for the API
    user_input = f"""
    Fasting Sugar Level: {fasting_sugar} mg/dL
    Before Meal Sugar Level: {before_meal_sugar} mg/dL
    After Meal Sugar Level: {after_meal_sugar} mg/dL
    """

    if diabetes_type != "Select":
        user_input += f"\nType of Diabetes: {diabetes_type}"

    # API request
    message = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=1000,
        temperature=0,
        system="You are a world-class dietician. Respond only with detailed diet plans in a user-friendly format, including bold headings and bullet points.",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": f"Based on the following blood sugar levels:\n{user_input}\nProvide a suitable diet plan."
                    }
                ]
            }
        ]
    )

    # Extract the response and format it as a single string
    raw_text = message.content
    response = raw_text[0].text

    # Display the diet plan in a user-friendly format
    st.write(response)

# Main Section (for displaying the diet plan)
st.write("Your personalized diet plan will appear here after you submit your blood sugar levels.")
