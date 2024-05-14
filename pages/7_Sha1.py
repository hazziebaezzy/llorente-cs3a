import streamlit as st
import hashlib
import pandas as pd

from nav import navi

st.set_page_config(
        page_title="Sha1",
        page_icon="🔐",
        layout="wide"
    )

navi()

st.markdown("""
    <style>
        body {
            background-color: lightblue !important;
        }
        .stButton button {
            background-color: #ff8fab !important;
            border: none;
        }
        .stButton button:hover {
            background-color: #fb6f92 !important;
            border: none;
        }
         textarea {
            color: #fb6f92 !important;
         }

        input {
            color: #fb6f92 !important;
            padding: 20px !important;
        }  
            
    </style>
""", unsafe_allow_html=True)

st.header("Welcome to SHA1!🔐")
st.header('SHA1', divider='rainbow')

on = st.toggle("Show History")

if on:
    st.write("Secure Hash Algorithm 1, or SHA-1, was developed in 1993 by the U.S. government's standards agency National Institute of Standards and Technology (NIST). It is widely used in security applications and protocols, including TLS, SSL, PGP, SSH, IPsec, and S/MIME. SHA-1 works by feeding a message as a bit string of length less than 2 ^ 64 bits, and producing a 160-bit hash value known as a message digest. ")

def compute_sha1(input_string):
    # Create a SHA-1 hash object
    sha1_hash = hashlib.sha1()

    # Update the hash object with the input string
    sha1_hash.update(input_string.encode('utf-8'))

    # Get the hexadecimal representation of the hash value
    hex_digest = sha1_hash.hexdigest()

    return hex_digest

genre = st.radio(
    "Choose Input",
    ["Text", "File"])

if genre == 'Text':
    st.write('You selected Text.')
    input_string = st.text_area('Plaintext', placeholder="Input Text...")
    button = st.button("Submit", type="primary")

    if button:
        if input_string:  # Check if input_string is not empty
            sha1_hash = compute_sha1(input_string)
            st.text_input("SHA1 hash", value=sha1_hash)
        else:
            st.warning("Please input text for SHA1 hash to work!")

elif genre == 'File':
    st.write('You selected File.')
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        # Read file contents as string
        file_contents = uploaded_file.getvalue().decode("utf-8")
        data = File.read(65536) 
        st.write("File contents:", file_contents)

        # Compute SHA1 hash of file contents
        sha1_hash = compute_sha1(file_contents)
        st.write("SHA1 hash of file contents:", sha1_hash)
        
else:
    st.write("Please choose.")