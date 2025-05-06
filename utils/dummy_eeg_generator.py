import numpy as np
import time

def generate_baseline_eeg(duration_sec, fs=256):
    t = np.arange(0, duration_sec, 1/fs)
    alpha = np.sin(2 * np.pi * 10 * t)
    beta  = 0.5 * np.sin(2 * np.pi * 20 * t)
    theta = 0.75 * np.sin(2 * np.pi * 6 * t)
    delta = 0.3 * np.sin(2 * np.pi * 2 * t)
    noise = np.random.normal(0, 0.2, size=t.shape)
    eeg = alpha + beta + theta + delta + noise
    return eeg

def generate_multichannel_eeg(window_sec=1.0, fs=256, n_channels=22, n_features=64, seizure=False):
    base = generate_baseline_eeg(window_sec, fs)  # shape: (256,)
    multichannel = np.tile(base, (n_channels, 1))  # shape: (22, 256)

    multichannel_features = np.repeat(multichannel[:, :, np.newaxis], n_features, axis=2)  # (22, 256, 64)

    # Add realistic feature-wise noise
    noise = np.random.normal(0, 0.05, size=multichannel_features.shape)
    eeg_data = multichannel_features + noise

    if seizure:
        seizure_noise = np.random.normal(0.5, 0.3, size=multichannel_features.shape)
        eeg_data += seizure_noise

    return eeg_data

def real_time_eeg_stream(window_sec=1.0, fs=256, interictal_sec=30, ictal_sec=5):
    while True:
        # Interictal (non-seizure)
        for _ in range(int(interictal_sec)):
            yield generate_multichannel_eeg(window_sec, fs), 0
            time.sleep(window_sec)

        # Ictal (seizure)
        for _ in range(int(ictal_sec)):
            yield generate_multichannel_eeg(window_sec, fs, seizure=True), 1
            time.sleep(window_sec)
