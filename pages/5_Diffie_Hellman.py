import random
import streamlit as st

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
    st.write('lovelove')
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