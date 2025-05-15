import whisper
from pyannote.audio import Pipeline
from dotenv import load_dotenv
import os

# Indlæs miljøvariabler fra .env-filen
load_dotenv()
hf_token = os.getenv("HUGGINGFACE_TOKEN")

# Initialisér diarization-pipeline med token
pipeline = Pipeline.from_pretrained(
    "pyannote/speaker-diarization",
    use_auth_token=hf_token
)

# 1. Indlæs Whisper-model
print("Indlæser Whisper-model...")
whisper_model = whisper.load_model("small")

# 2. Transskriber lydfil
print("Kører transskription...")
whisper_result = whisper_model.transcribe("uffe.mp3", language="da")

# 3. Diarization med pyannote
print("Kører speaker diarization...")
diarization = pipeline("uffe.mp3")

# 4. Kombinér resultater
print("Kombinerer resultater...")

def find_speaker_for_timestamp(start, end, diarization_result):
    for turn, _, speaker in diarization_result.itertracks(yield_label=True):
        if turn.start <= start <= turn.end or turn.start <= end <= turn.end:
            return speaker
    return "Unknown"

with open("kombineret_output.txt", "w", encoding="utf-8") as f:
    for segment in whisper_result["segments"]:
        start = segment["start"]
        end = segment["end"]
        text = segment["text"]
        speaker = find_speaker_for_timestamp(start, end, diarization)
        f.write(f"[{start:.2f} - {end:.2f}] {speaker}: {text.strip()}\n")

print("Færdig! Se 'kombineret_output.txt'")


#python tts_transcribe.py




