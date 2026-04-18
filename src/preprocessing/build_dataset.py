from pathlib import Path
import numpy as np

from src.preprocessing.loader import load_edf
from src.preprocessing.filtering import apply_filters
from src.preprocessing.referencing import apply_reference
from src.preprocessing.channel_cleaning import clean_channels
from src.preprocessing.segmentation import segment_signal
from src.preprocessing.labeling import generate_labels
from src.preprocessing.feature_extraction import extract_features


def process_file(file_path, is_seizure_file=False,
                 seizure_start=None, preictal_duration=600):
    """
    Process a single EDF file into features and labels
    """

    data = load_edf(str(file_path))
    raw = data["raw"]

    filtered = apply_filters(raw)
    referenced = apply_reference(filtered)
    cleaned = clean_channels(referenced)

    segments = segment_signal(cleaned)
    features = extract_features(segments, sfreq=256)

    if is_seizure_file:
        labels = generate_labels(
            segments,
            sfreq=256,
            seizure_start=seizure_start,
            preictal_duration=preictal_duration
        )
    else:
        labels = np.zeros(len(segments), dtype=int)

    return features, labels