from pathlib import Path
from src.preprocessing.loader import load_edf
from src.preprocessing.filtering import apply_filters
from src.preprocessing.referencing import apply_reference

if __name__ == "__main__":
    file_path = Path("data/raw/chb01/chb01_01.edf")

    data = load_edf(str(file_path))
    raw = data["raw"]

    filtered = apply_filters(raw)
    referenced = apply_reference(filtered)
    print("Raw:", raw)
    print("Filtered:", filtered)
    print("Referenced:", referenced)