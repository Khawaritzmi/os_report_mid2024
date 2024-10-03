
import psutil
import argparse

def list_processes():
    processes = psutil.pids()
    print(f"Daftar proses yang berjalan di sistem:")
    for pid in processes:
        try:
            process = psutil.Process(pid)
            print(f"PID: {pid}, Nama: {process.name()}")
        except psutil.NoSuchProcess:
            pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CLI untuk menampilkan daftar proses yang berjalan")
    args = parser.parse_args()

    list_processes()