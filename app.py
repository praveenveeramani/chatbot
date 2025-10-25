import streamlit as st
from groq_chat import chat_with_groq

st.set_page_config(page_title="Chatbot", page_icon="👽", layout="centered")

st.title("🤖 AI Chatbot")
st.markdown("Chat with your AI model powered by **Groq API**!")

# Chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Display previous messages
for msg in st.session_state["messages"]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
user_input = st.chat_input("Ask me anything...")
if user_input:
    st.session_state["messages"].append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = chat_with_groq(user_input)
            st.markdown(response)

    st.session_state["messages"].append({"role": "assistant", "content": response})
