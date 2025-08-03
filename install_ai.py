#!/usr/bin/env python3
"""
Script para instalar IA gratuita local para detecção de emoções
"""

import subprocess
import sys

def install_fer():
    """Instala FER - biblioteca de IA gratuita para emoções"""
    try:
        print("📦 Instalando FER (IA gratuita para emoções)...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "fer"])
        print("✅ FER instalado com sucesso!")
        return True
    except subprocess.CalledProcessError:
        print("❌ Erro ao instalar FER")
        return False

def test_fer():
    """Testa se FER está funcionando"""
    try:
        from fer import FER
        print("✅ FER importado com sucesso!")
        
        # Criar detector
        detector = FER(mtcnn=True)
        print("✅ Detector FER criado!")
        print("🤖 IA local pronta para usar!")
        return True
    except ImportError as e:
        print(f"❌ Erro ao importar FER: {e}")
        return False
    except Exception as e:
        print(f"❌ Erro no FER: {e}")
        return False

if __name__ == "__main__":
    print("🚀 Configurando IA gratuita local...")
    print("=" * 50)
    
    if install_fer():
        if test_fer():
            print("\n🎉 IA local configurada com sucesso!")
            print("📋 Agora execute:")
            print("   python3 main_ai.py --mode camera")
        else:
            print("\n⚠️ Instalação OK, mas teste falhou")
    else:
        print("\n❌ Falha na instalação")