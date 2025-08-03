#!/usr/bin/env python3
"""
Instalador simples do OpenCV
"""

import subprocess
import sys

def instalar():
    try:
        print("📦 Instalando OpenCV...")
        subprocess.run([
            sys.executable, "-m", "pip", "install", 
            "opencv-python", "--user"
        ], check=True)
        print("✅ OpenCV instalado!")
        return True
    except:
        print("❌ Erro na instalação")
        return False

def testar():
    try:
        import cv2
        print(f"✅ OpenCV {cv2.__version__} funcionando!")
        return True
    except:
        print("❌ OpenCV não funciona")
        return False

if __name__ == "__main__":
    print("🚀 Instalador OpenCV")
    print("=" * 25)
    
    if instalar():
        if testar():
            print("\n🎉 Pronto!")
            print("📋 Execute: python3 detector_simples.py")
        else:
            print("\n❌ Instalação falhou")
    else:
        print("\n❌ Não foi possível instalar")
