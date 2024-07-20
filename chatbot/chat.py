import streamlit as st
from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as ggi

load_dotenv(".env")

fetcheed_api_key = os.getenv("API_KEY")
ggi.configure(api_key = "AIzaSyBmlUKVyw3eHkW0wjyLhcvLBnGT9MP_EmI")

model = ggi.GenerativeModel("gemini-pro") 
chat = model.start_chat()

def LLM_Response(question):
    question= ""+question+" answer me emotionally"
    response = chat.send_message(question,stream=True)
    return response

st.title("Talk with Tarry")

user_quest = st.text_input("Hey there, do you have any questions or require guidance? Even if you just neeed someone to talk to, I'm here for you.")
btn = st.button("Ask")

if btn and user_quest:
    result = LLM_Response(user_quest)
    st.subheader("Response : ")
    for word in result:
        st.text(word.text)
