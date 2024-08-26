import webrtcvad
from pydub import AudioSegment
import numpy as np

def process_audio(filepath):
    # Load audio file
    audio = AudioSegment.from_wav(filepath)
    audio = audio.set_frame_rate(16000).set_channels(1)  # WebRTC VAD requires 16kHz, mono

    # Convert to raw audio data
    raw_data = np.array(audio.get_array_of_samples())
    raw_data = raw_data.astype(np.int16)

    # Initialize VAD
    vad = webrtcvad.Vad()
    frame_duration = 30  # ms
    frame_size = int(16000 * frame_duration / 1000)
    num_frames = len(raw_data) // frame_size

    # Detect voice activity
    timestamps = []
    for i in range(num_frames):
        start = i * frame_size
        end = (i + 1) * frame_size
        frame = raw_data[start:end]
        if vad.is_speech(frame.tobytes(), 16000):
            timestamps.append({
                "start": start / 16000,
                "end": end / 16000
            })

    return timestamps
