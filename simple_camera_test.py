#!/usr/bin/env python3
"""
Teste básico do sistema sem dependências pesadas
"""

import cv2
import sys
import os

# Adicionar src ao path
sys.path.append('src')

try:
    from emotion_detector_basic import BasicEmotionDetector
    from data_manager import DataManager
except ImportError as e:
    print(f"❌ Erro de importação: {e}")
    print("Execute: pip install opencv-python pandas")
    sys.exit(1)

def main():
    print("🎥 Iniciando teste básico...")
    
    # Testar câmera primeiro
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("❌ Erro: Câmera não acessível")
        return
    
    print("✅ Câmera OK - iniciando detector...")
    
    try:
        detector = BasicEmotionDetector()
        data_manager = DataManager()
        
        print("Pressione 'q' para sair, 's' para salvar emoção")
        
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            
            # Detectar emoções
            processed_frame, emotions = detector.detect_emotion(frame)
            
            # Mostrar informações
            cv2.putText(processed_frame, f"Faces: {len(emotions)}", 
                       (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
            
            cv2.imshow('Teste Basico - Detector de Emocoes', processed_frame)
            
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                break
            elif key == ord('s') and emotions:
                # Salvar emoção detectada
                best_emotion = max(emotions, key=lambda x: x['confidence'])
                data_manager.save_emotion(
                    best_emotion['emotion'], 
                    best_emotion['confidence']
                )
                print(f"💾 Salvo: {best_emotion['emotion']} ({best_emotion['confidence']})")
        
    except Exception as e:
        print(f"❌ Erro durante execução: {e}")
    
    finally:
        cap.release()
        cv2.destroyAllWindows()
        print("👋 Teste finalizado")

if __name__ == "__main__":
    main()