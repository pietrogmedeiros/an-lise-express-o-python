#!/usr/bin/env python3
"""
Instalação apenas do essencial - OpenCV + NumPy + Pandas
"""

import subprocess
import sys

def install_essentials():
    """Instala apenas o essencial que sempre funciona"""
    packages = [
        "opencv-python==4.8.1.78",
        "numpy==1.24.3",
        "pandas==2.0.3"
    ]
    
    print("📦 Instalando apenas dependências essenciais...")
    
    for package in packages:
        try:
            print(f"   Instalando {package}...")
            subprocess.check_call([
                sys.executable, "-m", "pip", "install", 
                package, "--no-cache-dir"
            ])
            print(f"   ✅ {package} OK")
        except subprocess.CalledProcessError as e:
            print(f"   ❌ Erro: {package}")
            return False
    
    return True

def test_system():
    """Testa se tudo está funcionando"""
    try:
        import cv2
        import numpy as np
        import pandas as pd
        
        print("✅ OpenCV:", cv2.__version__)
        print("✅ NumPy:", np.__version__)
        print("✅ Pandas:", pd.__version__)
        
        # Testar câmera
        cap = cv2.VideoCapture(0)
        if cap.isOpened():
            print("✅ Câmera acessível")
            cap.release()
        else:
            print("⚠️ Câmera não acessível")
        
        return True
    except Exception as e:
        print(f"❌ Erro no teste: {e}")
        return False

if __name__ == "__main__":
    print("🚀 Instalação Simples e Confiável")
    print("=" * 40)
    
    if install_essentials():
        if test_system():
            print("\n🎉 Sistema pronto!")
            print("📋 Execute: python3 main_opencv.py --mode camera")
        else:
            print("\n❌ Teste falhou")
    else:
        print("\n❌ Instalação falhou")