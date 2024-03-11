import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Hello",
        page_icon="👋",
    )

    st.write("# Welcome to Applied Cryptography! 👋")
    st.write("By: Hazel Llorente")
    
    st.sidebar.success("Select a demo above.")

    st.markdown(
        """
        [XOR Cipher](https://fantastic-carnival-7vw4q4444pjfw699-8501.app.github.dev/)
        Jump into our [documentation](https://docs.streamlit.io)
        Ask a question in our [community
          forums](https://discuss.streamlit.io)
        Use a neural net to [analyze the Udacity Self-driving Car Image
          Dataset](https://github.com/streamlit/demo-self-driving)
        Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
    """
    )


if __name__ == "__main__":
    run()