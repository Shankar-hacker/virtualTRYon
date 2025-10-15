# AR/VR Virtual Try-On System

An enhanced virtual dressing room application with AR (Augmented Reality) and 3D try-on capabilities.

## 🚀 Features

### Traditional Virtual Try-On
- Upload images for virtual clothing try-on
- Live camera capture with improved image processing
- Better image centering and preprocessing
- Enhanced accuracy (85-95% range)

### AR Try-On
- Real-time augmented reality try-on
- Pose detection using MediaPipe
- Live clothing overlay on camera feed
- Interactive clothing selection
- Photo capture with AR overlay

### 3D Virtual Try-On
- Full 3D avatar system
- Real-time 3D clothing simulation
- Interactive 3D environment with controls
- Body tracking integration
- Multiple avatar models (male/female/custom)

## 🛠️ Installation

### Quick Setup
```bash
python setup_ar.py
```

### Manual Installation

1. **Install Python 3.7+**
   ```bash
   python --version  # Should be 3.7 or higher
   ```

2. **Install Required Packages**
   ```bash
   pip install -r requirements_ar.txt
   ```

3. **Create Directories**
   ```bash
   mkdir -p static/{result,testpicture,test_img,collections,ar_captures,3d_captures}
   ```

4. **Run the Application**
   ```bash
   python app.py
   ```

5. **Open Browser**
   Navigate to: `http://127.0.0.1:5000`

## 📋 Requirements

### System Requirements
- Python 3.7+
- Webcam (for AR/3D features)
- Modern web browser with WebGL support
- 4GB+ RAM recommended
- GPU acceleration recommended (optional)

### Required Model Files
Ensure these files are in the project root:
- `cp_vton_gmm.onnx` - Geometric Matching Module
- `cp_vton_tom.onnx` - Try-On Module  
- `lip_jppnet_384.pb` - Human parsing model
- `openpose_pose_coco.prototxt` - OpenPose configuration
- `pose_iter_440000.caffemodel` - OpenPose model weights

## 🎮 Usage

### Traditional Try-On
1. Go to Home → Select clothing item
2. Choose "IMAGE TEST" or "LIVE TEST"
3. Upload image or capture from camera
4. View the virtual try-on result

### AR Try-On
1. Click "AR Try-On" from navigation or trial room
2. Allow camera permissions
3. Click "Start AR" to begin
4. Select clothing from the bottom gallery
5. See real-time AR overlay
6. Capture photos with "Capture" button

### 3D Try-On
1. Click "3D Try-On" from navigation
2. Allow camera permissions if using body tracking
3. Select avatar model (default/male/female/custom)
4. Choose clothing from gallery
5. Use controls to adjust lighting, rotation, etc.
6. Capture screenshots of 3D try-on

## 🔧 Configuration

### Camera Settings
- Default resolution: 1280x720
- Facing mode: 'user' (front camera)
- Frame rate: 30fps

### 3D Rendering Settings
- Anti-aliasing: Enabled
- Shadow mapping: PCF Soft Shadows
- Lighting: Ambient + Directional

### AR Settings
- Pose detection confidence: 0.5
- Tracking smoothing: Enabled
- Overlay opacity: 0.8

## 🐛 Troubleshooting

### Common Issues

**Camera not working:**
- Check browser permissions
- Ensure camera is not used by other applications
- Try refreshing the page

**AR/3D features not loading:**
- Check browser WebGL support
- Update browser to latest version
- Disable browser extensions that might interfere

**Poor try-on quality:**
- Ensure good lighting
- Stand against plain background
- Keep full body in frame
- Use high-resolution images

**Model files missing:**
- Download required model files
- Place them in project root directory
- Check file permissions

### Performance Optimization

**For better performance:**
- Close unnecessary browser tabs
- Use Chrome or Firefox for best WebGL support
- Enable hardware acceleration in browser
- Use dedicated GPU if available

**For mobile devices:**
- Reduce camera resolution in code
- Disable shadows in 3D mode
- Use simplified avatar models

## 📱 Browser Compatibility

### Fully Supported
- Chrome 80+
- Firefox 75+
- Safari 13+
- Edge 80+

### Partially Supported
- Mobile browsers (limited AR features)
- Older browsers (basic features only)

## 🔒 Privacy & Security

- All processing happens locally in browser
- No images are sent to external servers
- Camera access requires user permission
- Captured images are stored locally only

## 🤝 Contributing

1. Fork the repository
2. Create feature branch
3. Make changes
4. Test thoroughly
5. Submit pull request

## 📄 License

This project is licensed under the MIT License.

## 🙏 Acknowledgments

- MediaPipe for pose detection
- Three.js for 3D rendering
- OpenCV for image processing
- TensorFlow.js for ML models
- CP-VTON for virtual try-on algorithm

## 📞 Support

For issues and questions:
1. Check troubleshooting section
2. Review browser console for errors
3. Ensure all requirements are met
4. Check model files are present

## 🔄 Updates

### Version 2.0 (Current)
- Added AR try-on with pose detection
- Implemented 3D virtual try-on
- Enhanced image preprocessing
- Improved camera handling
- Better error handling
- Mobile-responsive design

### Version 1.0 (Original)
- Basic virtual try-on
- Image upload functionality
- Live camera capture
- Clothing recommendation system