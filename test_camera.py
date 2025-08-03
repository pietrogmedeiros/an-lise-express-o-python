#!/usr/bin/env python3
"""
Teste simples da câmera sem dependências pesadas
"""

import cv2
import sys

def test_camera():
    print("🎥 Testando acesso à câmera...")
    
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("❌ Erro: Não foi possível acessar a câmera")
        return False
    
    print("✅ Câmera acessada com sucesso!")
    print("Pressione 'q' para sair")
    
    while True:
        ret, frame = cap.read()
        if not ret:
            print("❌ Erro ao capturar frame")
            break
        
        # Mostrar frame
        cv2.imshow('Teste da Camera', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()
    print("👋 Teste finalizado")
    return True

if __name__ == "__main__":
    test_camera()