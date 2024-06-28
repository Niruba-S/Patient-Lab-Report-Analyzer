import streamlit as st
import os
from dotenv import load_dotenv
from module import display

def main():
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
        # Your home page code here

    elif st.session_state.page == "chatbot":
        # Your chatbot page code here

if __name__ == "__main__":
    main()
    st.run(host="0.0.0.0", port=8001)







































