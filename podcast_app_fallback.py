import gradio as gr
import tempfile
import os
import logging
import requests
from pathlib import Path

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def convert_pdf_to_podcast_fallback(pdf_file, url, question, tone, length, language, use_advanced_audio):
    temp_path = None
    try:
        if pdf_file is None:
            return None, "Error: Please upload a PDF file"
        
        with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp_file:
            tmp_file.write(pdf_file)
            temp_path = tmp_file.name

        mock_transcript = f"""
# Podcast Transcript

**Topic:** {question or 'PDF Content Analysis'}
**Tone:** {tone}
**Length:** {length}
**Language:** {language}

## Summary

This is a sample transcript generated from your PDF content. The original API endpoint (gabrielchua/open-notebooklm) appears to be experiencing issues.

## Next Steps

To get this working with real audio generation, you could:

1. **Use a different TTS service** like:
   - Google Cloud Text-to-Speech
   - Amazon Polly
   - Azure Cognitive Services
   - ElevenLabs
   - Coqui TTS

2. **Fix the current API** by:
   - Checking if the Hugging Face space is still active
   - Verifying the API endpoint structure
   - Adding proper authentication if required

3. **Use local TTS** with libraries like:
   - pyttsx3 (offline)
   - gTTS (Google Text-to-Speech)
   - edge-tts (Microsoft Edge TTS)

## Current Status

- ✅ PDF uploaded successfully
- ✅ Parameters processed
- ❌ Audio generation failed (API unavailable)
- ✅ Mock transcript generated

File: {temp_path}
Size: {os.path.getsize(temp_path)} bytes
        """
        
        return None, mock_transcript
        
    except Exception as e:
        logger.error(f"Conversion failed: {str(e)}")
        return None, f"Error: {str(e)}"
    
    finally:
        if temp_path and os.path.exists(temp_path):
            try:
                os.unlink(temp_path)
            except Exception as cleanup_error:
                logger.warning(f"Failed to cleanup temp file: {cleanup_error}")

def convert_pdf_to_podcast(pdf_file, url, question, tone, length, language, use_advanced_audio):
    try:
        from gradio_client import Client, handle_file
        
        temp_path = None
        try:
            if pdf_file is None:
                return None, "Error: Please upload a PDF file"
            
            with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp_file:
                tmp_file.write(pdf_file)
                temp_path = tmp_file.name

            client = Client("gabrielchua/open-notebooklm")
            
            try:
                result = client.predict(
                    files=[handle_file(temp_path)],
                    url=url or "",
                    question=question or "",
                    tone=tone,
                    length=length,
                    language=language,
                    use_advanced_audio=use_advanced_audio,
                    api_name="/generate_podcast"
                )
                
                if result and len(result) >= 2:
                    return result[0], result[1]
                else:
                    return None, "Error: Invalid response from API"
                    
            except Exception as api_error:
                logger.error(f"API call failed: {str(api_error)}")
                return convert_pdf_to_podcast_fallback(pdf_file, url, question, tone, length, language, use_advanced_audio)
        
        finally:
            if temp_path and os.path.exists(temp_path):
                try:
                    os.unlink(temp_path)
                except Exception as cleanup_error:
                    logger.warning(f"Failed to cleanup temp file: {cleanup_error}")
                    
    except ImportError:
        logger.warning("gradio_client not available, using fallback method")
        return convert_pdf_to_podcast_fallback(pdf_file, url, question, tone, length, language, use_advanced_audio)
    except Exception as e:
        logger.error(f"Main conversion failed: {str(e)}")
        return convert_pdf_to_podcast_fallback(pdf_file, url, question, tone, length, language, use_advanced_audio)

with gr.Blocks(title="LumeCast: Convert PDFs to Podcasts") as demo:
    gr.Markdown("# LumeCast: Convert PDFs to Podcasts")
    gr.Markdown("⚠️ **Note:** The original API is experiencing issues. This version includes fallback functionality.")
    
    with gr.Row():
        with gr.Column():
            pdf_input = gr.File(
                label="Upload your PDF",
                file_types=[".pdf"],
                type="binary"
            )
            
            url_input = gr.Textbox(
                label="URL (optional)",
                placeholder="Enter URL here...",
                value=""
            )
            
            question_input = gr.Textbox(
                label="Question or Topic",
                placeholder="What would you like to focus on?",
                value=""
            )
            
            tone_input = gr.Radio(
                label="Select Tone",
                choices=["Fun", "Formal"],
                value="Fun"
            )
            
            length_input = gr.Radio(
                label="Select Length",
                choices=["Short (1-2 min)", "Medium (3-5 min)"],
                value="Medium (3-5 min)"
            )
            
            language_input = gr.Dropdown(
                label="Select Language",
                choices=[
                    "English", "Spanish", "French", "German",
                    "Chinese", "Japanese", "Korean", "Hindi",
                    "Portuguese", "Russian", "Italian", "Turkish", "Polish"
                ],
                value="English"
            )
            
            advanced_audio = gr.Checkbox(
                label="Use Advanced Audio Generation",
                value=True
            )
            
            convert_btn = gr.Button("Convert to Podcast", variant="primary")
        
        with gr.Column():
            audio_output = gr.Audio(label="Generated Podcast")
            transcript_output = gr.Markdown(label="Transcript")
            status_output = gr.Textbox(label="Status", interactive=False)

    def handle_conversion(pdf_file, url, question, tone, length, language, use_advanced_audio):
        try:
            audio, transcript = convert_pdf_to_podcast(pdf_file, url, question, tone, length, language, use_advanced_audio)
            if audio is None:
                return None, f"❌ {transcript}", f"Failed: {transcript}"
            else:
                return audio, transcript, "✅ Conversion completed successfully!"
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
        outputs=[audio_output, transcript_output, status_output]
    )

if __name__ == "__main__":
    try:
        demo.launch(share=True, debug=True)
    except Exception as e:
        logger.error(f"Failed to launch app: {e}")
        print(f"Error launching app: {e}")

app = demo.app
