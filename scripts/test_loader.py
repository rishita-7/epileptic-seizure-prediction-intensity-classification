from src.preprocessing.loader import load_edf

if __name__ == "__main__":
    file_path = "data/raw/chb01/chb01_01.edf"

    data = load_edf(file_path)

    print(data)