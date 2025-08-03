#!/usr/bin/env python3
"""
Sistema inteligente que funciona com ou sem IA
"""

import argparse
import sys
import os
import cv2
import time
from datetime import datetime

# Adicionar src ao path
sys.path.append('src')

from emotion_detector_smart import SmartEmotionDetector
from data_manager import DataManager

def main():
    parser = argparse.ArgumentParser(description='Sistema Inteligente de Emoções')
    parser.add_argument('--mode', choices=['camera', 'report'], 
                       default='camera', help='Modo de execução')
    
    args = parser.parse_args()
    
    if args.mode == 'camera':
        print("🧠 Iniciando detector inteligente...")
        
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print("❌ Câmera não acessível")
            return
        
        detector = SmartEmotionDetector()
        data_manager = DataManager()
        
        emotion_counter = {}
        last_save_time = time.time()
        save_interval = 3

        print("🎮 Controles: 'q'=sair, 's'=salvar, 'i'=info")

        try:
            while True:
                ret, frame = cap.read()
                if not ret:
                    break
                
                processed_frame, emotions = detector.detect_emotion(frame)
                
                # Contar emoções
                for emotion_data in emotions:
                    emotion = emotion_data['emotion']
                    emotion_counter[emotion] = emotion_counter.get(emotion, 0) + 1
                
                # Salvar automaticamente
                current_time = time.time()
                if emotions and (current_time - last_save_time) > save_interval:
                    best_emotion = max(emotions, key=lambda x: x['confidence'])
                    data_manager.save_emotion(
                        best_emotion['emotion'], 
                        best_emotion['confidence']
                    )
                    last_save_time = current_time
                    print(f"💾 {best_emotion['emotion']} ({best_emotion['confidence']:.2f})")
                
                # Interface
                status = "🤖 IA" if detector.ai_available else "🧠 Básico+"
                cv2.putText(processed_frame, f"{status}", 
                           (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
                cv2.putText(processed_frame, f"Faces: {len(emotions)}", 
                           (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
                
                if emotion_counter:
                    most_common = max(emotion_counter, key=emotion_counter.get)
                    cv2.putText(processed_frame, f"Dominante: {most_common}", 
                               (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
                
                cv2.imshow('🧠 Detector Inteligente', processed_frame)
                
                key = cv2.waitKey(1) & 0xFF
                if key == ord('q'):
                    break
                elif key == ord('s') and emotions:
                    best_emotion = max(emotions, key=lambda x: x['confidence'])
                    data_manager.save_emotion(best_emotion['emotion'], best_emotion['confidence'])
                    print(f"💾 Salvo: {best_emotion['emotion']}")
                elif key == ord('i'):
                    print(f"\n📊 Estatísticas:")
                    for emotion, count in emotion_counter.items():
                        print(f"   {emotion}: {count}")
                    print(f"🤖 IA: {'Ativa' if detector.ai_available else 'Básico+'}")
        
        except KeyboardInterrupt:
            print("\n👋 Encerrando...")
        finally:
            cap.release()
            cv2.destroyAllWindows()

if __name__ == "__main__":
    main()