def clean_channels(raw):
    """
    Clean EEG channels by removing duplicates.

    Parameters:
        raw (mne.io.Raw): Referenced EEG data

    Returns:
        mne.io.Raw: Cleaned EEG data
    """

    raw_clean = raw.copy()

    # Get unique channel names while preserving order
    seen = set()
    unique_channels = []

    for ch in raw_clean.ch_names:
        base_name = ch.split('-')[0] if '-' in ch else ch

        if ch not in seen:
            seen.add(ch)
            unique_channels.append(ch)

    # Pick only unique channels
    raw_clean.pick_channels(unique_channels)

    return raw_clean