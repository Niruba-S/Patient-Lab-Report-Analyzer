import streamlit as st
import os
from dotenv import load_dotenv
from module import display

load_dotenv()
st.session_state.api_key = os.environ.get("OPEN_AI_KEY") 


if "conversation" not in st.session_state:
    st.session_state.conversation = []
if "uploaded_file" not in st.session_state:
    st.session_state.uploaded_file = None
if "text" not in st.session_state:
    st.session_state.text = " "
if "page" not in st.session_state:
    st.session_state.page = "home"
if "Image_text" not in st.session_state:
    st.session_state.Image_text = ""
if "sum" not in st.session_state:
    st.session_state.sum = ""
def on_click_home():
    st.session_state.page = "home"
    st.session_state.show_clicked =False     
def on_click_chat():
    st.session_state.page = "chat"
    st.session_state.show_clicked =True     
    

st.header("Patient Lab Report Analyzer")

try:
    if "show_clicked" not in st.session_state:
        st.session_state.show_clicked = False
    if not st.session_state.show_clicked and st.session_state.page == "home":
        st.session_state.uploaded_file = st.file_uploader("Choose a file", type=["pdf"])
        if st.session_state.uploaded_file and st.button("ANALYZE") :
            with st.spinner("ANALYZING"):
                try:
                    dis = display(st.session_state.uploaded_file, st.session_state.api_key)
                    try:
                        t_im = dis.request()
                        st.session_state.text = t_im
                        st.session_state.Image_text = t_im
                    except:
                        pass
                    text = dis.analyze(st.session_state.text)
                    st.session_state.text = text
                    st.title("REPORT")
                    st.write(st.session_state.text)

                    if len(st.session_state.text) > 0:
                        st.title("AI GENERATED SUMMARY")
                        st.session_state.sum = dis.summary(st.session_state.text)
                        st.write(st.session_state.sum)
                    st.session_state.text += st.session_state.Image_text
                except Exception as e:
                    st.error(f"Error processing PDF: {e}")
            st.button("chat",on_click=on_click_chat,type='primary')

    elif st.session_state.show_clicked and st.session_state.page == "chat":
        st.write(st.session_state.sum)
        st.button("go_home",on_click=on_click_home)
        if "user_input" not in st.session_state:
            st.session_state.user_input = None
        st.session_state.user_input = st.text_input("You:", key="input")
        
            
        if st.button("Send",type='secondary'):
            if st.session_state.user_input:
                dis = display(st.session_state.uploaded_file, st.session_state.api_key)
                m = dis.get_openai_response(st.session_state.text, st.session_state.user_input)
                bot_response = m
                st.session_state.conversation.append({"role": "assistant", "content": bot_response})
                st.session_state.conversation.append({"role": "user", "content": st.session_state.user_input})
        
        
        for i in range(len(st.session_state.conversation)):
            message = st.session_state.conversation[len(st.session_state.conversation) - i - 1]
            if message["role"] == "assistant":
                st.write(f"**bot:** {message['content']}")
            else:
                st.write("__________________________________________________________________________________________________________________________________________")
                st.write(f"**user:** {message['content']}")
        
    
            

except Exception as e:
    st.error(f"Unexpected error: {e}")











# import streamlit as st
# import os
# from dotenv import load_dotenv
# from module import display

# load_dotenv()
# st.session_state.api_key = os.environ.get("OPEN_AI_KEY") 


# if "page" not in st.session_state:
#     st.session_state.page = "home"
# if "conversation" not in st.session_state:
#     st.session_state.conversation = []
# if "uploaded_file" not in st.session_state:
#     st.session_state.uploaded_file = None
# if "text" not in st.session_state:
#     st.session_state.text = " "

# if "Image_text" not in st.session_state:
#     st.session_state.Image_text = ""
# if "sum" not in st.session_state:
#     st.session_state.sum = ""

# st.header("Patient Lab Report Analyzer")

# try:
#     if "show_clicked" not in st.session_state:
#         st.session_state.show_clicked = False
#     if not st.session_state.show_clicked:
#         st.session_state.uploaded_file = st.file_uploader("Choose a file", type=["pdf"])
#         if st.session_state.uploaded_file:
#             if st.button("ANALYZE") :
#                 with st.spinner("ANALYZING"):
#                     try:
#                         dis = display(st.session_state.uploaded_file, st.session_state.api_key)
#                         try:
#                             t_im = dis.request()
#                             st.session_state.text = t_im
#                             st.session_state.Image_text = t_im
#                         except:
#                             pass
#                         text = dis.analyze(st.session_state.text)
#                         st.session_state.text = text
#                         st.title("REPORT")
#                         st.write(st.session_state.text)

#                         if len(st.session_state.text) > 0:
#                             st.title("AI GENERATED SUMMARY")
#                             st.session_state.sum = dis.summary(st.session_state.text)
#                             st.write(st.session_state.sum)
#                         st.session_state.text += st.session_state.Image_text
#                         st.session_state.show_clicked = True
#                     except Exception as e:
#                         st.error(f"Error processing PDF: {e}")
#                 st.button("chat")
                

#     elif st.session_state.show_clicked:
#         print(st.session_state.show_clicked)
#         st.write(st.session_state.sum)
#         if "user_input" not in st.session_state:
#             st.session_state.user_input = None
#         st.session_state.user_input = st.text_input("You:", key="input")

#         if st.button("Send"):
#             if st.session_state.user_input:
#                 dis = display(st.session_state.uploaded_file, st.session_state.api_key)
#                 m = dis.get_openai_response(st.session_state.text, st.session_state.user_input)
#                 bot_response = m
#                 st.session_state.conversation.append({"role": "assistant", "content": bot_response})
#                 st.session_state.conversation.append({"role": "user", "content": st.session_state.user_input})

#         for i in range(len(st.session_state.conversation)):
#             message = st.session_state.conversation[len(st.session_state.conversation) - i - 1]
#             if message["role"] == "assistant":
#                 st.write(f"**bot:** {message['content']}")
#             else:
#                 st.write("__________________________________________________________________________________________________________________________________________")
#                 st.write(f"**user:** {message['content']}")

# except Exception as e:
#     st.error(f"Unexpected error: {e}")

            







































































