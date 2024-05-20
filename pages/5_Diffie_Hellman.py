import streamlit as st
from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os

from nav import navi

st.set_page_config(
    page_title="RSA",
    page_icon="🔐",
    layout="wide"
)

navi()

st.markdown("""
    <style>
         textarea {
            color: #fb6f92 !important;
         }
    </style>
""", unsafe_allow_html=True)

st.header("Welcome to Simple Diffie Hellman!🔐")
st.header('Diffie Hellman', divider='rainbow')

on = st.toggle("Show History")

if on:
    st.write('The Diffie-Hellman key exchange, introduced by Whitfield Diffie and Martin Hellman in 1976, revolutionized modern cryptography by enabling secure communication over insecure channels without the need for pre-shared secrets. Their groundbreaking paper, "New Directions in Cryptography," laid the foundation for public-key cryptography, paving the way for the development of secure internet communication protocols and serving as a cornerstone in the field of modern cryptography.')

# Function to generate DH parameters and keys
def generate_dh_parameters():
    parameters = dh.generate_parameters(generator=2, key_size=2048)
    private_key = parameters.generate_private_key()
    public_key = private_key.public_key()
    return parameters, private_key, public_key

def serialize_key(key):
    return key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

def derive_shared_key(private_key, peer_public_key):
    shared_key = private_key.exchange(peer_public_key)
    derived_key = HKDF(
        algorithm=hashes.SHA256(),
        length=32,
        salt=None,
        info=b'handshake data'
    ).derive(shared_key)
    return derived_key

def encrypt_message(message, key):
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv))
    encryptor = cipher.encryptor()
    encrypted_message = iv + encryptor.update(message.encode()) + encryptor.finalize()
    return encrypted_message

def decrypt_message(encrypted_message, key):
    iv = encrypted_message[:16]
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv))
    decryptor = cipher.decryptor()
    decrypted_message = decryptor.update(encrypted_message[16:]) + decryptor.finalize()
    return decrypted_message.decode()

# Generate DH Parameters and Keys
if 'private_key' not in st.session_state:
    st.session_state.parameters, st.session_state.private_key, st.session_state.public_key = generate_dh_parameters()

if st.button("Generate Diffie-Hellman Keys"):
    st.session_state.parameters, st.session_state.private_key, st.session_state.public_key = generate_dh_parameters()
    st.text_area("Your Public Key", serialize_key(st.session_state.public_key).decode(), height=200)

# Encrypt Message
peer_public_key_pem = st.text_area("Peer Public Key (PEM format)", height=200)
message = st.text_input("Message to encrypt")

if st.button("Encrypt"):
    if peer_public_key_pem and message:
        try:
            peer_public_key = serialization.load_pem_public_key(peer_public_key_pem.encode())
            shared_key = derive_shared_key(st.session_state.private_key, peer_public_key)
            encrypted_message = encrypt_message(message, shared_key)
            st.text_area("Encrypted Message (hex)", encrypted_message.hex(), height=200)
        except Exception as e:
            st.error(f"Error during encryption: {e}")
    else:
        st.error("Please provide a peer public key and a message.")

# Decrypt Message
encrypted_message_hex = st.text_area("Encrypted Message (hex)", height=200)
peer_public_key_pem_decrypt = st.text_area("Peer Public Key (PEM format for decryption)", height=200)

if st.button("Decrypt"):
    if encrypted_message_hex and peer_public_key_pem_decrypt:
        try:
            peer_public_key = serialization.load_pem_public_key(peer_public_key_pem_decrypt.encode())
            encrypted_message = bytes.fromhex(encrypted_message_hex)
            shared_key = derive_shared_key(st.session_state.private_key, peer_public_key)
            message = decrypt_message(encrypted_message, shared_key)
            st.text_area("Decrypted Message", message, height=200)
        except Exception as e:
            st.error(f"Error during decryption: {e}")
    else:
        st.error("Please provide an encrypted message and the peer public key.")