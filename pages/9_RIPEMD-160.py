import hashlib
import streamlit as st

from nav import navi

st.set_page_config(
        page_title="RIPEMD-160",
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
            background-color: #7b2cbf !important;
            border: none;
        }
        .stButton button:hover {
            background-color: #5a189a !important;
            border: none;
        }
        input {
            color: #5a189a !important;
         }         
    </style>
""", unsafe_allow_html=True)

st.header("Welcome to RIPEMD-160!🔐")
st.header('RIPEMD-160', divider='rainbow')

on = st.toggle("Show History")

if on:
    st.write('RIPEMD-160, which stands for "RACE Integrity Primitives Evaluation Message Digest-160," is a cryptographic hash function developed by Hans Dobbertin, Antoon Bosselaers, and Bart Preneel in 1996. It was designed as an improvement over the original RIPEMD hash function, offering a longer output size and improved resistance against collision attacks. RIPEMD-160 gained recognition for its usage in various cryptographic applications, including digital signatures and data integrity verification, contributing to the broader landscape of secure communication and data protection.')

def compute_ripemd160(input_string):
    # Create a RIPEMD-160 hash object
    ripemd160_hash = hashlib.new('ripemd160')

    # Update the hash object with the input string
    ripemd160_hash.update(input_string.encode('utf-8'))

    # Get the hexadecimal representation of the hash value
    hex_digest = ripemd160_hash.hexdigest()

    return hex_digest

genre = st.radio(
    "Choose Input",
    ["Text", "File"])

if genre == 'Text':
    st.write('You selected Text.')
    input_string = st.text_area('Input Text', placeholder="Enter Text...")
    button = st.button("Submit", type="primary")

    if button:
        if input_string:  # Check if input_string is not empty
            ripemd160_hash = compute_ripemd160(input_string)
            st.text_input("RIPEMD-160 hash", ripemd160_hash)
        else:
            st.warning("Please input text for RIPEMD-160 hash to work!")

elif genre == 'File':
    st.write('You selected File.')
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        # Read file contents as string
        file_contents = uploaded_file.getvalue().decode("utf-8")
        st.write("File contents:", file_contents)

        # Compute RIPEMD-160 hash of file contents
        ripemd160_hash = compute_ripemd160(file_contents)
        st.write("RIPEMD-160 hash of file contents:", ripemd160_hash)
        
else:
    st.write("Please choose.")