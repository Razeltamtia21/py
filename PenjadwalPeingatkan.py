import time
from datetime import datetime, timedelta

# Fungsi untuk mengatur pengingat
def set_reminder():
    reminder_text = input("Masukkan pesan pengingat: ")
    minutes = int(input("Masukkan waktu pengingat (dalam menit): "))

    # Waktu pengingat
    reminder_time = datetime.now() + timedelta(minutes=minutes)
    print(f"\nPengingat disetel untuk {reminder_time.strftime('%H:%M:%S')}")

    # Tunggu hingga waktu pengingat
    while datetime.now() < reminder_time:
        time.sleep(1)

    # Tampilkan pesan pengingat
    print(f"\n=== Pengingat! ===\n{reminder_text}\n")

# Menjalankan pengingat
set_reminder()
