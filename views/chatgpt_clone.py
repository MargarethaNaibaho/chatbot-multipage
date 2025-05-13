import streamlit as st
from openai import OpenAI

st.title("ChatGPT Clone")

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messagesGPT" not in st.session_state:
    st.session_state.messagesGPT = []

for message in st.session_state.messagesGPT:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

prompt = st.chat_input("Apa nih yang mau kamu tanya?")
if prompt:
    with st.chat_message("user"):
        st.markdown(prompt)
    
    st.session_state.messagesGPT.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""

        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=st.session_state.messagesGPT,
            stream=True,
        )
        
        for chunk in stream:
            content = chunk.choices[0].delta.content or ""
            full_response += content
            message_placeholder.markdown(full_response + " ")
        
        message_placeholder.markdown(full_response)
    
    st.session_state.messagesGPT.append({"role": "assistant", "content": full_response})