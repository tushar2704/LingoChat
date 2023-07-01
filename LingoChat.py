import streamlit as st
import openai
st.title("Foreign-Language Private Tutor")

# Initialize OpenAI API
api_key = st.text_input("Enter your OpenAI API key")
if not api_key:
    st.write("Please enter your OpenAI API key first. Don't worry this will not be stored.")
    st.stop()
openai.api_key = api_key

text_input = st.text_input("Enter your text, in any Language and start chatting")
generate_button = st.button("Generate")

def generate_response(input_text):
    response = openai.Completion.create(
        engine="text-davinci-003",  # Specify the engine you want to use
        prompt=input_text,
        max_tokens=100  # Adjust the token limit as needed
    )

    return response.choices[0].text.strip()
if generate_button:
    # Call your generative AI model to generate a response based on the user's input
    response = generate_response(text_input)

    # Display the generated response
    st.write(response)
