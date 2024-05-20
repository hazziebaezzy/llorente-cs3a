import rsa
import streamlit as st
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding

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

st.header("Welcome to Simple RSA!🔐")
st.header('RSA', divider='rainbow')

on = st.toggle("Show History")

if on:
    st.write('The Rivest-Shamir-Adleman (RSA) encryption technique is asymmetric and commonly utilized in a variety of products and services. Asymmetric encryption employs a mathematically connected key pair to encrypt and decrypt data. A private and public key are generated, with the public key visible to everybody and the private key a secret known only to the key pair creator. With RSA, data can be encrypted using either the private or public key, and decrypted using the other key. This is one of the reasons why RSA is the most popular asymmetric encryption algorithm.')

# Function to generate RSA keys
def generate_rsa_keys():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )
    public_key = private_key.public_key()
    return private_key, public_key

# Function to serialize keys
def serialize_key(key, private=False):
    if private:
        return key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )
    else:
        return key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )

# Function to encrypt message
def encrypt_message(message, public_key):
    return public_key.encrypt(
        message.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

# Function to decrypt message
def decrypt_message(encrypted_message, private_key):
    return private_key.decrypt(
        encrypted_message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    ).decode()

# Streamlit UI
st.title("RSA Cryptography Application")

option = st.selectbox("Choose a task", ("Generate Keys", "Encrypt Message", "Decrypt Message"))

if option == "Generate Keys":
    if st.button("Generate RSA Keys"):
        private_key, public_key = generate_rsa_keys()
        st.text_area("Private Key", serialize_key(private_key, private=True).decode(), height=200)
        st.text_area("Public Key", serialize_key(public_key).decode(), height=200)

elif option == "Encrypt Message":
    public_key_pem = st.text_area("Public Key (PEM format)", height=200)
    message = st.text_input("Message to encrypt")
    if st.button("Encrypt"):
        if public_key_pem and message:
            try:
                public_key = serialization.load_pem_public_key(public_key_pem.encode())
                encrypted_message = encrypt_message(message, public_key)
                st.text_area("Encrypted Message (hex)", encrypted_message.hex(), height=200)
            except Exception as e:
                st.error(f"Error during encryption: {e}")
        else:
            st.error("Please provide a public key and a message.")

elif option == "Decrypt Message":
    private_key_pem = st.text_area("Private Key (PEM format)", height=200)
    encrypted_message_hex = st.text_area("Encrypted Message (hex)", height=200)
    if st.button("Decrypt"):
        if private_key_pem and encrypted_message_hex:
            try:
                private_key = serialization.load_pem_private_key(private_key_pem.encode(), password=None)
                encrypted_message = bytes.fromhex(encrypted_message_hex)
                message = decrypt_message(encrypted_message, private_key)
                st.text_area("Decrypted Message", message, height=200)
            except Exception as e:
                st.error(f"Error during decryption: {e}")
        else:
            st.error("Please provide a private key and an encrypted message.")
