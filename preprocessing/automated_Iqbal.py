import pandas as pd

def run_preprocessing():
    print("=== Memulai Otomatisasi Pre-processing Data ===")

    raw_data_path = "../dataset_raw/movie_feelings_dataset.csv"
    clean_data_path = "dataset_preprocessing/movie_feelings_dataset_preprocessing.csv"

    df = pd.read_csv(raw_data_path)

    # Membuang kolom yang tidak di pakai
    print("Membuang Kolom yang Tidak digunakan")

    kolom_dibuang = [
        'title', 'year', 'plot', 'imdb_rating', 
        'tomatometer', 'metascore', 'avg_rating', 
        'plot_feelings', 'gpt_feelings'
    ]

    df.drop(columns=kolom_dibuang, inplace=True)

    # Mengatasi Missing Value
    df.fillna(0, inplace=True)

    # Menyimpan data
    df.to_csv(clean_data_path, index=False)
    print(f"Data Berhasil di Save ke {clean_data_path}")
    print(f"Dimensi akhir data: {df.shape[0]} baris, {df.shape[1]} kolom.")
    print("=== Preprocessing Selesai 100% ===")

if __name__ == "__main__":
    run_preprocessing()
