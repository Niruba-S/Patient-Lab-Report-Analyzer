import streamlit as st
import os
from dotenv import load_dotenv
from module import display

load_dotenv()
st.session_state.api_key = os.environ.get("OPEN_AI_KEY") 

if "page" not in st.session_state:
    st.session_state.page = "home"
if "conversation" not in st.session_state:
    st.session_state.conversation = []
if "uploaded_file" not in st.session_state:
    st.session_state.uploaded_file = None
if "text" not in st.session_state:
    st.session_state.text = " "
if "show_clicked" not in st.session_state:
    st.session_state.show_clicked = False
if "Image_text" not in st.session_state:
    st.session_state.Image_text = ""
if st.session_state.page == "home":
    st.header("Patient Lab Report Analyzer")

    try:
        st.session_state.uploaded_file = st.file_uploader("Choose a file", type=["pdf"])
        if st.session_state.uploaded_file:
            if not st.session_state.show_clicked:
                if st.button("ANALYZE") :
                    try:
                        dis = display(st.session_state.uploaded_file, st.session_state.api_key)
                        try:
                            t_im=dis.request()
                            st.session_state.text = t_im
                            st.session_state.Image_text =t_im
                        except:
                            pass
                        text = dis.analyze(st.session_state.text)
                        st.session_state.text = text
                        st.title("REPORT")
                        st.write(st.session_state.text)
                        st.title("AI GENERATED SUMMARY")
                        sum=dis.summary(st.session_state.text)
                        st.write(sum)
                        st.session_state.text+=st.session_state.Image_text
                        st.session_state.show_clicked = True
                    except Exception as e:
                        st.error(f"Error processing PDF: {e}")
            if st.session_state.show_clicked and st.session_state.page != "chatbot":
                if st.button("CHAT_BOT"):
                    st.session_state.page = "chatbot"

    except :
        pass

elif st.session_state.page == "chatbot":
    if "st.session_state.user_input" not in st.session_state:
        st.session_state.user_input = None
    st.session_state.user_input = st.text_input("You:", key="input")

    if st.button("Send"):
        if st.session_state.user_input:
            dis = display(st.session_state.uploaded_file, st.session_state.api_key)
            m = dis.get_openai_response(st.session_state.text, st.session_state.user_input)
            bot_response = m
            st.session_state.conversation.append({"role": "assistant", "content": bot_response})
            st.session_state.conversation.append({"role": "user", "content": st.session_state.user_input})


    for i in range(len(st.session_state.conversation)):
        message=st.session_state.conversation[len(st.session_state.conversation)-i-1]
        if message["role"] == "assistant":
            
            
            st.write(f"**bot:** {message['content']}")
            
        else:
            st.write("                   ____________________________________________________________________________________________________________________________________________                                ")
            st.write(f"**user:** {message['content']}")
            
            

































# if st.session_state.bot:
#         # @st.cache_resource
#     def initialize():
#         chat= chat_gen(st.session_state.api_key,st.session_state.uploaded_file)
#         return chat

#     st.session_state.chat=initialize()

#     st.title("Doc chat Bot")

#     # Initialize chat history
#     if "messages" not in st.session_state:
#         st.session_state.messages = []

#     # Display chat messages from history on app rerun
#     for message in st.session_state.messages:
#         with st.chat_message(message["role"]):
#             st.markdown(message["content"])

#     # React to user input
#     if prompt := st.chat_input("What is up?"):
#         # Display user message in chat message container
#         st.chat_message("user").markdown(prompt)
#         # Add user message to chat history
#         st.session_state.messages.append({"role": "user", "content": prompt})

#         response = st.session_state.chat.ask_pdf(prompt,) 
#         #f"Echo: {prompt}"
#         # Display assistant response in chat message container
#         with st.chat_message("assistant"):
#             st.markdown(response)
#         # Add assistant response to chat history
#         st.session_state.messages.append({"role": "assistant", "content": response})






