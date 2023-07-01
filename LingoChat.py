#Author Tushar Aggarwal(https://www.tushar-aggarwal.com/)
# LingoChat

import streamlit as st
import openai

# Application title and body
st.set_page_config(page_title="🤖LingoChat🤖",
                   page_icon="🤖",
                   layout='wide')
# Title of application
st.title("🤖LingoChat")
st.markdown("### By [Tushar Aggarwal](https://www.tushar-aggarwal.com/)")

# Initialize OpenAI API
st.sidebar.markdown("## OpenAI API Key")

api_key = st.sidebar.text_input("Enter your OpenAI API key")
if not api_key:
    st.write("Please enter your OpenAI API key first. Don't worry this will not be stored.")
    st.stop()
openai.api_key = api_key

text_input = st.text_input("Now enter your query, in any Language and start chatting")
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








































































# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)