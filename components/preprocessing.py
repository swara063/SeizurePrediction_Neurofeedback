import numpy as np
from scipy.signal import butter, filtfilt
from sklearn.decomposition import FastICA
from scipy.stats import kurtosis

# ----- Bandpass Filter ----- 
def bandpass_filter(signal, lowcut=1.0, highcut=40.0, fs=256, order=2):
    nyquist = 0.5 * fs
    low = lowcut / nyquist
    high = highcut / nyquist
    b, a = butter(order, [low, high], btype='band')
    return filtfilt(b, a, signal.flatten()).reshape(-1, 1)

# ----- ICA Artifact Rejection ----- 
def advanced_ica_artifact_rejection(data, kurtosis_threshold=5.0):
    n_segments, n_channels, window_size, n_chan_features = data.shape
    processed_data = np.zeros_like(data)

    for seg in range(n_segments):
        for feat in range(n_chan_features):
            eeg_segment = data[seg, :, :, feat]
            ica = FastICA(n_components=n_channels, random_state=0, max_iter=500)
            try:
                sources = ica.fit_transform(eeg_segment.T).T
            except Exception as e:
                print(f"ICA failed at segment {seg}, feature {feat}: {e}")
                processed_data[seg, :, :, feat] = eeg_segment
                continue

            k = kurtosis(sources, axis=1, fisher=True)
            sources[np.abs(k) > kurtosis_threshold, :] = 0
            cleaned = np.dot(ica.mixing_, sources).T
            processed_data[seg, :, :, feat] = cleaned.T

    return processed_data

# ----- Main Preprocessing Function ----- 
def preprocess_eeg_segment(segment, fs=256):
    """
    Run filtering and ICA on a single EEG segment
    segment: shape (n_channels, window_size, n_chan_features)
    """
    n_channels, window_size, n_chan_features = segment.shape

    for ch in range(n_channels):
        for feat in range(n_chan_features):
            signal = segment[ch, :, feat].reshape(-1, 1)
            filtered = bandpass_filter(signal, lowcut=1.0, highcut=40.0, fs=fs, order=2)
            segment[ch, :, feat] = filtered.reshape(-1)

    preprocessed = advanced_ica_artifact_rejection(segment[np.newaxis, ...])[0]
    return preprocessed

# Main preprocessing function to reshape data to (1, 1, 22, 256, 64)
def preprocess_data_for_model(data):
    """
    Preprocess EEG segment and expand features to match model input shape.
    Input: (22, 256, 4)
    Output: (1, 22, 256, 64)
    """
    processed_data = preprocess_eeg_segment(data)  # Expected: (22, 256, 4)

    # Pad the last dimension from 4 → 64 (zero-padding)
    if processed_data.shape[-1] < 64:
        pad_width = 64 - processed_data.shape[-1]
        processed_data = np.pad(processed_data, ((0, 0), (0, 0), (0, pad_width)), mode='constant')
    elif processed_data.shape[-1] > 64:
        raise ValueError(f"Too many features: got {processed_data.shape[-1]}, expected 64")

    # Add batch dimension → (1, 22, 256, 64)
    return processed_data[np.newaxis, ...]

