#!/usr/bin/env python3
"""
Script para verificar se todas as dependências estão instaladas corretamente
"""

def check_imports():
    success = True
    
    try:
        import cv2
        print("✅ OpenCV importado com sucesso")
        print(f"   Versão: {cv2.__version__}")
    except ImportError as e:
        print(f"❌ Erro ao importar OpenCV: {e}")
        success = False
    
    try:
        import numpy as np
        print("✅ NumPy importado com sucesso")
        print(f"   Versão: {np.__version__}")
    except ImportError as e:
        print(f"❌ Erro ao importar NumPy: {e}")
        success = False
    
    try:
        import pandas as pd
        print("✅ Pandas importado com sucesso")
        print(f"   Versão: {pd.__version__}")
    except ImportError as e:
        print(f"❌ Erro ao importar Pandas: {e}")
        success = False
    
    # TensorFlow é opcional - não quebra o sistema se não estiver disponível
    try:
        import tensorflow as tf
        print("✅ TensorFlow importado com sucesso")
        print(f"   Versão: {tf.__version__}")
        print("   🤖 IA avançada disponível")
    except ImportError:
        print("⚠️  TensorFlow não instalado")
        print("   📝 Sistema funcionará em modo básico (sem IA)")
        print("   💡 Para instalar: pip3 install tensorflow-macos")
    except Exception as e:
        print(f"⚠️  TensorFlow com problemas: {e}")
        print("   📝 Sistema funcionará em modo básico")
    
    return success

def test_camera():
    try:
        import cv2
        cap = cv2.VideoCapture(0)
        if cap.isOpened():
            print("✅ Câmera acessível")
            cap.release()
            return True
        else:
            print("❌ Câmera não acessível")
            return False
    except Exception as e:
        print(f"❌ Erro na câmera: {e}")
        return False

if __name__ == "__main__":
    print("🔍 Verificando dependências...")
    print("=" * 40)
    
    deps_ok = check_imports()
    camera_ok = test_camera()
    
    print("\n" + "=" * 40)
    
    if deps_ok and camera_ok:
        print("🎉 Sistema pronto para usar!")
        print("📋 Comandos disponíveis:")
        print("   python3 main_simple.py --mode camera")
        print("   python3 main_simple.py --mode report")
    elif deps_ok:
        print("⚠️  Dependências OK, mas câmera com problema")
        print("💡 Verifique se outra app está usando a câmera")
    else:
        print("❌ Instale as dependências faltantes:")
        print("   pip3 install opencv-python pandas numpy")
