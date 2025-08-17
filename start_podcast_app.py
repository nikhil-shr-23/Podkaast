#!/usr/bin/env python3
import sys
import os

def check_dependencies():
    print("🔍 Checking dependencies...")
    
    required_packages = [
        'gradio',
        'pypdf', 
        'gtts',
        'pyttsx3'
    ]
    
    missing_packages = []
    
    for package in required_packages:
        try:
            if package == 'gtts':
                import gtts
            elif package == 'pyttsx3':
                import pyttsx3
            else:
                __import__(package)
            print(f"✅ {package}")
        except ImportError:
            print(f"❌ {package}")
            missing_packages.append(package)
    
    if missing_packages:
        print(f"\n⚠️  Missing packages: {', '.join(missing_packages)}")
        print("Please install with: pip3 install -r requirements.txt")
        return False
    
    print("✅ All dependencies available!")
    return True

def start_application():
    try:
        print("\n🚀 Starting PDF2Podcast Application...")
        print("=" * 50)
        
        from podcast_app_working import demo
        
        print("✅ Application loaded successfully!")
        print("✅ Interface components ready!")
        print("✅ TTS services available!")
        
        print("\n🎙️ Launching Gradio interface...")
        print("📱 The app will open in your browser")
        print("🌐 You'll also get a public shareable link")
        
        demo.launch(
            share=True, 
            debug=False,
            show_error=True
        )
        
    except Exception as e:
        print(f"\n❌ Failed to start application: {e}")
        print("\n🔧 Troubleshooting steps:")
        print("1. Make sure all dependencies are installed")
        print("2. Check if port 7860 is available")
        print("3. Try running: python3 demo_working.py")
        print("4. Check the error logs above")
        return False
    
    return True

def main():
    print("🎙️ PDF2Podcast - Startup Manager")
    print("=" * 40)
    
    if not check_dependencies():
        print("\n❌ Dependency check failed. Please install missing packages.")
        sys.exit(1)
    
    if start_application():
        print("\n🎉 Application started successfully!")
    else:
        print("\n⚠️  Application failed to start. Check the errors above.")
        sys.exit(1)

if __name__ == "__main__":
    main()
