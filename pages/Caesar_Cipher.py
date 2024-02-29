import streamlit as st

st.header("Caesar Cipher🔐")
st.sidebar.write("Caesar Cipher🔐")


st.write("Welcome to Caesar Cipher!!")

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
            encrypted_text = encrypt_decrypt(text, shift_keys, False)
            decrypted_text = encrypt_decrypt(encrypted_text, shift_keys, True)
            st.write("Text:", text)
            st.write("Shift keys:", " ".join(map(str, shift_keys)))
            st.write("Cipher:", encrypted_text)
            st.write("Decrypted text:", decrypted_text)
            st.balloons()
            st.snow()