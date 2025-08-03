#!/usr/bin/env python3
"""
Sistema básico de detecção - sem IA, 100% funcional
"""

import cv2
import time
import sys
import os
from datetime import datetime

# Adicionar src ao path
sys.path.append('src')

from emotion_detector_basic import BasicEmotionDetector

def main():
    print("😊 Iniciando detector básico...")
    
    # Testar câmera
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("❌ Câmera não acessível")
        print("💡 Dicas:")
        print("   - Feche outras apps que usam câmera")
        print("   - Verifique permissões do macOS")
        return
    
    detector = BasicEmotionDetector()
    
    # Contadores
    emotion_counter = {}
    total_detections = 0
    start_time = time.time()
    
    print("🎮 Controles:")
    print("   'q' = Sair")
    print("   'r' = Reset estatísticas")
    print("   'i' = Mostrar info")
    
    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("❌ Erro ao capturar frame")
                break
            
            # Detectar emoções
            processed_frame, emotions = detector.detect_emotion(frame)
            
            # Contar emoções
            for emotion_data in emotions:
                emotion = emotion_data['emotion']
                emotion_counter[emotion] = emotion_counter.get(emotion, 0) + 1
                total_detections += 1
            
            # Interface na tela
            runtime = time.time() - start_time
            cv2.putText(processed_frame, "😊 Detector Basico", 
                       (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
            cv2.putText(processed_frame, f"Faces: {len(emotions)}", 
                       (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
            cv2.putText(processed_frame, f"Total: {total_detections}", 
                       (10, 85), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
            cv2.putText(processed_frame, f"Tempo: {runtime:.0f}s", 
                       (10, 110), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
            
            # Mostrar emoção dominante
            if emotion_counter:
                dominant = max(emotion_counter, key=emotion_counter.get)
                cv2.putText(processed_frame, f"Dominante: {dominant}", 
                           (10, 135), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
            
            # Mostrar frame
            cv2.imshow('😊 Detector Basico de Emocoes', processed_frame)
            
            # Controles
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                break
            elif key == ord('r'):
                emotion_counter.clear()
                total_detections = 0
                start_time = time.time()
                detector.face_states.clear()
                print("🔄 Estatísticas resetadas")
            elif key == ord('i'):
                print(f"\n📊 Estatísticas:")
                print(f"   Tempo total: {runtime:.1f}s")
                print(f"   Total detecções: {total_detections}")
                for emotion, count in emotion_counter.items():
                    percentage = (count / total_detections * 100) if total_detections > 0 else 0
                    print(f"   {emotion}: {count} ({percentage:.1f}%)")
                stats = detector.get_stats()
                print(f"   Faces rastreadas: {stats['faces_tracked']}")
                print(f"   Frames processados: {stats['frames_processed']}")
    
    except KeyboardInterrupt:
        print("\n👋 Encerrando...")
    finally:
        cap.release()
        cv2.destroyAllWindows()
        
        # Estatísticas finais
        if total_detections > 0:
            print(f"\n📈 Resumo Final:")
            print(f"   Total de detecções: {total_detections}")
            print(f"   Tempo total: {time.time() - start_time:.1f}s")
            print(f"   Emoções detectadas:")
            for emotion, count in emotion_counter.items():
                percentage = count / total_detections * 100
                print(f"     {emotion}: {count} ({percentage:.1f}%)")

if __name__ == "__main__":
    main()