from pathlib import Path
from src.preprocessing.loader import load_edf
from src.preprocessing.filtering import apply_filters
from src.preprocessing.referencing import apply_reference
from src.preprocessing.channel_cleaning import clean_channels

if __name__ == "__main__":
    file_path = Path("data/raw/chb01/chb01_01.edf")

    data = load_edf(str(file_path))
    raw = data["raw"]

    filtered = apply_filters(raw)
    referenced = apply_reference(filtered)

    cleaned = clean_channels(referenced)

    print("Before cleaning:", len(referenced.ch_names))
    print("After cleaning:", len(cleaned.ch_names))
    print("Raw:", raw)
    print("Filtered:", filtered)
    print("Referenced:", referenced)
    print("Before cleaning:", len(referenced.ch_names))
    print("After cleaning:", len(cleaned.ch_names))