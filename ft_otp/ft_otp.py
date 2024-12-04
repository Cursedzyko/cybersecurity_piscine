import sys
import time
from cryptography.fernet import Fernet

def validate_key(key):
    return len(key) == 64 and all(c in '0123456789abcdef' for c in key)

def save_enc_key(enc_key, enc_key_file='ft_otp.enc_key'):
    """Save the encryption key to a file."""
    with open(enc_key_file, 'wb') as file:
        file.write(enc_key)

def load_enc_key(enc_key_file='ft_otp.enc_key'):
    """Load the encryption key from a file."""
    try:
        with open(enc_key_file, 'rb') as file:
            return file.read()
    except FileNotFoundError:
        print("Error: Encryption key file not found.")
        sys.exit(1)

def encrypt_key(hex_key, enc_key_file='ft_otp.key'):
    """Encrypt the HOTP key and save it."""
    enc_key = Fernet.generate_key()
    save_enc_key(enc_key)  # Save the encryption key
    cipher_suite = Fernet(enc_key)
    encrypted_key = cipher_suite.encrypt(hex_key.encode())
    with open(enc_key_file, 'wb') as file:
        file.write(encrypted_key)

def decrypt_key(enc_key, enc_key_file='ft_otp.key'):
    """Decrypt the HOTP key."""
    try:
        with open(enc_key_file, 'rb') as file:
            encrypted_key = file.read()
        cipher_suite = Fernet(enc_key)
        return cipher_suite.decrypt(encrypted_key).decode()
    except Exception as e:
        print(f"Error while decrypting: {e}")
        sys.exit(1)

def generate_otp(hex_key, counter):
    pass

def main():
    if len(sys.argv) < 3:
        print("Usage: ./ft_otp -g <key_file> or ./ft_otp -k")
        return

    flag = sys.argv[1]
    if flag == "-g":
        key_file = sys.argv[2]
        with open(key_file, 'r') as file:
            hex_key = file.read().strip()

        if not validate_key(hex_key):
            print("./ft_otp: error: key must be 64 hexadecimal characters.")
            sys.exit(1)

        encrypt_key(hex_key)
        print("Key was successfully saved in ft_otp.key.")
    elif flag == "-k":
        enc_key = load_enc_key()
        hex_key = decrypt_key(enc_key)

        counter = int(time.time() // 30)
        otp = generate_otp(hex_key, counter)
        print(otp)
    else:
        print("Invalid flag! Usage: ./ft_otp -g <key_file> or ./ft_otp -k")

if __name__ == "__main__":
    main()
