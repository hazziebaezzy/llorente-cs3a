import random
import streamlit as st
from nav import navi
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os

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

# Function to perform modular exponentiation (base^exponent mod modulus)
def mod_exp(base, exponent, modulus):
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent //= 2
        base = (base * base) % modulus
    return result

# Function to generate keys for Alice and Bob
def generate_keys(p, g):
    # Choose private keys for Alice and Bob
    a = random.randint(2, p - 2)
    b = random.randint(2, p - 2)
    # Compute public keys for Alice and Bob
    A = mod_exp(g, a, p)
    B = mod_exp(g, b, p)
    return a, A, b, B

# Function to compute shared secret
def compute_shared_secret(key, other_public_key, p):
    # Compute shared secret
    shared_secret = mod_exp(other_public_key, key, p)
    return shared_secret

# Function to encrypt a message using AES
def encrypt_message(shared_secret, plaintext):
    backend = default_backend()
    key = shared_secret.to_bytes(16, byteorder='big')
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
    encryptor = cipher.encryptor()
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(plaintext.encode()) + padder.finalize()
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()
    return iv, ciphertext

# Function to decrypt a message using AES
def decrypt_message(shared_secret, iv, ciphertext):
    backend = default_backend()
    key = shared_secret.to_bytes(16, byteorder='big')
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
    decryptor = cipher.decryptor()
    unpadder = padding.PKCS7(128).unpadder()
    padded_data = decryptor.update(ciphertext) + decryptor.finalize()
    plaintext = unpadder.update(padded_data) + unpadder.finalize()
    return plaintext.decode()

# Streamlit app
st.title("Diffie-Hellman Key Exchange")

# Input fields for prime modulus and base
p = st.number_input("Enter prime modulus (p)", value=89)
g = st.number_input("Enter base (g)", value=5)

# Button to generate keys and compute shared secret
if st.button("Generate Keys and Compute Shared Secret"):
    # Generate keys for Alice and Bob
    alice_private_key, alice_public_key, bob_private_key, bob_public_key = generate_keys(p, g)

    # Compute shared secret for Alice and Bob
    alice_shared_secret = compute_shared_secret(alice_private_key, bob_public_key, p)
    bob_shared_secret = compute_shared_secret(bob_private_key, alice_public_key, p)

    # Display shared secrets
    st.write("Alice's shared secret:", alice_shared_secret)
    st.write("Bob's shared secret:", bob_shared_secret)

    # Check if shared secrets match
    if alice_shared_secret == bob_shared_secret:
        st.write("Shared secrets match. Ready to encrypt and decrypt messages.")
    else:
        st.write("Shared secrets do not match. Please try again.")

    # Input field for plaintext message
    plaintext = st.text_area("Enter a message to encrypt")

    if plaintext:
        iv, ciphertext = encrypt_message(alice_shared_secret, plaintext)
        st.write("Encrypted message:", ciphertext)

        # Decrypt the message
        decrypted_message = decrypt_message(bob_shared_secret, iv, ciphertext)
        st.write("Decrypted message:", decrypted_message)
