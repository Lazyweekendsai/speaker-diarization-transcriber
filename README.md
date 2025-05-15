# speaker-diarization-transcriber
Transkriberer lyd og identificerer talere vha. Whisper og Pyannote

Et simpelt og effektivt værktøj, der kombinerer **Whisper** (OpenAI) og **Pyannote.audio** (Hugging Face) til at:

Transskribere lyd (fx interviews)  
Identificere talerskift (speaker diarization)  
Kombinere output i læsbar fil med talernavne og tidskoder

---

## 🛠 Teknologier

- Python
- [OpenAI Whisper](https://github.com/openai/whisper)
- [pyannote.audio](https://github.com/pyannote/pyannote-audio)
- `dotenv` (for sikker token-håndtering)
- Hugging Face API

---

## ⚙️ Installation

```bash
git clone https://github.com/Lazyweekendsai/speaker-diarization-transcriber.git
cd speaker-diarization-transcriber
pip install -r requirements.txt
