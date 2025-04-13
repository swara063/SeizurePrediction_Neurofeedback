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
    Preprocess the EEG data for input to the model.
    data: shape (n_channels, window_size, n_chan_features) for a single segment
    """
    # Step 1: Preprocess the segment
    processed_data = preprocess_eeg_segment(data)

    # Step 2: Reshape data to (1, 1, 22, 256, 64)
    n_channels, window_size, n_chan_features = processed_data.shape[1:4]
    # Reshaping (1, 1, 22, 256, 64)
    processed_data = processed_data.reshape(1, 1, n_channels, window_size, n_chan_features)

    return processed_data


#neelam