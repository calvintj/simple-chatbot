import streamlit as st
import os
import sys
from pathlib import Path
from dotenv import load_dotenv, find_dotenv
from streamlit_option_menu import option_menu
from langchain_openai import ChatOpenAI

# load api key
load_dotenv()

# set openai model
llm = ChatOpenAI(model="gpt-4o", temperature=0, openai_api_key=os.environ.get("BATI_OPENAI_API_KEY"))

header = st.container()

# with header:
#     st.title("Simple Chatbot")
#     st.write("This is a simple chatbot that uses the OpenAI API to generate responses to user questions.")

def streamlit_ui():
    with st.sidebar:
        choice = option_menu('Navigation', ['Simple_Chat'])

    if choice == 'Simple_Chat':
        if prompt := st.chat_input('Enter a message'):
            result = llm.invoke(prompt)
            st.markdown(result)

streamlit_ui()



