import streamlit as st

st.header("Home Page")

with st.container():
    chatbot = st.chat_input("Ask me anything:")
