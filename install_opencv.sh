#!/bin/bash
# Script para instalar OpenCV no macOS

# Desinstalar versões conflitantes
pip uninstall opencv-python opencv-contrib-python opencv-python-headless -y

# Instalar versão compatível
pip install opencv-python==4.8.1.78

# Se ainda houver problemas, instalar via conda
# conda install -c conda-forge opencv