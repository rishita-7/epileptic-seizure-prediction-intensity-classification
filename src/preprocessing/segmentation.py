import numpy as np

def segment_signal(raw, window_size=10, overlap=5):
    """
    Segment EEG signal into overlapping windows.

    Parameters:
        raw (mne.io.Raw): Preprocessed EEG data
        window_size (int): Window size in seconds
        overlap (int): Overlap in seconds

    Returns:
        np.ndarray: Segmented data (n_windows, n_channels, n_samples)
    """

    data = raw.get_data()
    sfreq = raw.info['sfreq']

    window_samples = int(window_size * sfreq)
    overlap_samples = int(overlap * sfreq)
    step = window_samples - overlap_samples

    n_channels, n_samples = data.shape

    segments = []

    for start in range(0, n_samples - window_samples, step):
        end = start + window_samples
        segment = data[:, start:end]
        segments.append(segment)

    return np.array(segments)