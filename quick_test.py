#!/usr/bin/env python3
"""
Teste rápido - use python3 quick_test.py
"""

def test_all():
    try:
        print("🔍 Testando dependências...")
        
        import numpy as np
        print(f"✅ NumPy {np.__version__}")
        
        import cv2
        print(f"✅ OpenCV {cv2.__version__}")
        
        import pandas as pd
        print(f"✅ Pandas {pd.__version__}")
        
        # Teste da câmera
        cap = cv2.VideoCapture(0)
        if cap.isOpened():
            print("✅ Câmera acessível")
            cap.release()
        else:
            print("⚠️ Câmera não acessível (normal se não tiver)")
        
        print("\n🎉 Tudo OK! Execute:")
        print("python3 main_simple.py --mode camera")
        
        return True
        
    except Exception as e:
        print(f"❌ Erro: {e}")
        return False

if __name__ == "__main__":
    test_all()