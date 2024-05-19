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

st.header("Welcome to Simple Diffie Hellman!🔐")
st.header('Deffie Hellman', divider='rainbow')

on = st.toggle("Show History")

if on:
    st.write('The Diffie-Hellman key exchange, introduced by Whitfield Diffie and Martin Hellman in 1976, revolutionized modern cryptography by enabling secure communication over insecure channels without the need for pre-shared secrets. Their groundbreaking paper, "New Directions in Cryptography," laid the foundation for public-key cryptography, paving the way for the development of secure internet communication protocols and serving as a cornerstone in the field of modern cryptography.')
# Function to perform modular exponentiation (base^exponent mod modulus)

def generate_private_number(p):
    pri_key = random.randint(1, p - 1)
    # print("random:", pri_key)
    return pri_key


def generate_public_key(pub_key, p, g):
    print("\t\t\t", g, '^', pub_key, "mod", p, "=", pow(g, pub_key, p))
    pub_key = pow(g, pub_key, p)
    return pub_key


def generate_shared_secret(private_key, public_key, p):
    st.write("\t\t\t", public_key, '^', private_key, "mod",
          p, "=", pow(public_key, private_key, p))
    shrd_key = pow(public_key, private_key, p)
    return shrd_key


def encrypt_message(message, shared_secret):
    # XOR the message with the shared secret to encrypt the message
    for c in message:
        st.write(f"{chr(ord(c))} = {ord(c)} ^ {shared_secret} = {ord(c) ^ shared_secret} = {chr(ord(c) ^ shared_secret)}")
    encrypted_message = ''.join(chr(ord(c) ^ shared_secret) for c in message)
    return encrypted_message


def decrypt_message(encrypted_message, shared_secret):
    # XOR the encrypted message with the shared secret to decrypt the message
    for c in encrypted_message:
        st.write(f"{chr(ord(c))} = {ord(c)} ^ {shared_secret} = {ord(c) ^ shared_secret} = {chr(ord(c) ^ shared_secret)}")
    message = ''.join(chr(ord(c) ^ shared_secret) for c in encrypted_message)
    return message

# Example usage:


# Select two large prime numbers, p and g
# p = 17
# g = 3
p = 100043
g = 100003

st.write("Bob and alice agreement:", g, "mod", p)

# Generate private keys
alice_private_num = generate_private_number(p)
st.write("alice_private_num:\t", alice_private_num)
bob_private_num = generate_private_number(p)
st.write("bob_private_num:\t", bob_private_num)


# Generate public keys
st.write("alice_public_key:")
alice_public_key = generate_public_key(alice_private_num, p, g)
st.write("bob_public_key:")
bob_public_key = generate_public_key(bob_private_num, p, g)

# Exchange public keys

# Generate shared secret
st.write("alice_shared_secret:")
alice_shared_secret = generate_shared_secret(alice_private_num, bob_public_key, p)
st.write("bob_shared_secret:")
bob_shared_secret = generate_shared_secret(bob_private_num, alice_public_key, p)

# The shared secrets generated by both parties should be the same
assert alice_shared_secret == bob_shared_secret

# Alice encrypts a message
message = "Hello Bob, how are you?"
encrypted_message = encrypt_message(message, alice_shared_secret)
print("\nencrypted_message:", encrypted_message)
# Bob decrypts the message
# you can try alice_shared_secret key to decrypt the message
decrypted_message = decrypt_message(encrypted_message, bob_shared_secret)
st.write("bob decryption using his shared_secret_key:", decrypted_message)


decrypted_message = decrypt_message(encrypted_message, alice_shared_secret)
st.write("bob decryption using alice's shared_secret_key:", decrypted_message)

# trying to decrypt the message using a number. output with error
st.write("\nEve trying to decrypt the message using a random key")
decrypted_message = decrypt_message(encrypted_message, 2334)
st.write("decrypted_message:", decrypted_message)  #

# The decrypted message should be the same as the original message
assert message == decrypted_message, "Decryption error"