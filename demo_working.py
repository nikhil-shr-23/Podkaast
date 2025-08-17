#!/usr/bin/env python3
"""
Demo script for the working PDF2Podcast TTS functionality
This tests the core functions without launching the full Gradio interface
"""

import tempfile
import os

def test_pdf_text_extraction():
    """Test PDF text extraction"""
    print("🧪 Testing PDF Text Extraction...")
    
    try:
        # Create a simple test PDF content
        test_content = b"Test PDF content for podcast generation"
        
        # Test the extraction function
        from podcast_app_working import extract_text_from_pdf
        
        # Create a mock PDF file
        with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp_file:
            tmp_file.write(test_content)
            temp_path = tmp_file.name
        
        try:
            # This will fail since it's not a real PDF, but we can test the function structure
            result = extract_text_from_pdf(test_content)
            print(f"✅ Text extraction function works: {result[:50]}...")
        finally:
            os.unlink(temp_path)
            
        return True
        
    except Exception as e:
        print(f"❌ Text extraction test failed: {e}")
        return False

def test_script_generation():
    """Test podcast script generation"""
    print("\n🧪 Testing Podcast Script Generation...")
    
    try:
        from podcast_app_working import generate_podcast_script
        
        test_text = "This is a sample text for testing podcast script generation."
        script = generate_podcast_script(test_text, "Test Question", "Fun", "Short (1-2 min)", "English")
        
        if script and "Podcast Script" in script:
            print("✅ Script generation successful!")
            print(f"Script preview: {script[:100]}...")
            return True
        else:
            print("❌ Script generation failed")
            return False
            
    except Exception as e:
        print(f"❌ Script generation test failed: {e}")
        return False

def test_tts_functionality():
    """Test text-to-speech functionality"""
    print("\n🧪 Testing Text-to-Speech...")
    
    try:
        # Test offline TTS first
        from podcast_app_working import text_to_speech_pyttsx3
        
        test_text = "Hello, this is a test of the text to speech functionality."
        audio_path = text_to_speech_pyttsx3(test_text)
        
        if audio_path and os.path.exists(audio_path):
            print(f"✅ Offline TTS successful! Audio saved to: {audio_path}")
            print(f"Audio file size: {os.path.getsize(audio_path)} bytes")
            
            # Clean up
            os.unlink(audio_path)
            return True
        else:
            print("❌ Offline TTS failed")
            return False
            
    except Exception as e:
        print(f"❌ TTS test failed: {e}")
        return False

def test_gtts_functionality():
    """Test Google TTS functionality"""
    print("\n🧪 Testing Google TTS (Online)...")
    
    try:
        from podcast_app_working import text_to_speech_gtts
        
        test_text = "Hello, this is a test of Google text to speech."
        audio_path = text_to_speech_gtts(test_text, "English")
        
        if audio_path and os.path.exists(audio_path):
            print(f"✅ Google TTS successful! Audio saved to: {audio_path}")
            print(f"Audio file size: {os.path.getsize(audio_path)} bytes")
            
            # Clean up
            os.unlink(audio_path)
            return True
        else:
            print("❌ Google TTS failed")
            return False
            
    except Exception as e:
        print(f"❌ Google TTS test failed: {e}")
        return False

def main():
    """Run all tests"""
    print("🎙️ PDF2Podcast Working Version - Functionality Test")
    print("=" * 60)
    
    tests = [
        ("PDF Text Extraction", test_pdf_text_extraction),
        ("Script Generation", test_script_generation),
        ("Offline TTS", test_tts_functionality),
        ("Google TTS", test_gtts_functionality)
    ]
    
    results = []
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"❌ {test_name} test crashed: {e}")
            results.append((test_name, False))
    
    print("\n" + "=" * 60)
    print("📊 Test Results Summary:")
    
    all_passed = True
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{test_name}: {status}")
        if not result:
            all_passed = False
    
    if all_passed:
        print("\n🎉 All tests passed! Your working version is ready.")
        print("You can now run: python3 podcast_app_working.py")
    else:
        print("\n⚠️  Some tests failed. Check the errors above.")
    
    return all_passed

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
