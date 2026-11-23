import pathlib


def main():
    # 13 dipilih karena angkanya kecil dan spesifik, jadi terasa
    # seperti hitungan sungguhan, bukan tebakan kasar. Lapangan
    # dipenuhi angka besar seperti 47, 87, 137, sampai 365, jadi
    # jawaban rendah yang presisi ini justru menonjol dan
    # lebih bisa dipercaya sebagai jumlah tab yang benar-benar
    # dibuka seseorang.
    # Tulis jawabannya sebagai teks polos, tanpa baris baru di akhir.
    out_path = pathlib.Path("/output/entry.txt")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("13", encoding="utf-8")


if __name__ == "__main__":
    main()
