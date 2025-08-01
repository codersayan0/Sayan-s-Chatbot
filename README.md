
# 🧠 Sayan's Chatbot  
### Multimodal AI Chatbot using Gemini Flash, Gradio, Voice & Image Input

![Gradio Interface](https://img.shields.io/badge/Built%20With-Gradio-blue?logo=gradio) ![Python](https://img.shields.io/badge/Language-Python-blue?logo=python) ![Gemini](https://img.shields.io/badge/AI-Generative%20Gemini-red)

---

## 📌 Overview

This is a multimodal chatbot powered by **Google's Gemini Flash (1.5)** and built using **Gradio**.  
It accepts **text**, **voice**, and **image** inputs and provides **voice + text** responses — making it a powerful tool for AI interaction with natural and visual understanding.

---

## ✨ Features

- 🗣️ **Text and Voice Input** (via microphone)
- 🖼️ **Image Upload Support**
- 🔊 **Voice Output** using `gTTS` (text-to-speech)
- 💬 **Interactive Chat UI** via Gradio
- 💾 **Downloadable Chat Log**
- 🧹 **Clear Chat History**

---

## 🖥️ Interface Preview

```
[Your Message]    [📤 Send] [💾 Download] [🧹 Clear Chat]
[🎤 Speak Instead]  [🖼️ Upload Image]
🔊 Voice reply plays below the chat log
```

---

## 🚀 Getting Started

### 🔧 Prerequisites

Make sure you have Python 3.8+ installed. Then install dependencies:

```bash
pip install google-generativeai gradio pillow gtts speechrecognition
```

> If you're on Windows and `pyaudio` gives trouble, use `gTTS` (already done in this project) — no additional audio drivers needed!

---

## 🔑 Gemini API Setup

1. Visit [Google AI Studio](https://makersuite.google.com/)
2. Generate your API key
3. Replace the API key in `chat.py`:
   ```python
   genai.configure(api_key="YOUR_API_KEY")
   ```

---

## ▶️ Running the Project

```bash
python chat.py
```

A Gradio interface will open in your browser. You can:

- Type or speak a message
- Optionally upload an image
- Hear the bot's voice reply
- Download the full chat log

---

## 📁 File Structure

```
chat.py               # Main chatbot application
chat_history.txt      # Generated on download
README.md             # You're here!
```

---

## 📌 Example Use Cases

- 🤔 "What do you see in this photo?" → [Upload an image]
- 🗣️ Ask: "Summarize this in simple terms" → via voice
- 💡 Combine voice + image → get multimodal insight

---

## 🧑‍💻 Built With

- [Gradio](https://gradio.app)
- [Google Generative AI SDK](https://ai.google.dev/)
- [gTTS](https://pypi.org/project/gTTS/)
- [Pillow](https://pypi.org/project/Pillow/)

---

## 📜 License

This project is open for learning and educational use. Attribution appreciated!
