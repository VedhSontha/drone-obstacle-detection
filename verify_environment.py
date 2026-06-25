import sys
import os
from pathlib import Path

def check_dependencies() -> bool:
    print("=" * 60)
    print("🛸 DRONE OBSTACLE DETECTION - ENVIRONMENT VERIFICATION 🛸")
    print("=" * 60)
    
    all_ok = True
    
    # 1. Check Python Version
    print(f"[Python] version: {sys.version.split()[0]} (Recommended: 3.10+)")
    
    # 2. Check PyTorch & CUDA
    try:
        import torch
        print(f"[PyTorch] version: {torch.__version__} - Installed successfully")
        cuda_avail = torch.cuda.is_available()
        print(f"[CUDA] available: {cuda_avail}")
        if cuda_avail:
            print(f"[CUDA] device: {torch.cuda.get_device_name(0)}")
        else:
            print("[CUDA] Warning: Running on CPU. Training/Inference will be slower.")
    except ImportError:
        print("[PyTorch] ❌ NOT INSTALLED (Required for YOLO & PyTorch operations)")
        all_ok = False
        
    # 3. Check OpenCV
    try:
        import cv2
        print(f"[OpenCV] version: {cv2.__version__} - Installed successfully")
    except ImportError:
        print("[OpenCV] ❌ NOT INSTALLED (Required for image processing & video feed)")
        all_ok = False

    # 4. Check Ultralytics (YOLO)
    try:
        import ultralytics
        print(f"[Ultralytics] version: {ultralytics.__version__} - Installed successfully")
    except ImportError:
        print("[Ultralytics] ❌ NOT INSTALLED (Required for YOLOv8/v11 inference)")
        all_ok = False

    # 5. Check DroNet Model Checkpoints
    dronet_json = Path("of-obstacledetection/DroNeTello/models/DroNet/model_struct.json")
    dronet_weights = Path("of-obstacledetection/DroNeTello/models/DroNet/model_weights_new_best.h5")
    
    print("-" * 60)
    print("📂 CHECKING LOCAL CHECKPOINTS:")
    if dronet_json.exists():
        print(f"  [DroNet] Structure: Found ({dronet_json})")
    else:
        print(f"  [DroNet] ⚠️ Structure: Missing ({dronet_json})")
        
    if dronet_weights.exists():
        print(f"  [DroNet] Weights: Found ({dronet_weights})")
    else:
        print(f"  [DroNet] ⚠️ Weights: Missing ({dronet_weights})")
        
    print("=" * 60)
    return all_ok

if __name__ == "__main__":
    success = check_dependencies()
    if not success:
        print("[Status] ❌ Environment verification failed. Please install missing core dependencies.")
        sys.exit(1)
    else:
        print("[Status] ✅ All core dependencies verified successfully!")
        sys.exit(0)
