import numpy as np
import time

# Real-time EEG signal simulator mimicking patient data
# Generates continuous EEG stream with alternating non-seizure (interictal) and seizure (ictal) states.

def generate_baseline_eeg(duration_sec, fs=256):
    """
    Simulate baseline (non-seizure) EEG as a mix of EEG rhythms plus noise.
    - Alpha (8-12 Hz), Beta (12-30 Hz), Theta (4-8 Hz), Delta (0.5-4 Hz)
    """
    t = np.arange(0, duration_sec, 1/fs)
    # Sum of sinusoids for different bands
    alpha = np.sin(2 * np.pi * 10 * t)
    beta  = 0.5 * np.sin(2 * np.pi * 20 * t)
    theta = 0.75 * np.sin(2 * np.pi * 6 * t)
    delta = 0.3 * np.sin(2 * np.pi * 2 * t)
    noise = np.random.normal(0, 0.2, size=t.shape)
    eeg = alpha + beta + theta + delta + noise
    return eeg


def generate_seizure_eeg(duration_sec, fs=256):
    """
    Simulate seizure (ictal) EEG with high-amplitude rhythmic spikes.
    """
    t = np.arange(0, duration_sec, 1/fs)
    # Spike-and-wave: rhythmic 3 Hz with spikes
    spike_wave = 2.0 * np.sin(2 * np.pi * 3 * t)
    # Add random high-frequency noise to spikes
    noise = np.random.normal(0, 0.3, size=t.shape)
    # Occasional sharp transients
    for _ in range(int(duration_sec * 2)):  # ~2 spikes per second
        loc = np.random.randint(0, len(t)-1)
        spike_wave[loc] += np.random.uniform(3, 5)
    return spike_wave + noise


def real_time_eeg_stream(window_sec=1.0, fs=256, interictal_sec=30, ictal_sec=5):
    """
    Generator yielding consecutive windows of EEG data.
    After an interictal period, inserts an ictal period (seizure).
    """
    while True:
        # Interictal phase
        interictal_data = generate_baseline_eeg(interictal_sec, fs)
        # Yield in windows
        for start in range(0, len(interictal_data), int(window_sec * fs)):
            yield interictal_data[start:start + int(window_sec * fs)], 0  # label 0: non-seizure
            time.sleep(window_sec)

        # Ictal phase
        ictal_data = generate_seizure_eeg(ictal_sec, fs)
        for start in range(0, len(ictal_data), int(window_sec * fs)):
            yield ictal_data[start:start + int(window_sec * fs)], 1  # label 1: seizure
            time.sleep(window_sec)

# Example usage
def main():
    stream = real_time_eeg_stream()
    for i, (segment, label) in enumerate(stream):
        print(f"Window {i}: Label={'SEIZURE' if label==1 else 'NON-SEIZURE'} | Segment shape={segment.shape}")
        if i >= 100:  # stop after 100 windows
            break

if __name__ == '__main__':
    main()
