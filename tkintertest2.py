from tkinter import *
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def aes_encrypt(key, message):
    cipher = AES.new(key, AES.MODE_CBC)
    iv = cipher.iv
    return iv + cipher.encrypt(pad(message.encode('utf-8'), AES.block_size))

def aes_decrypt(key, encrypted_message):
    iv = encrypted_message[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    return unpad(cipher.decrypt(encrypted_message[AES.block_size:]), AES.block_size).decode('utf-8')

def create_label(master, text, row, column, columnspan=1):
    label = Label(master, text=text)
    label.grid(row=row, column=column, columnspan=columnspan)
    return label

def create_entry(master, row, column):
    entry = Entry(master)
    entry.grid(row=row, column=column)
    return entry

def create_button(master, text, command, row, column):
    button = Button(master, text=text, command=command)
    button.grid(row=row, column=column)
    return button

def create_result_label(master, row, column, columnspan=2):
    return create_label(master, "", row, column, columnspan)

def create_key_entry(master, row, column):
    entry = create_entry(master, row, column+1)
    create_label(master, "Enter the key:", row, column)
    return entry

def create_message_entry(master, row, column):
    entry = create_entry(master, row, column+1)
    create_label(master, "Enter the message:", row, column)
    return entry

def create_encrypt_button(master, key_entry, message_entry, result_label):
    create_button(master, "Encrypt", lambda: result_label.config(text=f"Encrypted message: {aes_encrypt(key_entry.get().encode('utf-8'), message_entry.get()).hex()}"), 2, 0)

def create_decrypt_button(master, key_entry, message_entry, result_label):
    create_button(master, "Decrypt", lambda: result_label.config(text=f"Decrypted message: {aes_decrypt(key_entry.get().encode('utf-8'), bytes.fromhex(message_entry.get()))}"), 2, 1)

root = Tk()
root.title("AES Encryption and Decryption")

key_entry = create_key_entry(root, 0, 0)
message_entry = create_message_entry(root, 1, 0)
result_label = create_result_label(root, 3, 0)

create_encrypt_button(root, key_entry, message_entry, result_label)
create_decrypt_button(root, key_entry, message_entry, result_label)

root.mainloop()

