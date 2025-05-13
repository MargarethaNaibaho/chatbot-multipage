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

# Navigation setup
pg = st.navigation(pages=[about_page, sales_dashboard_page, chatbot_page])

# Run
pg.run()