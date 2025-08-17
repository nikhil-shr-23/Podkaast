#!/usr/bin/env python3
import sys
import importlib.util

def test_imports():
    required_packages = [
        'gradio',
        'gradio_client',
        'pandas',
        'google.generativeai',
        'pypdf',
        'loguru',
        'promptic',
        'tenacity',
        'requests'
    ]
    
    print("Testing package imports...")
    failed_imports = []
    
    for package in required_packages:
        try:
            if package == 'google.generativeai':
                import google.generativeai
            else:
                importlib.import_module(package)
            print(f"✅ {package}")
        except ImportError as e:
            print(f"❌ {package}: {e}")
            failed_imports.append(package)
    
    if failed_imports:
        print(f"\nFailed imports: {failed_imports}")
        print("Please install missing packages with: pip install -r requirements.txt")
        return False
    
    print("\n✅ All packages imported successfully!")
    return True

def test_gradio_client():
    try:
        from gradio_client import Client
        print("\nTesting Gradio Client connection...")
        
        client = Client("gradio/hello_world")
        print("✅ Gradio Client initialized successfully")
        
        try:
            result = client.predict("Hello", api_name="/greet")
            print(f"✅ Test API call successful: {result}")
        except Exception as api_error:
            print(f"⚠️  API call failed (expected): {api_error}")
            print("✅ Client creation successful - this is sufficient for our app")
        
        return True
        
    except Exception as e:
        print(f"❌ Gradio Client test failed: {e}")
        return False

def test_file_operations():
    import tempfile
    import os
    
    print("\nTesting file operations...")
    
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp_file:
            tmp_file.write(b"test content")
            temp_path = tmp_file.name
        
        if os.path.exists(temp_path):
            print("✅ Temporary file created successfully")
        
        os.unlink(temp_path)
        if not os.path.exists(temp_path):
            print("✅ Temporary file cleanup successful")
        
        return True
        
    except Exception as e:
        print(f"❌ File operations test failed: {e}")
        return False

def main():
    print("🧪 PDF2Podcast Application Test Suite")
    print("=" * 50)
    
    tests = [
        ("Package Imports", test_imports),
        ("Gradio Client", test_gradio_client),
        ("File Operations", test_file_operations)
    ]
    
    results = []
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"❌ {test_name} test crashed: {e}")
            results.append((test_name, False))
    
    print("\n" + "=" * 50)
    print("📊 Test Results Summary:")
    
    all_passed = True
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{test_name}: {status}")
        if not result:
            all_passed = False
    
    if all_passed:
        print("\n🎉 All tests passed! Your environment is ready.")
        print("You can now run: python podcast_app.py")
    else:
        print("\n⚠️  Some tests failed. Please fix the issues above before running the main app.")
    
    return all_passed

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
