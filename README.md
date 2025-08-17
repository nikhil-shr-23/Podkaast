# 🎙️ PDF2Podcast - Convert PDFs to Podcasts

A web application that converts PDF documents into engaging podcasts using advanced text-to-speech technology. Built with Gradio and featuring multiple TTS engines for reliable audio generation.

## ✨ Features

- **📄 PDF Processing**: Extract text from any PDF document
- **🎭 Customizable Audio**: Choose tone (Fun/Formal) and length (Short/Medium)
- **🌍 Multi-language Support**: 13+ languages including English, Spanish, French, German, Chinese, Japanese, and more
- **🎵 Dual TTS Engines**: 
  - **Google TTS** (online, high quality)
  - **System TTS** (offline, reliable)
- **📱 Web Interface**: Clean, intuitive Gradio-based UI
- **🔗 Public Sharing**: Generate shareable links for your podcasts
- **⚡ Real-time Processing**: Fast conversion with progress indicators

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Internet connection (for Google TTS)
- PDF files to convert

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd PDF2Podcast-main
   ```

2. **Install dependencies**
   ```bash
   pip3 install -r requirements.txt
   ```

3. **Launch the application**
   ```bash
   python3 start_podcast_app.py
   ```

4. **Open your browser**
   - Local: http://127.0.0.1:7860
   - Public: Use the shareable link provided

## 📖 Usage Guide

### Basic Workflow

1. **Upload PDF**: Click "Upload your PDF" and select your document
2. **Configure Settings**:
   - **Tone**: Choose between "Fun" or "Formal"
   - **Length**: Select "Short (1-2 min)" or "Medium (3-5 min)"
   - **Language**: Pick from 13+ supported languages
   - **Advanced Audio**: Toggle between online (Google TTS) and offline (System TTS)
3. **Convert**: Click "🎬 Convert to Podcast"
4. **Download**: Get your generated audio file and transcript

### Advanced Options

- **URL Input**: Add additional context or references
- **Question/Topic**: Focus on specific aspects of your PDF content
- **TTS Selection**: Choose between high-quality online TTS or reliable offline TTS

## 🛠️ Available Scripts

### Main Application
- **`podcast_app_working.py`** - Fully functional main application
- **`start_podcast_app.py`** - Smart startup script with dependency checking

### Testing & Development
- **`demo_working.py`** - Test core functionality without UI
- **`test_gradio_interface.py`** - Verify Gradio interface components
- **`test_app.py`** - Comprehensive application test suite

### Legacy Versions
- **`podcast_app.py`** - Original version (has API issues)
- **`podcast_app_fallback.py`** - Fallback version with mock responses

## 🔧 Technical Details

### Architecture
- **Frontend**: Gradio Blocks interface
- **Backend**: Python with modular TTS services
- **PDF Processing**: PyPDF for text extraction
- **Audio Generation**: Multiple TTS engines with fallback support

### TTS Engines
1. **Google TTS (gTTS)**
   - High-quality, natural-sounding voices
   - Requires internet connection
   - Supports 13+ languages
   - Output: MP3 format

2. **System TTS (pyttsx3)**
   - Uses system voices
   - Works offline
   - Platform-independent
   - Output: WAV format

### Dependencies
```
gradio>=4.0.0          # Web interface
pypdf>=3.0.0           # PDF text extraction
gTTS>=2.3.0            # Google Text-to-Speech
pyttsx3>=2.90          # System Text-to-Speech
edge-tts>=6.1.0        # Microsoft Edge TTS (optional)
```

## 🌐 Deployment

### Local Development
```bash
python3 podcast_app_working.py
```

### Production Deployment
```bash
# Deploy to Hugging Face Spaces
gradio deploy

# Or use the startup script
python3 start_podcast_app.py
```

### Docker (Coming Soon)
```bash
# Docker support will be added in future versions
docker build -t pdf2podcast .
docker run -p 7860:7860 pdf2podcast
```

## 🐛 Troubleshooting

### Common Issues

#### 1. **"RUNTIME_ERROR" or API Issues**
- **Cause**: Original Hugging Face API endpoint is down
- **Solution**: Use `podcast_app_working.py` instead of `podcast_app.py`

#### 2. **Missing Dependencies**
```bash
pip3 install -r requirements.txt
```

#### 3. **Port Already in Use**
- Change port in the launch command
- Or kill existing processes on port 7860

#### 4. **TTS Not Working**
- **Online TTS**: Check internet connection
- **Offline TTS**: Verify system has text-to-speech capabilities

### Testing Your Setup

1. **Run the test suite**
   ```bash
   python3 demo_working.py
   ```

2. **Check interface components**
   ```bash
   python3 test_gradio_interface.py
   ```

3. **Verify dependencies**
   ```bash
   python3 start_podcast_app.py
   ```

## 📱 Browser Compatibility

- ✅ Chrome/Chromium (recommended)
- ✅ Firefox
- ✅ Safari
- ✅ Edge
- ⚠️ Internet Explorer (not supported)

## 🔒 Security & Privacy

- **Local Processing**: PDFs are processed locally, not uploaded to external servers
- **Temporary Files**: Generated files are automatically cleaned up
- **No Data Storage**: Your content is not stored permanently
- **Secure Sharing**: Public links are temporary and secure

## 🤝 Contributing

We welcome contributions! Here's how to help:

1. **Fork the repository**
2. **Create a feature branch**
3. **Make your changes**
4. **Test thoroughly**
5. **Submit a pull request**

### Development Setup
```bash
# Install development dependencies
pip3 install -r requirements.txt

# Run tests
python3 demo_working.py
python3 test_gradio_interface.py

# Start development server
python3 start_podcast_app.py
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Gradio** for the excellent web interface framework
- **Google TTS** for high-quality text-to-speech
- **PyPDF** for reliable PDF processing
- **Open Source Community** for the amazing TTS libraries

## 📞 Support

### Getting Help
1. **Check the troubleshooting section** above
2. **Run the test scripts** to identify issues
3. **Check the logs** for error messages
4. **Open an issue** on GitHub with details

### Reporting Bugs
Please include:
- Python version
- Operating system
- Error message
- Steps to reproduce
- Test script output

## 🚀 Roadmap

### Upcoming Features
- [ ] **Docker Support** for easy deployment
- [ ] **Batch Processing** for multiple PDFs
- [ ] **Audio Customization** (speed, pitch, voice selection)
- [ ] **Export Options** (MP3, WAV, OGG)
- [ ] **Cloud Storage** integration
- [ ] **API Endpoints** for programmatic access

### Version History
- **v2.0.0** - Working version with reliable TTS engines
- **v1.0.0** - Initial release (had API issues)

---

**Made with ❤️ for content creators, educators, and podcast enthusiasts**

*Transform your documents into engaging audio content with PDF2Podcast!* 🎙️✨
