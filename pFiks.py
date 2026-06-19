class Node:
    def __init__(self, nama, rata2, status):
        self.nama = nama
        self.rata2 = rata2
        self.status = status
        self.next = None

awal = None


def tambah_data(nama, rata2, status):
    global awal

    baru = Node(nama, rata2, status)

    if awal is None:
        awal = baru
    else:
        bantu = awal
        while bantu.next:
            bantu = bantu.next
        bantu.next = baru


def tampil_nama():
    bantu = awal

    print("\nDAFTAR SISWA")
    print("------------")

    if bantu is None:
        print("Belum ada data")
    else:
        while bantu:
            print("-", bantu.nama)
            bantu = bantu.next


def cari_data(nama):
    bantu = awal

    while bantu:
        if bantu.nama.lower() == nama.lower():
            print("\nDATA DITEMUKAN")
            print("Nama      :", bantu.nama)
            print("Rata-rata :", bantu.rata2)
            print("Status    :", bantu.status)
            return

        bantu = bantu.next

    print("Data tidak ditemukan")


def hapus_terakhir():
    global awal

    if awal is None:
        print("Data kosong")
        return

    if awal.next is None:
        print(f"Data {awal.nama} dihapus")
        awal = None
        return

    bantu = awal

    while bantu.next.next:
        bantu = bantu.next

    print(f"Data {bantu.next.nama} dihapus")
    bantu.next = None


while True:
    tampil_nama()

    print("\nMENU")
    print("1. Tambah Data")
    print("2. Cari Data")
    print("3. Hapus Data Terakhir")
    print("4. Selesai")

    pilihan = input("Masukkan pilihan: ")

    if pilihan == "1":
        nama = input("Nama: ")
        uh = int(input("Nilai UH : "))
        uts = int(input("Nilai UTS: "))
        uas = int(input("Nilai UAS: "))

        rata2 = (uh + uts + uas) / 3

        if rata2 >= 80:
            status = "Lulus"
        else:
            status = "Tidak Lulus"

        tambah_data(nama, rata2, status)

    elif pilihan == "2":
        nama = input("Masukkan nama yang dicari: ")
        cari_data(nama)

    elif pilihan == "3":
        hapus_terakhir()

    elif pilihan == "4":
        print("Program selesai")
        break

    else:
        print("Pilihan tidak valid")