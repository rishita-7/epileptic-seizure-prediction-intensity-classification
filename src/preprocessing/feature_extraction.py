import numpy as np
from scipy.signal import welch

def extract_features(segments, sfreq):
    """
    Extract time and frequency domain features from EEG segments.

    Parameters:
        segments (np.ndarray): (n_segments, n_channels, n_samples)
        sfreq (float): Sampling frequency

    Returns:
        np.ndarray: Feature matrix (n_segments, n_features)
    """

    feature_list = []

    for segment in segments:
        channel_features = []

        for channel_data in segment:
            # ---- Time-domain features ----
            mean = np.mean(channel_data)
            std = np.std(channel_data)
            var = np.var(channel_data)

            # ---- Frequency-domain (Welch PSD) ----
            freqs, psd = welch(channel_data, fs=sfreq)

            # Band powers
            delta = np.mean(psd[(freqs >= 0.5) & (freqs < 4)])
            theta = np.mean(psd[(freqs >= 4) & (freqs < 8)])
            alpha = np.mean(psd[(freqs >= 8) & (freqs < 13)])
            beta  = np.mean(psd[(freqs >= 13) & (freqs < 30)])

            channel_features.extend([mean, std, var, delta, theta, alpha, beta])

        feature_list.append(channel_features)

    return np.array(feature_list)