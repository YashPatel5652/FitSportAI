# import openai
# import toml
# import streamlit as st


# def show_messages(text):
#     messages_str = [
#         f"<span style='color: green;'><b>USER</b>: {_['content']}</span></br>"  if _['role'] == 'user' else f"<span style='color: white;'><b>SYSTEM</b>: {_['content']}</span></br></br>"
#         for _ in st.session_state["messages"][1:]
#     ]
#     text.markdown("Messages", unsafe_allow_html=True)
#     text.markdown(str("\n".join(messages_str)), unsafe_allow_html=True)
    
    


# #with open("../secrets.toml", "r") as f:
# #    config = toml.load(f)

# openai.api_key = ""

# BASE_PROMPT = [{"role": "system", 'content':"""
# You are Donnie, an automated Gym assistant to provide workout routines for the users and give suggestions. \
# You first greet the customer, then ask them what type of workout routine they want, \
# give them a few workout options and wait for them to finalize\ if they ask for changes make those changes accordingly\
# , then summarize it and check for a final \
# time if the user wants to add anything else. \
# If it's a split, you ask for an upper body lower body or back chest and legs split. \

# Make sure to clarify all questions about exercises and form \
# also make sure to talk only about fitness and fitness related topics\
# You respond in a short, very conversational friendly style. \



# """}]

# if "messages" not in st.session_state:
#     st.session_state["messages"] = BASE_PROMPT

# st.header("FIT-BOT")

# text = st.empty()
# show_messages(text)

# if 'something' not in st.session_state:
#     st.session_state.something = ''

# def submit():
#     st.session_state.something = st.session_state.widget
#     st.session_state.widget = ''


# st.text_input('Enter message here ', key='widget', on_change=submit)
#     # st.write(a)
# if st.session_state.something != '':
#     with st.spinner("Generating response..."):
        
#         st.session_state["messages"] += [{"role": "user", "content": st.session_state.something}]
#         response = openai.ChatCompletion.create(
#             model="gpt-3.5-turbo", messages=st.session_state["messages"]
#         )
        
#         message_response = response["choices"][0]["message"]["content"]
#         st.session_state["messages"] += [
#             {"role": "system", "content": message_response}
#         ]
#         show_messages(text)
        
#     st.session_state.something = ''

#     if st.button("Clear"):
#         st.session_state["messages"] = BASE_PROMPT
#         show_messages(text)


# import openai
# import toml
# import streamlit as st
# import os

# if "user_id" not in st.session_state:
#     st.warning("⚠️ You must log in to access this page.")
#     st.stop() 

# # Load API key from environment variable (if set)
# openai.api_key = os.getenv("OPENAI_API_KEY")

# # If the environment variable is not set, use the hardcoded key (not recommended for production)
# if openai.api_key is None:
#     openai.api_key = ""
# # Function to show messages
# def show_messages(text):
#     messages_str = [
#         f"<span style='color: green;'><b>USER</b>: {_['content']}</span></br>"  if _['role'] == 'user' else f"<span style='color: white;'><b>SYSTEM</b>: {_['content']}</span></br></br>"
#         for _ in st.session_state["messages"][1:]
#     ]
#     text.markdown("Messages", unsafe_allow_html=True)
#     text.markdown(str("\n".join(messages_str)), unsafe_allow_html=True)


# # Base prompt for the chatbot
# BASE_PROMPT = [{"role": "system", 'content':"""
# You are Donnie, an automated Gym assistant to provide workout routines for the users and give suggestions. \
# You first greet the customer, then ask them what type of workout routine they want, \
# give them a few workout options and wait for them to finalize. If they ask for changes, make those changes accordingly. \
# Then summarize it and check for a final response to see if the user wants to add anything else. \
# If it's a split, you ask for an upper body, lower body, or back chest and legs split. \

# Make sure to clarify all questions about exercises and form. \
# Also, make sure to talk only about fitness and fitness-related topics. \
# You respond in a short, very conversational, friendly style. \
# """}]

# # Initialize session state if not already initialized
# if "messages" not in st.session_state:
#     st.session_state["messages"] = BASE_PROMPT

# # Title of the app
# st.header("FIT-BOT")

# # Placeholder for messages
# text = st.empty()

# # Function to display messages
# show_messages(text)

# # Initialize input field state
# if 'something' not in st.session_state:
#     st.session_state.something = ''

# # Function to handle submit
# def submit():
#     st.session_state.something = st.session_state.widget
#     st.session_state.widget = ''

# # Input for the user message
# st.text_input('Enter message here ', key='widget', on_change=submit)

# # When a message is entered, get a response from OpenAI
# if st.session_state.something != '':
#     with st.spinner("Generating response..."):
        
#         # Add the user's message to the session state
#         st.session_state["messages"] += [{"role": "user", "content": st.session_state.something}]
        
#         try:
#             # Get the response from OpenAI API
#             response = openai.ChatCompletion.create(
#                 model="gpt-3.5-turbo",  # You can change the model as per your requirement
#                 messages=st.session_state["messages"]
#             )
            
#             # Extract the message from the response
#             message_response = response["choices"][0]["message"]["content"]
            
#             # Add the system's response to the session state
#             st.session_state["messages"] += [{"role": "system", "content": message_response}]
            
#             # Show the messages
#             show_messages(text)

#         except openai.error.AuthenticationError:
#             st.error("API Key is missing or incorrect. Please check the key and try again.")
#         except openai.error.OpenAIError as e:
#             st.error(f"An error occurred with OpenAI: {e}")
#         except Exception as e:
#             st.error(f"An unexpected error occurred: {e}")
        
#     # Reset the input field after response
#     st.session_state.something = ''

# # Button to clear the conversation
# if st.button("Clear"):
#     st.session_state["messages"] = BASE_PROMPT
#     show_messages(text)


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

