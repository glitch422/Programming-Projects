from cryptography.fernet import Fernet

# Generate a random encryption key 
key = Fernet.generate_key()

def encrypt_text(text, key):
  #Create a Fernet symetric encryption object with the provided key
  cipher = Fernet(key)

  #Encode the text to bytes
  encoded_text = text.encode()

  #Encrypt the text with the key
  encrypted_text = cipher.encrypt(encoded_text)

  #Return the base64-encoded encrypted text
  return encrypted_text.decode()

def decrypt_text(encrypted_text, key):
  #Create a Fernet symetric encryption object with the provided key
  cipher = Fernet(key)

  #Decode the base64-encoded encrypted text to bytes
  decode_text = encrypted_text.encode()

  #Decrypt the text with the key
  decrypted_text = cipher.decrypt(decode_text)

  #Return the decrypted text as a string
  return decrypted_text.decode()


# Example usage
plaintext = input('Write text here to encrpyt: ')
encrypted = encrypt_text(plaintext, key)
decrypted = decrypt_text(encrypted, key)

print('Original text:', plaintext)
print('Encrpyted text:', encrypted)
print('Decrypted text:', decrypted)
