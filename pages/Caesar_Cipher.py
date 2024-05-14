import streamlit as st
from nav import navi 

st.set_page_config(
        page_title="Caesar Cipher",
        page_icon="🔐",
        layout="wide"
    )

navi()

st.header(" Welcome to Caesar Cipher!🔐")
st.header('CAESAR CIPHER', divider='rainbow')

def encrypt_decrypt(text, shift_keys, ifdecrypt):
    result = ""
    shift_keys_len = len(shift_keys)
    
    for i, char in enumerate(text):
            
            shift_key = shift_keys[i % shift_keys_len] if not ifdecrypt else -shift_keys[i % shift_keys_len]
            
            result += chr((ord(char) + shift_key - 32) % 94 + 32)
            st.write(i, char, shift_keys[i % shift_keys_len], result[i])
    st.write("----------")
    
    return result 

text = st.text_input('Text')
shift_keys = st.text_input('Shift Keys').strip("[]").split()
shift_keys = list(map(int, shift_keys))


if st.button('Submit', type="primary"):
        if not text:
            st.warning('Please input text!!')
        elif not shift_keys:
            st.warning('Please input shift keys!!')
        else:
            encrypted = encrypt_decrypt(text, shift_keys, False)
            decrypted = encrypt_decrypt(encrypted, shift_keys, True)
            st.write("Text:", text)
            st.write("Shift keys:", " ".join(map(str, shift_keys)))
            st.write("Cipher:", encrypted)
            st.write("Decrypted text:", decrypted)