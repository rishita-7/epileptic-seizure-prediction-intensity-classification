import mne

def apply_filters(raw):
    """
    Apply bandpass and notch filtering to EEG data.

    Parameters:
        raw (mne.io.Raw): Raw EEG object

    Returns:
        mne.io.Raw: Filtered copy of raw data
    """

    # Work on a copy
    raw_filtered = raw.copy()

    # Explicitly load data ONLY here
    raw_filtered.load_data()

    # Bandpass filter
    raw_filtered.filter(
        l_freq=0.5,
        h_freq=40.0,
        fir_design='firwin',
        verbose=False
    )

    # Notch filter (India: 50 Hz)
    raw_filtered.notch_filter(
        freqs=50.0,
        verbose=False
    )

    return raw_filtered