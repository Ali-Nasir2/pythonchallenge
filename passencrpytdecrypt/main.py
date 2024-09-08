import os
import base64
from cryptography.fernet import Fernet

KEY_FILE = "give location of key file"
PASSWORD_FILE = "give location of password file"

# Generate a key for encryption and save it to a text file with the medium name
def generate_key(medium):
    key = base64.urlsafe_b64encode(os.urandom(32)).decode()
    with open(KEY_FILE, "w") as key_file:
        key_file.write(f"Medium: {medium}\n")
        key_file.write(f"Key: {key}\n")
    return key

# Load the encryption key from a text file
def load_key(medium):
    if os.path.exists(KEY_FILE):
        with open(KEY_FILE, "r") as key_file:
            lines = key_file.readlines()
            key = lines[1].strip().split(": ")[1]
            return key.encode()
    else:
        return generate_key(medium).encode()

# Encrypt a password
def encrypt_password(key, password):
    f = Fernet(key)
    return f.encrypt(password.encode())

# Decrypt a password
def decrypt_password(key, encrypted_password):
    f = Fernet(key)
    return f.decrypt(encrypted_password).decode()

# Save password to a text file
def save_password(medium, encrypted_password, filename=PASSWORD_FILE):
    with open(filename, "a") as file:
        file.write(f"Medium: {medium}\n")
        file.write(f"Encrypted Password: {encrypted_password}\n")
        file.write("-" * 40 + "\n")

# Read and decrypt passwords from the text file
def read_passwords(key, filename=PASSWORD_FILE):
    with open(filename, "r") as file:
        lines = file.readlines()
        for i in range(0, len(lines), 4):
            medium = lines[i].strip().split(": ")[1]
            encrypted_password = lines[i+1].strip().split(": ")[1]
            decrypted_password = decrypt_password(key, encrypted_password.encode())
            print(f"Medium: {medium}")
            print(f"Decrypted Password: {decrypted_password}")
            print("-" * 40)

# Main function
def main():
    while True:
        choice = input("Do you want to (E)ncrypt or (D)ecrypt a password? (Q to quit) ").strip().upper()

        if choice == 'E':
            medium = input("Enter the medium (e.g., Facebook, Binance): ")
            key = load_key(medium)
            password = input("Enter the password: ")
            encrypted_password = encrypt_password(key, password)
            save_password(medium, encrypted_password.decode())
            print(f"Password for {medium} has been encrypted and saved.")
        elif choice == 'D':
            user_key = input("Enter the 32-bit key for decryption: ").strip()
            try:
                read_passwords(user_key.encode())
            except Exception as e:
                print(f"Failed to decrypt passwords: {e}")
        elif choice == 'Q':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select either 'E' for encrypt, 'D' for decrypt, or 'Q' to quit.")

if __name__ == "__main__":
    main()
