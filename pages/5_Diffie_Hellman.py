import random
import streamlit as st
from nav import navi
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os

st.set_page_config(
    page_title="Encryption App",
    page_icon="🔐",
    layout="wide"
)

st.markdown("""
    <style>
         textarea {
            color: #fb6f92 !important;
         }
    </style>
""", unsafe_allow_html=True)

st.header("Welcome to Simple Encryption!🔐")
st.header('Encrypt and Decrypt', divider='rainbow')

# Function to encrypt a message using AES
def encrypt_message(key, plaintext):
    backend = default_backend()
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
    encryptor = cipher.encryptor()
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(plaintext.encode()) + padder.finalize()
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()
    return iv, ciphertext

# Function to decrypt a message using AES
def decrypt_message(key, iv, ciphertext):
    backend = default_backend()
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
    decryptor = cipher.decryptor()
    unpadder = padding.PKCS7(128).unpadder()
    padded_data = decryptor.update(ciphertext) + decryptor.finalize()
    plaintext = unpadder.update(padded_data) + unpadder.finalize()
    return plaintext.decode()

# Predefined shared secret key (must be 16 bytes for AES-128)
shared_secret_key = b'sixteen_byte_key'

# Streamlit app
st.title("Encrypt and Decrypt a Message")

# Input field for plaintext message
plaintext = st.text_area("Enter a message to encrypt")

if plaintext:
    iv, ciphertext = encrypt_message(shared_secret_key, plaintext)
    st.write("Encrypted message (hex):", ciphertext.hex())

    # Decrypt the message
    decrypted_message = decrypt_message(shared_secret_key, iv, ciphertext)
    st.write("Decrypted message:", decrypted_message)
