from cryptography.fernet import Fernet

# Generate encryption key
key = Fernet.generate_key()

# Create encryption object
cipher = Fernet(key)


def encrypt_phone(phone):
    return cipher.encrypt(phone.encode())


def decrypt_phone(encrypted_phone):
    return cipher.decrypt(encrypted_phone).decode()


while True:

    print("\n==============================")
    print("  TELEPHONE ENCRYPTION SYSTEM")
    print("==============================")
    print("1. Encrypt telephone number")
    print("2. Decrypt telephone number")
    print("3. Exit")

    choice = input("\nSelect an option: ")

    if choice == "1":

        phone = input("Enter telephone number: ")

        encrypted = encrypt_phone(phone)

        print("\nEncrypted telephone number:")
        print(encrypted.decode())

    elif choice == "2":

        encrypted = input("Enter encrypted telephone number: ")

        try:
            decrypted = decrypt_phone(encrypted.encode())

            print("\nDecrypted telephone number:")
            print(decrypted)

        except Exception:
            print("\nUnable to decrypt the number.")

    elif choice == "3":

        print("Exiting...")
        break

    else:

        print("Invalid option.")
