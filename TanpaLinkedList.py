while True:
    nama = input("nama: ")
    a = int(input("nilai UH: "))
    b = int(input("nilai UTS: "))
    c = int(input("nilai UAS: "))

    rata2 = (a + b + c) / 3
    print("rata-rata siswa:", rata2)

    if rata2 >= 80:
        print("-----")
        print(f"{nama} lulus")
    else:
        print("-----")
        print(f"{nama} tidak lulus")
        break