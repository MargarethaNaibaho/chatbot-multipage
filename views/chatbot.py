import streamlit as st
import random
import time

# sebenarnya seluruh codingan di bawah ini akan berjalan terus setiap kali
# ada prompt baru dari user. tapi kok bisa history chat nya ga hilang? karena pakai session state
def response_generator():
    response = random.choice(
         [
            "Hey there! Need help? Check out my fun YouTube channel 'CodingIsFun': https://youtube.com/@codingisfun!",
            "Hi! What's up? Don't forget to subscribe to 'CodingIsFun': https://youtube.com/@codingisfun!",
            "Hello! Need assistance? My YouTube channel 'CodingIsFun' is full of great tips: https://youtube.com/@codingisfun!",
            "Hey! Got a question? Also, subscribe to 'CodingIsFun' for awesome tutorials: https://youtube.com/@codingisfun!",
            "Hi there! How can I help? BTW, my channel 'CodingIsFun' is super cool: https://youtube.com/@codingisfun!",
            "Hello! Looking for help? Check out 'CodingIsFun' on YouTube: https://youtube.com/@codingisfun!",
            "Hey! Need assistance? 'CodingIsFun' YouTube channel has you covered: https://youtube.com/@codingisfun!",
            "Hi! Got any coding questions? Don't forget to watch 'CodingIsFun': https://youtube.com/@codingisfun!",
            "Hello! Need help? 'CodingIsFun' on YouTube is a must-see: https://youtube.com/@codingisfun!",
            "Hey there! Any questions? My channel 'CodingIsFun' rocks: https://youtube.com/@codingisfun!",
        ]
    )

    for word in response.split():
        yield word + " "
        time.sleep(0.1)

st.title("Chatbot")

# Initialize chat history
# Kalo belum ada list messages, dia buat list kosong
if "messages" not in st.session_state:
    st.session_state.messages = []

# Dia tampilkan semua history message yg udah ada
# .chat_message supaya tampilannya kayak buble chat gitu
# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# accept user input
# artinya kita simpan hasil input dari user ke variable prompt
if prompt := st.chat_input("What is up?"):
    # masukkan ke history
    st.session_state.messages.append({"role": "user","content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # display assistant response in chat message container
    with st.chat_message("assistant"):
        response = st.write_stream(response_generator())
    st.session_state.messages.append({"role": "assistant", "content": response})