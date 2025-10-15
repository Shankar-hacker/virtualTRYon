#!/usr/bin/env python3
"""
Setup script for AR/VR Virtual Try-On features
"""

import os
import sys
import subprocess
import platform

def run_command(command):
    """Run a command and return success status"""
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✓ {command}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ {command}")
        print(f"Error: {e.stderr}")
        return False

def check_python_version():
    """Check if Python version is compatible"""
    version = sys.version_info
    if version.major == 3 and version.minor >= 7:
        print(f"✓ Python {version.major}.{version.minor}.{version.micro} is compatible")
        return True
    else:
        print(f"✗ Python {version.major}.{version.minor}.{version.micro} is not compatible")
        print("Please use Python 3.7 or higher")
        return False

def install_requirements():
    """Install required packages"""
    print("\n📦 Installing required packages...")
    
    # Install basic requirements
    if os.path.exists('requirements_ar.txt'):
        success = run_command(f"{sys.executable} -m pip install -r requirements_ar.txt")
        if not success:
            print("Failed to install some packages. Trying individual installation...")
            
            # Try installing packages individually
            packages = [
                'opencv-python',
                'opencv-contrib-python', 
                'tensorflow',
                'scikit-learn',
                'matplotlib',
                'flask',
                'Pillow',
                'numpy',
                'PyYAML',
                'scikit-image',
                'imageio',
                'flask-cors'
            ]
            
            for package in packages:
                run_command(f"{sys.executable} -m pip install {package}")
    else:
        print("requirements_ar.txt not found. Installing essential packages...")
        essential_packages = [
            'opencv-python',
            'tensorflow',
            'flask',
            'Pillow',
            'numpy'
        ]
        
        for package in essential_packages:
            run_command(f"{sys.executable} -m pip install {package}")

def create_directories():
    """Create necessary directories"""
    print("\n📁 Creating directories...")
    
    directories = [
        'static/result',
        'static/testpicture', 
        'static/test_img',
        'static/collections',
        'static/ar_captures',
        'static/3d_captures'
    ]
    
    for directory in directories:
        try:
            os.makedirs(directory, exist_ok=True)
            print(f"✓ Created {directory}")
        except Exception as e:
            print(f"✗ Failed to create {directory}: {e}")

def check_models():
    """Check if required model files exist"""
    print("\n🤖 Checking model files...")
    
    required_files = [
        'cp_vton_gmm.onnx',
        'cp_vton_tom.onnx', 
        'lip_jppnet_384.pb',
        'openpose_pose_coco.prototxt',
        'pose_iter_440000.caffemodel'
    ]
    
    missing_files = []
    for file in required_files:
        if os.path.exists(file):
            print(f"✓ {file}")
        else:
            print(f"✗ {file} (missing)")
            missing_files.append(file)
    
    if missing_files:
        print(f"\n⚠️  Missing {len(missing_files)} model files. The app may not work properly.")
        print("Please ensure all model files are in the project directory.")

def setup_database():
    """Setup database if needed"""
    print("\n🗄️  Setting up database...")
    
    try:
        import sqlite3
        conn = sqlite3.connect('user_data.db')
        cursor = conn.cursor()
        
        # Create users table if it doesn't exist
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS user(
                name TEXT, 
                password TEXT, 
                mobile TEXT, 
                email TEXT
            )
        """)
        
        conn.commit()
        conn.close()
        print("✓ Database setup complete")
        
    except Exception as e:
        print(f"✗ Database setup failed: {e}")

def main():
    """Main setup function"""
    print("🚀 Setting up AR/VR Virtual Try-On System")
    print("=" * 50)
    
    # Check Python version
    if not check_python_version():
        return False
    
    # Install requirements
    install_requirements()
    
    # Create directories
    create_directories()
    
    # Check models
    check_models()
    
    # Setup database
    setup_database()
    
    print("\n" + "=" * 50)
    print("🎉 Setup complete!")
    print("\nTo run the application:")
    print("python app.py")
    print("\nThen open your browser to: http://127.0.0.1:5000")
    
    print("\n📝 Features available:")
    print("• Traditional Virtual Try-On")
    print("• AR Try-On with pose detection")
    print("• 3D Virtual Try-On")
    print("• Live camera capture")
    print("• Image upload and processing")
    
    return True

if __name__ == "__main__":
    main()