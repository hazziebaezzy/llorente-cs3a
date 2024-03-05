import streamlit as st

st.header("Block Cipher🔐")
st.sidebar.write("Block Cipher🔐")

st.write('Welcome to Block Cipher!!')

def pad(data, block_size):    # CMS (Cryptographic Message Syntax). This pads with the same value as the number of padding bytes.
    # Calculate the number of bytes needed to reach a multiple of block size.
    padding_length = block_size - len(data) % block_size  
    
    # Create the padding by repeating the padding length byte.
    padding = bytes([padding_length] * padding_length)  
    
    # Add the padding to the original data.
    return data + padding                          

def unpad(data):
    # Extract the padding length from the last byte of the data
    padd_length = data[-1]  # The last byte of the data indicates the length of the padding
    
    # Remove the padding by slicing the data, excluding the last 'padding_length' bytes
    # This effectively removes the padding from the data
    return data[:-padd_length]  # Return the data without the padding

def xor_encrypt_block(plaintext_block, key):
    # Initialize an empty bytes object to store the encrypted block
    encrypted_block = b''
    # Iterate through each byte in the plaintext block
    for i in range(len(plaintext_block)):
        # XOR each byte of the plaintext block with the corresponding byte of the key
        # Use modulus operator to ensure that key bytes are reused if the key length is shorter than the plaintext block length
        encrypted_block += bytes([plaintext_block[i] ^ key[i % len(key)]])
        
    # Return the encrypted block
    return encrypted_block                 

def xor_decrypt_block(ciphertext_block, key):
    return xor_encrypt_block(ciphertext_block, key)  # XOR decryption is same as encryption

def xor_encrypt(plaintext, key, block_size):
    # Initialize an empty bytes object to store the encrypted data
    encrypted_data = b''
    
    # Pad the plaintext to ensure its length is a multiple of the block size
    padded_plaintext = pad(plaintext, block_size)
    st.write('Encrypted blocks')
    # Iterate through the plaintext in blocks of size block_size
    for x, i in enumerate(range(0, len(padded_plaintext), block_size)):
        # Extract a block of plaintext
        plaintext_block = padded_plaintext[i:i+block_size]
        st.write(f"Plain block[{x}]: {plaintext_block.hex()} : {plaintext_block}")
        # Encrypt the plaintext block using XOR with the key
        encrypted_block = xor_encrypt_block(plaintext_block, key)
        # Append the encrypted block to the encrypted data
        encrypted_data += encrypted_block
        st.write(f"Cipher block[{x}]: {encrypted_block.hex()} : {encrypted_block}")
    # Return the encrypted data
    return encrypted_data                            

def xor_decrypt(ciphertext, key, block_size):
    # Initialize an empty bytes object to store the decrypted data
    decrypted_data = b''
    st.write('Decrypted blocks')
    # Iterate through the ciphertext in blocks of size block_size
    for x, i in enumerate(range(0, len(ciphertext), block_size)):
        # Extract the current block of ciphertext
        ciphertext_block = ciphertext[i:i+block_size]
        
        # Decrypt the current block using xor_decrypt_block function
        decrypted_block = xor_decrypt_block(ciphertext_block, key)
        # Append the decrypted block to the decrypted data
        decrypted_data += decrypted_block
        st.write(f"block[{x}]: {decrypted_block.hex()}: {decrypted_block}")
    # Remove any padding from the decrypted data
    unpadded_decrypted_data = unpad(decrypted_data)
    
    # Return the unpadded decrypted data
    return unpadded_decrypted_data                               

if __name__ == "__main__":

    # Define the plaintext and encryption key
    plaintext = bytes(st.text_area('Plaintext').encode())
    key = bytes(st.text_area('Key').encode())
    block_size = int(st.number_input('Block Size', step=1, format="%d", placeholder="Insert a number..."))
    sbn_submit = st.button('Submit', type="primary")

if sbn_submit:  
    if block_size not in [8, 16, 32, 64, 128]:
        st.write('Block size must be one of 8, 16, 32, 64, or 128 bytes')
    else:
        key = pad(key, block_size)   # Pad the key

    # Define the block size for encryption (adjust according to your needs
    # Encryption
        encrypt_data = xor_encrypt(plaintext, key, block_size)
    # Decryption
        decrypt_data = xor_decrypt(encrypt_data, key, block_size)

        st.write("\nOriginal plaintext:", plaintext)
        st.write("Key byte      :", key)
        st.write("Key hex       :", key.hex())
        st.write("Encrypted data:", encrypt_data.hex())  # Print encrypted data in hexadecimal format
        st.write("Decrypted data:", decrypt_data.hex())
        st.write("Decrypted data:", decrypt_data)
        st.balloons()
        st.snow()

# print(b'Hello Bob, this '.hex())
