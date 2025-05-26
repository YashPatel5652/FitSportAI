import streamlit as st
import google.generativeai as genai
import os

# Configure Gemini API Key
genai.configure(api_key=os.getenv("GEMINI_API_KEY") or "your Gamini_API_KEY")

# Initialize model
model = genai.GenerativeModel("gemini-pro")

# System prompt
SYSTEM_PROMPT = "You are Donnie, a friendly gym assistant who only talks about fitness. Greet the user and help build a workout plan."

# Streamlit setup
st.title("🏋️ FIT-BOT (Gemini AI)")

# Initialize message list
if "messages" not in st.session_state:
    st.session_state.messages = [SYSTEM_PROMPT]  # Just use string messages

# Show chat history
for i, msg in enumerate(st.session_state.messages[1:], start=1):  # skip system prompt
    if i % 2 == 1:
        st.markdown(f"🧍‍♂️ **User:** {msg}")
    else:
        st.markdown(f"🤖 **Donnie:** {msg}")

# Input
user_input = st.text_input("💬 Type your message here:")

# On submit
if user_input:
    st.session_state.messages.append(user_input)

    try:
        response = model.generate_content(st.session_state.messages)
        reply = response.text
        st.session_state.messages.append(reply)
        st.rerun()

    except Exception as e:
        st.error(f"❌ Gemini Error: {e}")

# Clear button
if st.button("Clear Conversation"):
    st.session_state.messages = [SYSTEM_PROMPT]
    st.rerun()

