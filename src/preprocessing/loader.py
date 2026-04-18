import mne

def load_edf(file_path: str):
    """
    Load an EDF file using MNE with lazy loading.

    Parameters:
        file_path (str): Path to EDF file

    Returns:
        dict: Contains raw object and metadata
    """
    raw = mne.io.read_raw_edf(file_path, preload=False, verbose=False)

    metadata = {
        "n_channels": len(raw.ch_names),
        "sampling_rate": raw.info["sfreq"],
        "duration_sec": float(raw.n_times / raw.info["sfreq"]),
        "channel_names": raw.ch_names
    }

    return {
        "raw": raw,
        **metadata
    }