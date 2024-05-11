import streamlit as st
import hashlib
import pandas as pd

from nav import navi

st.set_page_config(
        page_title="Blake2",
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
            background-color: #02c39a !important;
            border: none;
        }
        .stButton button:hover {
            background-color: #00a896 !important;
            border: none;
        }
         textarea {
            color: #00a896 !important;
         }

          
            
    </style>
""", unsafe_allow_html=True)

st.header("Welcome to BLAKE2!🔐")
st.header('BLAKE2', divider='rainbow')

on = st.toggle("Show History")

if on:
    st.write("BLAKE2 is a cryptographic hash function faster than MD5, SHA-1, SHA-2, and SHA-3, yet is at least as secure as the latest standard SHA-3. BLAKE2 has been adopted by many projects due to its high speed, security, and simplicity.  The BLAKE2 cryptographic hash function [BLAKE2] was designed by Jean-Philippe Aumasson, Samuel Neves, Zooko Wilcox-O'Hearn, and Christian Winnerlein.")

def compute_blake2(input_string):
    # Create a BLAKE2 hash object
    blake2_hash = hashlib.blake2b()

    # Update the hash object with the input string
    blake2_hash.update(input_string.encode('utf-8'))

    # Get the hexadecimal representation of the hash value
    hex_digest = blake2_hash.hexdigest()

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
            blake2_hash = compute_blake2(input_string)
            st.text_area("BLAKE2 hash", value=blake2_hash, height=150)
        else:
            st.warning("Please input text for BLAKE2 hash to work!")

elif genre == 'File':
    st.write('You selected File.')
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        # Read file contents as string
        file_contents = uploaded_file.getvalue().decode("utf-8")
        st.write("File contents:", file_contents)

        # Compute BLAKE2 hash of file contents
        blake2_hash = compute_blake2(file_contents)
        st.write("BLAKE2 hash of file contents:", blake2_hash)
        
else:
    st.write("Please choose.")