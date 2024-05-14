import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="navi",
        page_icon="👋",
    )

    st.write("# Welcome to Streamlit! 👋")

def navi():
    columns = st.columns((1,1,1,1,1))
    columns2 = st.columns((1, 1, 1, 1))

    with columns[0]:
        st.page_link("pages/1_Reverse_Cipher.py", label="Reverse Cipher", icon="🗝️", use_container_width=True)
    with columns[1]:
        st.page_link("pages/2_ROT13.py", label="ROT13", icon="🗝️", use_container_width=True)
    with columns[2]:
        st.page_link("pages/3_Simple_Substitution_Cipher.py", label="Simple Substitution Cipher", icon="🗝️", use_container_width=True)
    with columns[3]:
        st.page_link("pages/4_RSA.py", label="RSA", icon="🗝️", use_container_width=True)
    with columns[4]:
        st.page_link("pages/5_Diffie_Hellman.py", label="Diffie Hellman", icon="🗝️", use_container_width=True)
    st.markdown('---')
    with columns2[0]:
        st.page_link("pages/6_MD5_Hash.py", label="MD5", icon="🗝️", use_container_width=True)
    with columns2[1]:
        st.page_link("pages/7_Sha1.py", label="SHA1", icon="🗝️", use_container_width=True)
    with columns2[2]:
        st.page_link("pages/8_Blake2.py", label="BLAKE2", icon="🗝️", use_container_width=True)
    with columns2[3]:
        st.page_link("pages/9_RIPEMD-160.py", label="WHIRLPOOL", icon="🗝️", use_container_width=True)


if __name__ == "__main__":
    run()