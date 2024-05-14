import streamlit as st

def navi():
    columns = st.columns((1,1,1,1,1))
    columns2 = st.columns((1, 1, 1, 1))

    with columns[0]:
        st.page_link("pages/Reverse_Cipher.py", label="Reverse Cipher", icon="🗝️", use_container_width=True)
    with columns[1]:
        st.page_link("pages/ROT13.py", label="ROT13", icon="🗝️", use_container_width=True)
    with columns[2]:
        st.page_link("pages/Simple_Substitution_Cipher.py", label="Simple Substitution Cipher", icon="🗝️", use_container_width=True)
    with columns[3]:
        st.page_link("pages/RSA.py", label="RSA", icon="🗝️", use_container_width=True)
    with columns[4]:
        st.page_link("pages/Diffie_Hellman.py", label="Diffie Hellman", icon="🗝️", use_container_width=True)
    st.markdown('---')
    with columns2[0]:
        st.page_link("pages/MD5_Hash.py", label="MD5", icon="🗝️", use_container_width=True)
    with columns2[1]:
        st.page_link("pages/Sha1.py", label="SHA1", icon="🗝️", use_container_width=True)
    with columns2[2]:
        st.page_link("pages/Blake2.py", label="BLAKE2", icon="🗝️", use_container_width=True)
    with columns2[3]:
        st.page_link("pages/RIPEMD-160.py", label="WHIRLPOOL", icon="🗝️", use_container_width=True)
   