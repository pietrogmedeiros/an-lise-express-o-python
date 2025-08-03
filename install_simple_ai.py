#!/usr/bin/env python3
"""
Instalação simplificada de IA local
"""

import subprocess
import sys

def install_basic_packages():
    """Instala apenas pacotes básicos e confiáveis"""
    packages = [
        "opencv-python==4.8.1.78",
        "numpy==1.24.3", 
        "pandas==2.0.3"
    ]
    
    for package in packages:
        try:
            print(f"📦 Instalando {package}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            print(f"✅ {package} instalado!")
        except subprocess.CalledProcessError:
            print(f"❌ Erro ao instalar {package}")
            return False
    return True

def try_install_fer():
    """Tenta instalar FER, mas não falha se não conseguir"""
    try:
        print("🤖 Tentando instalar FER (IA)...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "fer", "--no-deps"])
        print("✅ FER instalado!")
        return True
    except:
        print("⚠️ FER não instalou - usando modo básico")
        return False

def test_imports():
    """Testa importações"""
    try:
        import cv2
        import numpy as np
        import pandas as pd
        print("✅ Dependências básicas OK")
        
        try:
            from fer import FER
            print("✅ FER disponível - IA ativa")
            return True
        except:
            print("⚠️ FER não disponível - modo básico ativo")
            return False
    except Exception as e:
        print(f"❌ Erro: {e}")
        return False

if __name__ == "__main__":
    print("🚀 Instalação simplificada...")
    print("=" * 40)
    
    if install_basic_packages():
        try_install_fer()
        test_imports()
        
        print("\n🎉 Sistema pronto!")
        print("📋 Execute: python3 main_smart.py --mode camera")
    else:
        print("\n❌ Falha na instalação básica")