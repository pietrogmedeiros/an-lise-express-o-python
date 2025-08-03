#!/usr/bin/env python3
"""
Instalação básica - apenas OpenCV
"""

import subprocess
import sys

def install_opencv():
    """Instala apenas OpenCV"""
    try:
        print("📦 Instalando OpenCV...")
        subprocess.check_call([
            sys.executable, "-m", "pip", "install", 
            "opencv-python", "--no-cache-dir"
        ])
        print("✅ OpenCV instalado!")
        return True
    except:
        print("❌ Erro ao instalar OpenCV")
        return False

def test_opencv():
    """Testa OpenCV"""
    try:
        import cv2
        print(f"✅ OpenCV {cv2.__version__} funcionando!")
        
        # Testar câmera
        cap = cv2.VideoCapture(0)
        if cap.isOpened():
            print("✅ Câmera OK")
            cap.release()
        else:
            print("⚠️ Câmera não detectada")
        
        return True
    except Exception as e:
        print(f"❌ Erro: {e}")
        return False

if __name__ == "__main__":
    print("🚀 Instalação Básica")
    print("=" * 30)
    
    if install_opencv():
        if test_opencv():
            print("\n🎉 Pronto!")
            print("📋 Execute: python3 main_basic.py")
        else:
            print("\n❌ Teste falhou")
    else:
        print("\n❌ Instalação falhou")