from models.user import Mahasiswa
from models.tugas import Tugas, TugasManager

def tampilkan_menu():
    print("\n=== Menu Manajemen Tugas Mahasiswa ===")
    print("1. Tambah Tugas")
    print("2. Lihat Tugas")
    print("3. Hapus Tugas")
    print("4. Keluar")

def main():
    nama = input("Masukkan nama Anda: ")
    nim = input("Masukkan NIM Anda: ")
    user = Mahasiswa(nama, nim)
    print(f"\nSelamat datang, {user.info()}!")

    manager = TugasManager()

    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-4): ")

        if pilihan == "1":
            judul = input("Judul Tugas: ")
            deadline = input("Deadline: ")
            deskripsi = input("Deskripsi: ")
            tugas = Tugas(judul, deadline, deskripsi)
            manager.tambah_tugas(tugas)
            print("Tugas berhasil ditambahkan.")
        elif pilihan == "2":
            semua_tugas = manager.tampilkan_semua()
            if not semua_tugas:
                print("Belum ada tugas.")
            else:
                for idx, t in enumerate(semua_tugas, start=1):
                    print(f"\nTugas #{idx}")
                    print(f"Judul    : {t.judul}")
                    print(f"Deadline : {t.deadline}")
                    print(f"Deskripsi: {t.deskripsi}")
        elif pilihan == "3":
            judul = input("Masukkan judul tugas yang ingin dihapus: ")
            manager.hapus_tugas(judul)
            print("Tugas dihapus jika ditemukan.")
        elif pilihan == "4":
            print("Terima kasih telah menggunakan aplikasi.")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
