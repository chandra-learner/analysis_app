import os
import openai
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv
import streamlit as st
import requests

_ = load_dotenv(find_dotenv())
OpenAI.api_key = os.environ['OPENAI_API_KEY']  # store api key in .env file -- export OPENAI_API_KEY = 'sk-proj-tSsXLnnZIpHXtq73BQ5bT3BlbkFJLAGOzyUykAfmTbpLqrLH'

print(OpenAI.api_key)
print(openai.__version__)

client = OpenAI()

def get_response(messages, model='gpt-3.5-turbo'):
    
    response = client.chat.completions.create(
        model=model,
        messages = messages,
        temperature = 0,
        max_tokens = 400   # controls only output
    )
    token_count = response.usage
    print(f"token count : {token_count}")
    return response.choices[0].message.content


def main():
    # Title of the webpage
    st.title('Expert Stock Analysis')
    
    # Text box for user input
    user_input = st.text_input("Enter Stock Name/Symbol: ")
    
    system_msg = "you are a stock analyst"

    assistant_msg = ""

    #user_msg = "HI, write a peom for a loving wife friend in 4 lines"
    user_msg = f"Write technical analysis of {user_input} stock in tabular form. and recommendation for stock if it can be buy or sell"

    messages = [{"role": "system", "content":system_msg},
                {"role": "assistant", "content":assistant_msg},
                {"role": "user", "content":user_msg}]

    response = get_response(messages)
    print(response)
    
    # Button to trigger API call
    if st.button('Submit'):
        # Call the API with the user input
        result = get_response(messages)
        # Display the API response on the page
        st.write(response)

if __name__ == "__main__":
    main()


