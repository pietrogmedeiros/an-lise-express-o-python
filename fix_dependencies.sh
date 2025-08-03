#!/bin/bash
echo "🧹 Limpando instalações anteriores..."

# Desinstalar todas as versões conflitantes
pip uninstall opencv-python opencv-contrib-python opencv-python-headless tensorflow tensorflow-macos tensorflow-metal -y

echo "📦 Instalando dependências para macOS..."

# Para macOS com Apple Silicon (M1/M2)
if [[ $(uname -m) == 'arm64' ]]; then
    echo "🍎 Detectado Apple Silicon - instalando versões otimizadas"
    pip install tensorflow-macos==2.13.0
    pip install tensorflow-metal==1.0.1
else
    echo "💻 Detectado Intel Mac - instalando TensorFlow padrão"
    pip install tensorflow==2.13.0
fi

# Instalar OpenCV
pip install opencv-python==4.8.1.78

# Outras dependências
pip install numpy==1.24.3
pip install pandas==2.0.3
pip install matplotlib==3.7.2
pip install streamlit==1.25.0
pip install plotly==5.15.0

echo "✅ Instalação concluída!"