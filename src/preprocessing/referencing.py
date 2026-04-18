import mne

def apply_reference(raw):
    """
    Apply common average reference (CAR) to EEG data.

    Parameters:
        raw (mne.io.Raw): Filtered EEG data

    Returns:
        mne.io.Raw: Re-referenced EEG data
    """

    raw_ref = raw.copy()

    # Apply Common Average Reference
    raw_ref.set_eeg_reference(ref_channels='average', verbose=False)

    return raw_ref