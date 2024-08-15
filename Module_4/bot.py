import streamlit as st
from transformers import SpeechT5Processor, SpeechT5ForTextToSpeech, SpeechT5HifiGan
from datasets import load_dataset
import torch
import soundfile as sf
import io
from IPython.display import Audio

# Load models and tokenizer
processor = SpeechT5Processor.from_pretrained("microsoft/speecht5_tts")
model = SpeechT5ForTextToSpeech.from_pretrained("microsoft/speecht5_tts")
vocoder = SpeechT5HifiGan.from_pretrained("microsoft/speecht5_hifigan")

# Load xvector dataset for speaker embeddings
embeddings_dataset = load_dataset("Matthijs/cmu-arctic-xvectors", split="validation")

# Streamlit UI
st.title("Text-to-Speech Generation with SpeechT5")
st.write("Enter text and generate speech using the SpeechT5 model.")

# Text input
text_input = st.text_area("Text to convert to speech:", 
                          "Simply run this code in a Google Colab cell, and you should see an audio player widget that lets you play the generated speech directly in the notebook.")

# Speaker selection
speaker_index = st.slider("Select Speaker Index:", min_value=0, max_value=len(embeddings_dataset)-1, value=7306)
speaker_embeddings = torch.tensor(embeddings_dataset[speaker_index]["xvector"]).unsqueeze(0)

if st.button("Generate Speech"):
    if text_input:
        st.write("Generating speech...")
        
        # Process and generate speech
        inputs = processor(text=text_input, return_tensors="pt")
        speech = model.generate_speech(inputs["input_ids"], speaker_embeddings, vocoder=vocoder)
        
        # Save the generated speech to a BytesIO object
        audio_bytes_io = io.BytesIO()
        sf.write(audio_bytes_io, speech.numpy(), samplerate=16000, format='WAV')
        audio_bytes_io.seek(0)
        
        # Display audio player
        st.audio(audio_bytes_io, format="audio/wav")
    else:
        st.warning("Please enter some text.")

st.write("Select a speaker from the dataset to influence the voice characteristics.")
st.write("Speaker index:", speaker_index)
