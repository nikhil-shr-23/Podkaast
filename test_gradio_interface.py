#!/usr/bin/env python3
"""
Test script to verify the Gradio interface loads without errors
"""

import sys
import time

def test_gradio_interface():
    """Test if the Gradio interface loads without errors"""
    try:
        print("🧪 Testing Gradio Interface Loading...")
        
        # Import the app
        from podcast_app_working import demo
        
        print("✅ App imported successfully")
        
        # Test if the interface components are properly configured
        if hasattr(demo, 'blocks'):
            print("✅ Gradio blocks interface configured")
        else:
            print("❌ Gradio blocks interface not found")
            return False
        
        # Test if the app object exists
        if hasattr(demo, 'app'):
            print("✅ App object available")
        else:
            print("❌ App object not found")
            return False
        
        print("✅ All interface tests passed!")
        return True
        
    except Exception as e:
        print(f"❌ Interface test failed: {e}")
        return False

def main():
    """Run the interface test"""
    print("🎙️ Gradio Interface Test")
    print("=" * 40)
    
    success = test_gradio_interface()
    
    if success:
        print("\n🎉 Interface test passed! You can now run the full app.")
        print("Run: python3 podcast_app_working.py")
    else:
        print("\n⚠️  Interface test failed. Check the errors above.")
    
    return success

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
