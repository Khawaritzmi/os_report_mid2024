import os
import sys

def create_file(filename):
    with open(filename, 'w') as f:
        f.write('')  # Membuat file kosong
    print(f'File {filename} berhasil dibuat.')

def list_files(directory='.'):
    try:
        files = os.listdir(directory)
        print("\n".join(files))
    except FileNotFoundError:
        print(f'Direktori {directory} tidak ditemukan.')

def delete_file(filename):
    try:
        os.remove(filename)
        print(f'File {filename} berhasil dihapus.')
    except FileNotFoundError:
        print(f'File {filename} tidak ditemukan.')

def main():
    if len(sys.argv) < 2:
        print("Penggunaan: <perintah> [opsi]")
        sys.exit(1)

    command = sys.argv[1]

    if command == "create":
        create_file(sys.argv[2])
    elif command == "list":
        list_files(sys.argv[2] if len(sys.argv) > 2 else '.')
    elif command == "delete":
        delete_file(sys.argv[2])
    else:
        print(f"Perintah tidak dikenal: {command}")

if __name__ == "__main__":
    main()