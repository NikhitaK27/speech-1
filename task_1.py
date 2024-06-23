
import os
import torch
import torchaudio
from transformers import Wav2Vec2Processor, Wav2Vec2ForCTC
from jiwer import cer

# Use CPU as the device
device = torch.device("cpu")
print(f'Using device: {device}')

#Download and Prepare Data
data_path = './data'
if not os.path.exists(data_path):
    os.makedirs(data_path)

# Dictionary to hold datasets
datasets = {
    'train-clean-100': torchaudio.datasets.LIBRISPEECH(data_path, url="train-clean-100", download=True),
    'train-clean-360': torchaudio.datasets.LIBRISPEECH(data_path, url="train-clean-360", download=True),
    'test-clean': torchaudio.datasets.LIBRISPEECH(data_path, url="test-clean", download=True),
    'test-other': torchaudio.datasets.LIBRISPEECH(data_path, url="test-other", download=True)
}

# Load and Prepare Model
processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-large-960h-lv60-self")
model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-large-960h-lv60-self")
model.to(device)  # Ensure model is set to CPU
model.eval()

#Define Speech Recognition Function
def speech_to_text(model, processor, waveform, sampling_rate):
    # Ensure waveform is mono and resample if necessary
    waveform = waveform.to(device)  # Move waveform to CPU
    if waveform.ndim > 1:
        waveform = waveform.mean(dim=0)
    if sampling_rate != 16000:
        resampler = torchaudio.transforms.Resample(orig_freq=sampling_rate, new_freq=16000)
        waveform = resampler(waveform)

    # Process waveform through the model
    inputs = processor(waveform, sampling_rate=16000, return_tensors="pt", padding=True)
    inputs = inputs.to(device)  # Ensure inputs are on CPU
    with torch.no_grad():
        logits = model(inputs.input_values, attention_mask=inputs.attention_mask).logits

    predicted_ids = torch.argmax(logits, dim=-1)
    transcription = processor.decode(predicted_ids[0])
    return transcription

# Evaluate the Model
def evaluate_model_on_datasets(model, processor, datasets, num_samples=100):
    results = {}
    for name, dataset in datasets.items():
        total_cer = 0
        num_samples = min(num_samples, len(dataset))
        for i in range(num_samples):
            waveform, sample_rate, _, _, _, _ = dataset[i]
            transcription = speech_to_text(model, processor, waveform, sample_rate)
            reference = dataset[i][2]
            total_cer += cer(reference, transcription)
        average_cer = total_cer / num_samples
        results[name] = average_cer
        print(f"Average CER for {name}: {average_cer}")
    return results

results = evaluate_model_on_datasets(model, processor, datasets)

# Print the results of the evaluation
print(results)
