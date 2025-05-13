import streamlit as st

# Page setup
about_page = st.Page(
    page="views/about_me.py",
    title="About Me",
    icon=":material/account_circle:",
    default=True
)

sales_dashboard_page = st.Page(
    page="views/sales_dashboard.py",
    title="Sales Dashboard",
    icon=":material/bar_chart:",
)

chatbot_page = st.Page(
    page="views/chatbot.py",
    title="Chatbot",
    icon=":material/smart_toy:"
)

chatgpt_clone = st.Page(
    page="views/chatgpt_clone.py",
    title="ChatGPT Clone",
    icon=":material/forum:"
)

# Navigation setup
# pg = st.navigation(pages=[about_page, sales_dashboard_page, chatbot_page])

pg = st.navigation(
    {
        "Info": [about_page],
        "Projects": [sales_dashboard_page, chatbot_page, chatgpt_clone]
    }
)

#  shared on all pages
st.logo("assets/laskar_ai_logo.png")
st.sidebar.text("Made with ❤️ by Margaretha")

# Run
pg.run()