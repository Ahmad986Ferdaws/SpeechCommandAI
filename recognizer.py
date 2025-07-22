# app/recognizer.py

import torchaudio
import torch
import os
from torchaudio.models import wav2vec2_model

# Load pretrained Wav2Vec2.0 model for classification
bundle = torchaudio.pipelines.WAV2VEC2_ASR_BASE_960H
model = bundle.get_model()

def transcribe_audio(file_path):
    waveform, sample_rate = torchaudio.load(file_path)

    if sample_rate != bundle.sample_rate:
        waveform = torchaudio.functional.resample(waveform, sample_rate, bundle.sample_rate)

    with torch.inference_mode():
        emissions, _ = model(waveform)
    transcript = bundle.decode(emissions[0])
    return transcript.strip().lower()

if __name__ == "__main__":
    print(transcribe_audio("audio/input.wav"))
