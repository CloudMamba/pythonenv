from tkinter import *
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# Define AES encryption and decryption functions
def encrypt_message(key, message):
    cipher = AES.new(key, AES.MODE_CBC)
    iv = cipher.iv
    encrypted_message = cipher.encrypt(pad(message.encode('utf-8'), AES.block_size))
    return iv + encrypted_message

def decrypt_message(key, encrypted_message):
    iv = encrypted_message[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    decrypted_message = unpad(cipher.decrypt(encrypted_message[AES.block_size:]), AES.block_size)
    return decrypted_message.decode('utf-8')

# Create the tkinter GUI
root = Tk()
root.title("AES Encryption and Decryption")

# Define the key entry field
key_label = Label(root, text="Enter the key:")
key_label.grid(row=0, column=0)
key_entry = Entry(root, show="*")
key_entry.grid(row=0, column=1)

# Define the message entry field
message_label = Label(root, text="Enter the message:")
message_label.grid(row=1, column=0)
message_entry = Entry(root)
message_entry.grid(row=1, column=1)

# Define the encryption button
def encrypt():
    key = key_entry.get().encode('utf-8')
    message = message_entry.get()
    encrypted_message = encrypt_message(key, message)
    result_label.config(text=f"Encrypted message: {encrypted_message.hex()}")

encrypt_button = Button(root, text="Encrypt", command=encrypt)
encrypt_button.grid(row=2, column=0)

# Define the decryption button
def decrypt():
    key = key_entry.get().encode('utf-8')
    encrypted_message = bytes.fromhex(message_entry.get())
    decrypted_message = decrypt_message(key, encrypted_message)
    result_label.config(text=f"Decrypted message: {decrypted_message}")

decrypt_button = Button(root, text="Decrypt", command=decrypt)
decrypt_button.grid(row=2, column=1)

# Define the result label
result_label = Label(root, text="")
result_label.grid(row=3, column=0, columnspan=2)

# Run the GUI loop
root.mainloop()

