#!/usr/bin/env python3
"""
Executar sem ambiente virtual - direto no sistema
"""

import os
import sys
import subprocess

def check_opencv():
    """Verifica se OpenCV está instalado"""
    try:
        import cv2
        print(f"✅ OpenCV {cv2.__version__} encontrado!")
        return True
    except ImportError:
        print("❌ OpenCV não encontrado")
        return False

def install_opencv():
    """Instala OpenCV no sistema"""
    try:
        print("📦 Instalando OpenCV no sistema...")
        subprocess.check_call([
            "/usr/bin/python3", "-m", "pip", "install", 
            "opencv-python", "--user", "--break-system-packages"
        ])
        print("✅ OpenCV instalado!")
        return True
    except Exception as e:
        print(f"❌ Erro: {e}")
        return False

def run_detector():
    """Executa o detector"""
    try:
        print("🚀 Executando detector...")
        subprocess.check_call(["/usr/bin/python3", "detector_simples.py"])
    except KeyboardInterrupt:
        print("\n👋 Detector encerrado")
    except Exception as e:
        print(f"❌ Erro ao executar: {e}")

def main():
    print("🔧 Configuração Simples")
    print("=" * 30)
    
    # Verificar se está em ambiente virtual
    if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        print("⚠️  Detectado ambiente virtual")
        print("💡 Vamos usar Python do sistema")
    
    # Verificar OpenCV
    if not check_opencv():
        print("📦 Instalando OpenCV...")
        if not install_opencv():
            print("❌ Falha na instalação")
            print("💡 Tente manualmente:")
            print("   pip3 install opencv-python --user")
            return
    
    # Executar detector
    run_detector()

if __name__ == "__main__":
    main()