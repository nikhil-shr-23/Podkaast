# PDF2Podcast Troubleshooting Guide

## The "RUNTIME_ERROR" Issue

The error "The current space is in the invalid state: RUNTIME_ERROR. Please contact the owner to fix this" indicates that your application is experiencing runtime issues. Here's how to fix it:

## 🔍 Root Causes & Solutions

### 1. **API Endpoint Issues** (Most Likely Cause)
**Problem**: The Hugging Face API endpoint `gabrielchua/open-notebooklm` is:
- Down or experiencing issues
- Has changed its API structure
- Requires authentication
- Has been removed or deprecated

**Solutions**:
- Use the fallback version: `python podcast_app_fallback.py`
- Check if the space is still active: https://huggingface.co/spaces/gabrielchua/open-notebooklm
- Try alternative TTS services (see below)

### 2. **Missing Dependencies**
**Problem**: Required packages are not installed or have version conflicts.

**Solution**:
```bash
# Remove existing packages
pip uninstall gradio gradio-client -y

# Install with specific versions
pip install -r requirements.txt

# Or install manually
pip install gradio>=4.0.0 gradio-client>=0.10.0
```

### 3. **Python Environment Issues**
**Problem**: Python version incompatibility or virtual environment issues.

**Solution**:
```bash
# Create fresh virtual environment
python -m venv pdf2podcast_env
source pdf2podcast_env/bin/activate  # On Windows: pdf2podcast_env\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 4. **File Permission Issues**
**Problem**: Cannot create temporary files or access directories.

**Solution**:
```bash
# Check permissions
ls -la /tmp
chmod 755 /tmp  # If needed

# Run with proper permissions
python podcast_app.py
```

## 🧪 Testing Your Setup

### Run the Test Suite
```bash
python test_app.py
```

This will check:
- ✅ Package imports
- ✅ Gradio Client connectivity
- ✅ File operations
- ✅ Basic functionality

### Test Individual Components
```bash
# Test Gradio installation
python -c "import gradio; print('Gradio OK')"

# Test gradio_client
python -c "from gradio_client import Client; print('Client OK')"

# Test file operations
python -c "import tempfile; print('File ops OK')"
```

## 🚀 Alternative Solutions

### Option 1: Use Fallback Version
```bash
python podcast_app_fallback.py
```
This version provides a working interface with mock responses while you fix the API issues.

### Option 2: Integrate Different TTS Services

#### Google Cloud Text-to-Speech
```bash
pip install google-cloud-texttospeech
```

#### Amazon Polly
```bash
pip install boto3
```

#### Local TTS (Offline)
```bash
pip install pyttsx3 gTTS edge-tts
```

### Option 3: Use a Different Hugging Face Space
Replace the API endpoint with a working one:
```python
# Instead of "gabrielchua/open-notebooklm"
client = Client("gradio/hello_world")  # Test with working space
```

## 📋 Step-by-Step Recovery

1. **Stop the current application** (Ctrl+C)
2. **Check the test suite**: `python test_app.py`
3. **Install missing dependencies**: `pip install -r requirements.txt`
4. **Try the fallback version**: `python podcast_app_fallback.py`
5. **If that works, debug the main version**: `python podcast_app.py`

## 🐛 Debug Mode

Enable debug logging:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## 📞 Getting Help

If you're still experiencing issues:

1. **Check the logs** for specific error messages
2. **Run the test suite** and share the output
3. **Check your Python version**: `python --version`
4. **Verify your OS and architecture**
5. **Share the complete error traceback**

## 🔧 Quick Fix Commands

```bash
# Complete reset and reinstall
pip uninstall -y gradio gradio-client
pip install --upgrade pip
pip install -r requirements.txt

# Test the setup
python test_app.py

# Run the app
python podcast_app_fallback.py
```

## 📊 Common Error Patterns

| Error | Cause | Solution |
|-------|-------|----------|
| `ModuleNotFoundError` | Missing package | `pip install package_name` |
| `ImportError` | Version conflict | `pip install --upgrade package_name` |
| `PermissionError` | File access issues | Check directory permissions |
| `ConnectionError` | API endpoint down | Use fallback version |
| `RuntimeError` | Environment issues | Reset virtual environment |

## 🎯 Next Steps

1. **Immediate**: Use `podcast_app_fallback.py` to get a working interface
2. **Short-term**: Debug the main API endpoint issues
3. **Long-term**: Integrate with a reliable TTS service

The fallback version will give you a functional application while you resolve the underlying API issues.
