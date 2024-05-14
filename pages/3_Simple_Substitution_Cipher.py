import string
import streamlit as st

from nav import navi

st.set_page_config(
        page_title="Simple Substitution Cipher",
        page_icon="🔐",
        layout="wide"
    )

navi()

st.header("Welcome to Simple Substitution Cipher!🔐")
st.header('Simple Substitution Cipher', divider='rainbow')

on = st.toggle("Show History")

if on:
    st.write("It was one of the earliest methods used to encrypt messages. It's a type of monoalphabetic substitution cipher, meaning each letter in the plaintext is replaced with another letter consistently throughout the message. It is basically consists of substituting every plaintext character for a different ciphertext character. Unlike the Caesar cipher, which shifts the alphabet by a set number, the simple substitution cipher employs a completely randomized cipher alphabet.")

def generate_substitution_key(shift):
    """
    Generate a substitution key based on a given shift.
    """
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    substitution_key = dict(zip(alphabet, shifted_alphabet))
    return substitution_key

def encrypt(plaintext, substitution_key):
    """
    Encrypt the plaintext using the substitution key.
    """
    ciphertext = ''
    for char in plaintext.lower():
        if char in substitution_key:
            ciphertext += substitution_key[char]
        else:
            ciphertext += char
    return ciphertext

def decrypt(ciphertext, substitution_key):
    """
    Decrypt the ciphertext using the substitution key.
    """
    decryption_key = {v: k for k, v in substitution_key.items()}
    plaintext = ''
    for char in ciphertext.lower():
        if char in decryption_key:
            plaintext += decryption_key[char]
        else:
            plaintext += char
    return plaintext


genre = st.selectbox(
    "What type of content do you want?",
    ["Text", "File"])

if genre == 'Text':
    shift = 5
    substitution_key = generate_substitution_key(shift)
    plaintext = st.text_input('Enter a Plaintext')
    option = st.radio('Choose process', options=('Encrypt', 'Decrypt'))

    if option == 'Encrypt':
        btn = st.button('Submit', type='primary')
        if btn:
            if not plaintext:
                st.warning('Please enter a text to encrypt!')
            else:
                encrypted_text = encrypt(plaintext, substitution_key)
                st.write("Encrypted Plaintext:", encrypted_text)

    elif option == 'Decrypt':
                    # Decrypt plaintext using Simple Substitution Cipher
                    ciphertext = st.text_input('Enter the ciphertext to decrypt')
                    decrypted_text = decrypt(ciphertext, substitution_key)
                    btn = st.button('Submit', type='primary')
                    if btn:
                        if not ciphertext:
                            st.warning('Please input a text to decrypt!')
                        else:
                            st.write("Decrypted Ciphertext:", decrypted_text) 

elif genre == 'File':
    st.write('You selected File.')
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        # Read file contents as string
        file_contents = uploaded_file.getvalue().decode("utf-8")
        st.write("File contents:", file_contents)

        radio = st.radio("Choose process", options=("Encypt", "Decrypt"))

        if radio == 'Encypt':
            substitute = encrypt(file_contents, generate_substitution_key(5))
            radio_btn = st.button('Submit', type='primary')
            if radio_btn:
                st.write("Encrypted File:", substitute)
        elif radio == 'Decrypt':
            ciphertext = st.text_input('Enter the ciphertext to decrypt')
            decrypt_subs = decrypt(ciphertext, generate_substitution_key(5))
            btn = st.button('Submit', type='primary')
            if btn:
                    if not ciphertext:
                        st.warning('Please input a text to decrypt!')
                    else:
                        st.text_area("Decrypted Ciphertext:", decrypt_subs)
        
else:
    st.write("Please choose.")