import streamlit as st

from mini_components.forms.contact import contact_form

@st.dialog("Contact me") #untuk buat modal / pop-up window
def show_contact_form():
    contact_form()

# hero section
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")

with col1:
    st.image("./assets/face.png", width=200)

with col2:
    st.title("Margaretha Naibaho", anchor=False) # anchor ini dibuat False karena ga perlu link di header itu
    st.write(
        "Front-end Developer, focusing on JavaScript and Java Spring Boot"
    )

    if st.button("💌 Contact me"):
        show_contact_form()

# Experience and qualifications
st.write("\n")
st.subheader("Experience & Qualifications", anchor=False)
st.write(
    """
    - 🌱 Exploring **deep learning for image classification** and **cloud deployment**  
    - 💬 Feel free to ask me about **Java backend development, REST APIs, and database design**  
    - 📫 How to reach me: [LinkedIn](https://www.linkedin.com/in/margaretha-gok-asi-naibaho/) 
    - ⚡ Fun fact: Used to teach English while diving into tech!
    """
)

# Skills
st.write("\n")
st.subheader("Hard skills", anchor=False)
image_urls = [
    "https://upload.wikimedia.org/wikipedia/en/3/30/Java_programming_language_logo.svg",
    "https://upload.wikimedia.org/wikipedia/commons/4/44/Spring_Framework_Logo_2018.svg",
    "https://upload.wikimedia.org/wikipedia/commons/2/29/Postgresql_elephant.svg",
    "https://upload.wikimedia.org/wikipedia/commons/9/99/Unofficial_JavaScript_logo_2.svg",
    "https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg",
    "https://upload.wikimedia.org/wikipedia/commons/2/2d/Tensorflow_logo.svg"
]
columns_for_skills = st.columns(6, gap="small")

for col, url in zip(columns_for_skills, image_urls):
    with col:
        st.image(url, width=30)