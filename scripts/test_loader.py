from pathlib import Path
from src.preprocessing.loader import load_edf
from src.preprocessing.filtering import apply_filters
from src.preprocessing.referencing import apply_reference
from src.preprocessing.channel_cleaning import clean_channels
from src.preprocessing.segmentation import segment_signal
from src.preprocessing.labeling import generate_labels
from src.preprocessing.feature_extraction import extract_features

file_name = "chb01_15.edf"   # change this when needed

if __name__ == "__main__":
    file_path = Path(f"data/raw/chb01/{file_name}")

data = load_edf(str(file_path))
raw = data["raw"]

filtered = apply_filters(raw)
referenced = apply_reference(filtered)
cleaned = clean_channels(referenced)

segments = segment_signal(cleaned)

if file_name == "chb01_15.edf":
    labels = generate_labels(
        segments,
        sfreq=256,
        window_size=10,
        overlap=5,
        seizure_start=1732,
        preictal_duration=600
    )
else:
    import numpy as np
    labels = np.zeros(len(segments), dtype=int)

print("Segments:", segments.shape)
print("Labels:", labels.shape)
print("Pre-ictal count:", labels.sum())

features = extract_features(segments, sfreq=256)

print("Feature shape:", features.shape)