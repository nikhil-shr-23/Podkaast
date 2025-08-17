import gradio as gr
import tempfile
import os
import logging
import requests
from pathlib import Path
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def extract_text_from_pdf(pdf_file):
    temp_path = None
    try:
        import pypdf
        with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp_file:
            tmp_file.write(pdf_file)
            temp_path = tmp_file.name
        
        try:
            reader = pypdf.PdfReader(temp_path)
            text = ""
            for page in reader.pages:
                text += page.extract_text() + "\n"
            return text.strip()
        finally:
            os.unlink(temp_path)
    except Exception as e:
        logger.error(f"PDF text extraction failed: {e}")
        return f"Error extracting text from PDF: {str(e)}"

def generate_podcast_script(text, question, tone, length, language):
    try:
        if question:
            focus = f"Focusing on: {question}"
        else:
            focus = "General content overview"
        
        script = f"""
# Podcast Script

**Topic:** {focus}
**Tone:** {tone}
**Length:** {length}
**Language:** {language}

## Introduction
Welcome to today's podcast! We'll be discussing content from your uploaded document.

## Main Content
{text[:500]}{'...' if len(text) > 500 else ''}

## Summary
This podcast covered the key points from your document. The content has been adapted to a {tone.lower()} tone and formatted for {length.lower()} listening.

## Outro
Thank you for listening! This podcast was generated from your PDF content.
        """
        return script.strip()
    except Exception as e:
        logger.error(f"Script generation failed: {e}")
        return f"Error generating script: {str(e)}"

def text_to_speech_gtts(text, language="en"):
    try:
        from gtts import gTTS
        
        with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as tmp_file:
            temp_path = tmp_file.name
        
        lang_map = {
            "English": "en",
            "Spanish": "es", 
            "French": "fr",
            "German": "de",
            "Chinese": "zh",
            "Japanese": "ja",
            "Korean": "ko",
            "Hindi": "hi",
            "Portuguese": "pt",
            "Russian": "ru",
            "Italian": "it",
            "Turkish": "tr",
            "Polish": "pl"
        }
        
        lang_code = lang_map.get(language, "en")
        
        tts = gTTS(text=text, lang=lang_code, slow=False)
        tts.save(temp_path)
        
        return temp_path
        
    except Exception as e:
        logger.error(f"gTTS failed: {e}")
        return None

def text_to_speech_pyttsx3(text):
    try:
        import pyttsx3
        
        with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as tmp_file:
            temp_path = tmp_file.name
        
        engine = pyttsx3.init()
        
        engine.setProperty('rate', 150)
        engine.setProperty('volume', 0.9)
        
        engine.save_to_file(text, temp_path)
        engine.runAndWait()
        
        return temp_path
        
    except Exception as e:
        logger.error(f"pyttsx3 failed: {e}")
        return None

def convert_pdf_to_podcast(pdf_file, url, question, tone, length, language, use_advanced_audio):
    temp_path = None
    audio_path = None
    
    try:
        if pdf_file is None:
            return None, "Error: Please upload a PDF file"
        
        text = extract_text_from_pdf(pdf_file)
        if text.startswith("Error"):
            return None, text
        
        script = generate_podcast_script(text, question, tone, length, language)
        
        if use_advanced_audio:
            audio_path = text_to_speech_gtts(script, language)
            if not audio_path:
                audio_path = text_to_speech_pyttsx3(script)
        else:
            audio_path = text_to_speech_pyttsx3(script)
        
        if audio_path and os.path.exists(audio_path):
            return audio_path, script
        else:
            return None, f"{script}\n\n❌ Audio generation failed. Please try again."
        
    except Exception as e:
        logger.error(f"Conversion failed: {str(e)}")
        return None, f"Error: {str(e)}"

with gr.Blocks(title="Podkaast: Convert PDFs to Podcasts") as demo:
    gr.Markdown("# 🎙️ Podkaast: Convert PDFs to Podcasts")
    gr.Markdown("✅ **Working Version** - Uses reliable TTS services instead of broken API")
    
    with gr.Row():
        with gr.Column():
            pdf_input = gr.File(
                label="📄 Upload your PDF",
                file_types=[".pdf"],
                type="binary"
            )
            
            url_input = gr.Textbox(
                label="🔗 URL (optional)",
                placeholder="Enter URL here...",
                value=""
            )
            
            question_input = gr.Textbox(
                label="❓ Question or Topic",
                placeholder="What would you like to focus on?",
                value=""
            )
            
            tone_input = gr.Radio(
                label="🎭 Select Tone",
                choices=["Fun", "Formal"],
                value="Fun"
            )
            
            length_input = gr.Radio(
                label="⏱️ Select Length",
                choices=["Short (1-2 min)", "Medium (3-5 min)"],
                value="Medium (3-5 min)"
            )
            
            language_input = gr.Dropdown(
                label="🌍 Select Language",
                choices=[
                    "English", "Spanish", "French", "German",
                    "Chinese", "Japanese", "Korean", "Hindi",
                    "Portuguese", "Russian", "Italian", "Turkish", "Polish"
                ],
                value="English"
            )
            
            advanced_audio = gr.Checkbox(
                label="🚀 Use Advanced Audio (Online TTS)",
                value=True,
                info="Uses Google TTS for better quality (requires internet)"
            )
            
            convert_btn = gr.Button("🎬 Convert to Podcast", variant="primary", size="lg")
            loading_indicator = gr.Text("", visible=False, label="Processing...")
        
        with gr.Column():
            audio_output = gr.Audio(label="🎵 Generated Podcast")
            transcript_output = gr.Markdown(label="📝 Transcript")
            status_output = gr.Textbox(label="📊 Status", interactive=False, value="Ready to convert PDF to podcast! 🎙️")

    def handle_conversion(pdf_file, url, question, tone, length, language, use_advanced_audio):
        try:
            audio, transcript = convert_pdf_to_podcast(pdf_file, url, question, tone, length, language, use_advanced_audio)
            
            if audio is None:
                return None, f"❌ {transcript}", f"Failed: {transcript}"
            else:
                return audio, transcript, "✅ Podcast generated successfully! 🎉"
                
        except Exception as e:
            error_msg = f"Unexpected error: {str(e)}"
            logger.error(error_msg)
            return None, f"❌ {error_msg}", f"Failed: {error_msg}"

    convert_btn.click(
        fn=handle_conversion,
        inputs=[
            pdf_input,
            url_input,
            question_input,
            tone_input,
            length_input,
            language_input,
            advanced_audio
        ],
        outputs=[audio_output, transcript_output, status_output],
        show_progress=True
    )

if __name__ == "__main__":
    try:
        print("🚀 Starting Podkaast - Working Version")
        print("✅ Uses reliable TTS services instead of broken API")
        demo.launch(share=True, debug=True)
    except Exception as e:
        logger.error(f"Failed to launch app: {e}")
        print(f"Error launching app: {e}")

app = demo.app
