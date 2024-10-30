# Inisialisasi daftar to-do kosong
todo_list = []

# Fungsi untuk menampilkan daftar to-do
def tampilkan_todo():
    if not todo_list:
        print("Daftar tugas kosong.")
    else:
        print("\nDaftar Tugas:")
        for i, tugas in enumerate(todo_list, start=1):
            print(f"{i}. {tugas}")
    print()

# Fungsi untuk menambahkan tugas ke daftar
def tambah_tugas():
    tugas = input("Masukkan tugas baru: ")
    todo_list.append(tugas)
    print(f"Tugas '{tugas}' berhasil ditambahkan!\n")

# Fungsi untuk menghapus tugas dari daftar
def hapus_tugas():
    tampilkan_todo()
    try:
        nomor_tugas = int(input("Masukkan nomor tugas yang ingin dihapus: "))
        if 0 < nomor_tugas <= len(todo_list):
            tugas_terhapus = todo_list.pop(nomor_tugas - 1)
            print(f"Tugas '{tugas_terhapus}' berhasil dihapus!\n")
        else:
            print("Nomor tugas tidak valid.\n")
    except ValueError:
        print("Masukkan nomor yang valid.\n")

# Menu utama
def menu():
    while True:
        print("==== To-Do List ====")
        print("1. Tampilkan Daftar Tugas")
        print("2. Tambah Tugas")
        print("3. Hapus Tugas")
        print("4. Keluar")
        
        pilihan = input("Pilih opsi (1/2/3/4): ")
        
        if pilihan == '1':
            tampilkan_todo()
        elif pilihan == '2':
            tambah_tugas()
        elif pilihan == '3':
            hapus_tugas()
        elif pilihan == '4':
            print("Keluar dari program. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid, coba lagi.\n")

# Menjalankan menu
menu()
