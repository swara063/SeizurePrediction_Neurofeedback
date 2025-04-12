import numpy as np

def generate_dummy_eeg(n_channels=22, window_size=256, n_chan_features=4):
    eeg_segment = np.random.normal(0, 0.1, (n_channels, window_size, n_chan_features)).astype(np.float32)
    return eeg_segment
