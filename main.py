import pathlib


def main():
    """Simpan angka tiga belas sebagai jawaban ke file entry."""
    out_file = pathlib.Path("/output/entry.txt")
    out_file.parent.mkdir(parents=True, exist_ok=True)
    out_file.write_text("13")


if __name__ == "__main__":
    main()
