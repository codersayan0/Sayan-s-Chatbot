import google.generativeai as genai
import gradio as gr
from PIL import Image
import speech_recognition as sr
import pyttsx3
import tempfile
from gtts import gTTS

# 🔑 Gemini API setup
genai.configure(api_key="Enter your Gemini API key here")  # Replace with your key
model = genai.GenerativeModel("gemini-1.5-flash")
# 🧾 Store chat history
chat_log = []
# 🎤 Voice-to-text
def transcribe_audio(audio_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio = recognizer.record(source)
    try:
        return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        return "[Could not understand audio]"
    except sr.RequestError:
        return "[Voice recognition error]"
# 🔊 Text-to-speech: Gemini speaks the answer
def speak_response(text):
    tts = gTTS(text)
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmpfile:
        tts.save(tmpfile.name)
        return tmpfile.name
# 🧠 Generate Gemini response
def generate_response(text_prompt, audio_input, image_path):
    prompt = text_prompt.strip()
    # Use voice if no text input
    if not prompt and audio_input:
        prompt = transcribe_audio(audio_input)
    if not prompt:
        return "\n".join(chat_log) + "\n[No input provided]", None
    # With or without image
    if image_path:
        image = Image.open(image_path)
        response = model.generate_content([prompt, image])
    else:
        response = model.generate_content(prompt)

    answer = response.text.strip().replace("**", "")
    # 📝 Log
    entry = f"You: {prompt}" + (f" [Image attached]" if image_path else "")
    chat_log.append(entry)
    chat_log.append(f"Bot: {answer}")
    # 🔊 Generate voice reply
    audio_path = speak_response(answer)
    return "\n".join(chat_log), audio_path
# 🧹 Clear chat history
def clear_chat():
    chat_log.clear()
    return "", None  # Clears chatbox text and audio

# 💾 Export chat to file
def export_chat():
    filename = "chat_history.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write("\n".join(chat_log))
    return filename
# 🎨 Interface
with gr.Blocks() as demo:
    gr.Markdown("## 🎤🖼️ Sayan's Chatbot")
    gr.Markdown("Ask via text or voice, upload images, and get text & also voice responses!")
    chatbox = gr.Textbox(label="Chat History", lines=15, interactive=False)
    with gr.Row():
        input_box = gr.Textbox(placeholder="Type your message...", label="Text Message", scale=6)
        image_input = gr.Image(type="filepath", label="Optional Image", scale=4)
    with gr.Row():
        audio_input = gr.Audio(sources=["microphone"], type="filepath", label="🎤 Speak Instead")
    with gr.Row():
        submit_btn = gr.Button("📤 Send")
        download_btn = gr.Button("💾 Download Chat")
        clear_btn = gr.Button("🧹 Clear Chat")


    audio_output = gr.Audio(label="🔊 Bot Voice Reply")
    # 🔗 Button logic
    submit_btn.click(
        fn=generate_response,
        inputs=[input_box, audio_input, image_input],
        outputs=[chatbox, audio_output]
    )
    download_btn.click(fn=export_chat, inputs=[], outputs=gr.File(label="Download"))
    clear_btn.click(fn=clear_chat, inputs=[], outputs=[chatbox, audio_output])
demo.launch()
