import streamlit as st
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding

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
from nav import navi
# Streamlit UI
st.set_page_config(
    page_title="RSA Cryptography Application",
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

st.header("RSA Cryptography Application")

# State to store keys
if 'private_key' not in st.session_state:
    st.session_state.private_key = None
if 'public_key' not in st.session_state:
    st.session_state.public_key = None

# Generate RSA Keys
if st.button("Generate RSA Keys"):
    private_key, public_key = generate_rsa_keys()
    st.session_state.private_key = private_key
    st.session_state.public_key = public_key
    st.text_area("Private Key", serialize_key(private_key, private=True).decode(), height=200)
    st.text_area("Public Key", serialize_key(public_key).decode(), height=200)

# Encrypt Message
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

# Decrypt Message
encrypted_message_hex = st.text_area("Encrypted Message (hex)", height=200)
if st.button("Decrypt"):
    if st.session_state.private_key and encrypted_message_hex:
        try:
            encrypted_message = bytes.fromhex(encrypted_message_hex)
            message = decrypt_message(encrypted_message, st.session_state.private_key)
            st.text_area("Decrypted Message", message, height=200)
        except Exception as e:
            st.error(f"Error during decryption: {e}")
    else:
        st.error("Please generate RSA keys and provide an encrypted message.")
