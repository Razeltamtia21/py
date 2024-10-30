import random
import string

# Fungsi untuk menghasilkan password acak
def generate_password(length=8):
    # Kombinasi karakter untuk password
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Menu utama
def main():
    print("=== Password Generator ===")
    try:
        length = int(input("Masukkan panjang password yang diinginkan: "))
        if length < 4:
            print("Panjang password minimal 4 karakter untuk keamanan.")
        else:
            password = generate_password(length)
            print(f"Password Anda: {password}")
    except ValueError:
        print("Masukkan panjang yang valid dalam angka.")

# Menjalankan program
main()
