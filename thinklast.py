from tkinter import *
from Crypto.Cipher import AES

class KeyEncryptor:
    def __init__(self):
        self.key = b'0123456789abcdef'
        self.encrypted_key = NONE
        
        self.root = Tk()
        self.root.title("Key Encryption and Decryption")
        
        self.create_key_entry()
        self.create_encrypt_button()
        self.create_decrypt_button()
        self.create_result_label()
        
        self.root.mainloop()
    
    def aes_encrypt(self, key, message):
        cipher = AES.new(key, AES.MODE_CBC)
        iv = cipher.iv
        return iv + cipher.encrypt(message)
    
    def aes_decrypt(self, key, encrypted_message):
        iv = encrypted_message[:AES.block_size]
        cipher = AES.new(key, AES.MODE_CBC, iv=iv)
        return cipher.decrypt(encrypted_message[AES.block_size:])

    def create_label(self, text, row, column, columnspan=1):
        label = Label(self.root, text=text)
        label.grid(row=row, column=column, columnspan=columnspan)
        return label

    def create_entry(self, row, column):
        entry = Entry(self.root)
        entry.grid(row=row, column=column)
        return entry

    def create_button(self, text, command, row, column):
        button = Button(self.root, text=text, command=command)
        button.grid(row=row, column=column)
        return button

    def create_result_label(self):
        self.result_label = self.create_label("", 3, 0, 2)

    def create_key_entry(self):
        self.key_entry = self.create_entry(0, 1)
        self.create_label("Enter the key:", 0, 0)

    def create_encrypt_button(self):
        self.create_button("Encrypt", self.encrypt_key, 2, 0)

    def create_decrypt_button(self):
        self.create_button("Decrypt", self.decrypt_key, 2, 1)

    def encrypt_key(self):
        self.key = self.key_entry.get().encode('utf-8')
        self.encrypted_key = self.aes_encrypt(self.key, self.key)
        self.result_label.config(text=f"Encrypted key: {self.encrypted_key.hex()}")

    def decrypt_key(self):
        if self.key is None:
            self.result_label.config(text="Please encrypt a key first.")
            return
        decrypted_key = self.aes_decrypt(self.key, self.encrypted_key)
        self.result_label.config(text=f"Decrypted key: {decrypted_key.decode('utf-8')}")

KeyEncryptor()

