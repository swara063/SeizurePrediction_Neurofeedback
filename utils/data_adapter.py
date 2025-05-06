import numpy as np

def reshape_dummy_to_model_input(eeg_1d_window):
    """
    Convert 1D EEG vector (length 256) to shape (1, 22, 256, 4)
    Assuming synthetic EEG window maps identically across channels and features.
    """
    eeg_reshaped = np.tile(eeg_1d_window, (22, 4, 1)).transpose(0, 2, 1)  # shape (22, 256, 4)
    return np.expand_dims(eeg_reshaped, axis=0)  # shape (1, 22, 256, 4)
