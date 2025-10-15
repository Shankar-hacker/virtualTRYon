import os
import sys
import subprocess

def test_detection():
    # Test if we can run the detection script
    test_person = "static/test_img"
    test_cloth = "static/data"
    
    # Check if directories exist
    print("Checking directories...")
    print(f"test_img exists: {os.path.exists(test_person)}")
    print(f"data exists: {os.path.exists(test_cloth)}")
    print(f"result exists: {os.path.exists('static/result')}")
    
    # List files in test directories
    if os.path.exists(test_person):
        print(f"Files in test_img: {os.listdir(test_person)}")
    if os.path.exists(test_cloth):
        print(f"Files in data: {os.listdir(test_cloth)[:5]}...")  # Show first 5
    
    # Check model files
    print("\nChecking model files...")
    models = ['cp_vton_gmm.onnx', 'cp_vton_tom.onnx', 'lip_jppnet_384.pb', 
              'openpose_pose_coco.prototxt', 'pose_iter_440000.caffemodel']
    for model in models:
        print(f"{model}: {os.path.exists(model)}")
    
    # Try to run a simple detection if we have test files
    if os.path.exists(test_person) and os.listdir(test_person):
        person_file = None
        for f in os.listdir(test_person):
            if f.endswith(('.jpg', '.jpeg', '.png')):
                person_file = os.path.join(test_person, f)
                break
        
        if person_file and os.path.exists(test_cloth) and os.listdir(test_cloth):
            cloth_file = None
            for f in os.listdir(test_cloth):
                if f.endswith(('.jpg', '.jpeg', '.png')):
                    cloth_file = os.path.join(test_cloth, f)
                    break
            
            if cloth_file:
                print(f"\nTesting detection with:")
                print(f"Person: {person_file}")
                print(f"Cloth: {cloth_file}")
                
                cmd = f"python detection.py --input_image {person_file} --input_cloth {cloth_file}"
                print(f"Command: {cmd}")
                
                try:
                    result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=60)
                    print(f"Return code: {result.returncode}")
                    if result.stdout:
                        print(f"STDOUT: {result.stdout}")
                    if result.stderr:
                        print(f"STDERR: {result.stderr}")
                except subprocess.TimeoutExpired:
                    print("Detection script timed out after 60 seconds")
                except Exception as e:
                    print(f"Error running detection: {e}")

if __name__ == "__main__":
    test_detection()